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

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует!")
        
        conn.close()
        cur.close()

        return render_template("register.html", errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")

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

    cur.execute(f"SELECT id, password FROM users WHERE username ='{username}'")

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

