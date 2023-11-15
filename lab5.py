from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="knowledge_base_for_anastasia_udodova",
        user="anastasia_udodova_knowledge_base",
        password="0123456789")

    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"


@lab5.route('/lab5/users')
def get_users():
    connection = dbConnect()
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM users")

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('lab5.html', users=results)

@lab5.route('/lab5/mainpage')
def mainpage():
    username = session.get('username')
    return render_template('mainpage.html', username=username)

@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerpage():
    errors=[]

    if request.method == "GET":
        return render_template("register.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля!")
        print(errors)
        return render_template("register.html", errors=errors)

    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username,))

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует!")
        
        conn.close()
        cur.close()

        return render_template("register.html", errors=errors)

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    conn.commit()
    conn.close()
    cur.close()

    return redirect("/lab5/login")


@lab5.route('/lab5/loginn', methods=["GET", "POST"])
def loginpage():
    errors = []

    if request.method == "GET":
        return render_template("loginn.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля!")
        return render_template("loginn.html", errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    results = cur.fetchone()

    if results is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors)

    userId, hashPassword = results

    if check_password_hash(hashPassword, password):
        session['id'] =userId
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/mainpage")

    else:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors)


@lab5.route("/lab5/newtitle", methods = ["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get('id')
    username = session.get('username')
    if userID is not None:
        if request.method =="GET":
            return render_template("newtitle.html", username=username)
        
        if request.method == "POST":
            article_text = request.form.get("article_text")
            title = request.form.get("article_title")

            if len(article_text)==0:
                errors.append("Заполните текст")
                return render_template("newtitle.html", errors = errors, username=username)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, article_text))
            
            
            new_articl_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_articl_id}")

    return redirect("/lab5/loginn")



@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s AND user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines()

    return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=session.get("username"))

@lab5.route('/lab5/articles')
def list_articles():
    userID = session.get('id')
    username = session.get("username")
    
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute("SELECT id, title FROM articles WHERE user_id = %s;", (userID,))
        articles_data = cur.fetchall()
        
        articles = [{'id': row[0], 'title': row[1]} for row in articles_data]

        dbClose(cur, conn)

        return render_template('articles.html', articles=articles, username=username)

    return redirect("/lab5/loginn")

@lab5.route('/lab5/logout', methods=["GET"])
def logout():
    session.clear()
    return redirect("/lab5/loginn")


@lab5.route('/lab5/publish_article', methods=["POST"])
def publish_article():
    if 'username' in session:
        article_id = request.form.get('article_id')
       
        article = Article.query.filter_by(id=article_id, author=session['username']).first()
        if article:
            article.published = True
            db.session.commit()
            return "Article published successfully"
        else:
            return "You do not have permission to publish this article"
    else:
        return redirect("/lab5/loginn")


