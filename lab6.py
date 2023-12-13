from flask import Blueprint, render_template, request, redirect, url_for
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab():
    return render_template('lab6.html')


@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route('/lab6/checkarticles')
def main2():
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console!"

@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    errors=[]

    if request.method == "GET":
        return render_template("register1.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not username_form:
        errors.append("Пожалуйста, заполните поле имени!")
        print(errors)
        return render_template("register1.html", errors=errors)

    if len(password_form) < 5:
        errors.append("Пароль должен быть не менее 5 символов!")
        print(errors)
        return render_template("register1.html", errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors.append("Пользователь с таким именем уже существует")
        print(errors)
        return render_template("register1.html", errors=errors)

    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors=[]

    if request.method == "GET":
        return render_template("loginn2.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors.append("Пожалуйста, заполните все поля!")
        return render_template("loginn2.html", errors=errors)

    

    my_user = users.query.filter_by(username=username_form).first()

    if not my_user:
        errors.append("Пользователя с таким именем не существует!")
        return render_template("loginn2.html", errors=errors)

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")
        else:
            errors.append("Неправильный пароль")
        return render_template("loginn2.html", errors=errors)

    return render_template("loginn2.html")

@lab6.route("/lab6/articles", methods = ['GET', 'POST'])
@login_required
def view_articles():
    username_form = request.form.get('username')
    my_articles = articles.query.filter((articles.user_id == current_user.id)).all()
    print(my_articles)
    return render_template('list_articles.html', articles=my_articles, username_form = username_form)


@lab6.route("/lab6/newtitle", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("newtitle6.html")

    article_text = request.form.get("article_text")
    title = request.form.get("article_title")
    

    if len(article_text) == 0:
        errors = ["Заполните текст"]
        return render_template("newtitle6.html", errors=errors)

    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)


    db.session.add(new_article)
    db.session.commit()

    return redirect("/lab6/articles")

@lab6.route('/lab6/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab6/login')

@lab6.route("/lab6/articles/<int:article_id>", methods=['GET', 'POST'])
def getArticle(article_id):
    if current_user.is_authenticated:
        article = articles.query.filter_by(id=article_id).first()

        if article:
            if article.user_id == current_user.id or article.is_public:
                text = article.article_text.splitlines()
                likes_count = article.likes
                return render_template("6articleN.html", article_text=text, article_title=article.title, username=current_user.username, favorite=article.is_favorite, likes_count=likes_count)
            else:
                return "У вас нет доступа к этой статье"
        else:
            return "Статья не найдена"
    else:
        return "Пожалуйста, войдите, чтобы увидеть эту статью"