from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def statrt():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Удодова Анастасия Александровна, лабораторная работа 1</title>
      </head>
      <body>
        <header>
            НГТУ, ФБ, Лабораторные работы
        </header>

        <h1>НГТУ, ФБ, WEB-программирование 2 часть. Список лабораторных работ</h1>
        <li><a href='/lab1'>Лабораторная работа 1</a></li>

        <footer>
            &copy; Удодова Анастасия, ФБИ-14,3 курс, 2023
        </footer>
    </body>
</html>
"""  

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Удодова Анастасия Александровна. Лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>WEB-сервер на flask</h1>
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>

        <footer>
            &copy; Удодова Анастасия, ФБИ-14,3 курс, 2023
        </footer>
    </body>
</html>
"""