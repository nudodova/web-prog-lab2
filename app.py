from flask import Flask, redirect, url_for
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
<link rel="stylesheet" href="/static/lab1.css">  
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
 <link rel="stylesheet" href="/static/lab1.css">   
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

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="/static/lab1.css">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
       
    </body>
</html>
'''