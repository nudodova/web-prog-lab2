from flask import Flask, redirect, url_for, render_template
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
        <li><a href='/lab2'>Лабораторная работа 2</a></li>
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
        <a href="/menu">Меню</a>
        <h2>Реализованные роуты</h2>
        <li><a href='/lab1/oak'>Дуб</a></li>
        <li><a href='/lab1/student'>Студент</a></li>
        <li><a href='/lab1/python'>Python</a></li>
        <li><a href='/lab1/html'>HTML</a></li>
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

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="/static/lab1.css">
    <body>
        <h1>Удодова Анастасия Александровна</h1>
        <img src="''' + url_for('static', filename='student.jpg') + '''">
       
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="/static/lab1.css">
    <body>
        <div>Python — это язык программирования, который широко используется в интернет-приложениях, разработке 
        программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python, потому что 
        он эффективен, прост в изучении и работает на разных платформах. Программы на языке Python можно скачать бесплатно, 
        они совместимы со всеми типами систем и повышают скорость разработки.</div>

        <div>Веб-разработка на стороне сервера включает в себя сложные серверные функции, с помощью которых веб-сайты отображают 
        информацию для пользователя. Например, веб-сайты должны взаимодействовать с базами данных и другими веб-сайтами, а также 
        защищать данные при их отправке по сети. </div>

        <div>Python полезен при написании серверного кода, поскольку он предлагает множество библиотек, состоящих из предварительно 
        написанного кода для сложных серверных функций. Также разработчики используют широкий спектр платформ Python, которые предоставляют 
        все необходимые инструменты для более быстрого и простого создания интернет-приложений. Например, разработчики могут создать «скелет» 
        интернет-приложения за считанные секунды, потому что им не нужно писать код с нуля. Затем его можно протестировать с помощью инструментов 
        тестирования платформы независимо от внешних инструментов тестирования.</div>

        <img src="''' + url_for('static', filename='Python.png') + '''">
       
    </body>
</html>
'''
@app.route('/lab1/html')
def html():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="/static/lab1.css">
    <body>
        <div>HTML (от английского HyperText Markup Language) — это язык гипертекстовой разметки текста. Он нужен, чтобы размещать на веб-странице элементы: текст, картинки, таблицы и видео.</div>

        <div>Когда вы заходите на сайт, браузер подгружает HTML-файл с информацией о структуре и контенте веб-страницы. HTML как бы выстраивает визуальный фундамент сайта, но не «запускает» сайт самостоятельно. Он всего лишь указывает, где располагаются элементы, какой у них будет базовый дизайн, откуда брать стили для элементов и скрипты (обычно их пишут на JavaScript).</div>


        <img src="''' + url_for('static', filename='html.jpg') + '''">
       
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Анастасия Удодова'
    numberlab = 2
    group = 'ФБИ-14'
    kurs = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price':100},
        {'name': 'груши', 'price':120},
        {'name': 'апельсины', 'price':80},
        {'name': 'мандарины', 'price':95},
        {'name': 'манго', 'price':321},
    ]   
    books = [
        {'author': 'Михаил Булгаков', 'name': 'Мастер и Маргарита', 'genre': 'роман', 'pages': '400 страниц'},
        {'author': 'Антуан де Сент-Экзюпери', 'name': 'Маленький принц', 'genre': 'повесть-сказка', 'pages': '160 страниц'},
        {'author': 'Лев Толстой', 'name': 'Война и мир', 'genre': 'роман-эпопея', 'pages': '1300 страниц'},
        {'author': 'Федор Достоевский', 'name': 'Преступление и наказание', 'genre': 'роман', 'pages': '592 страниц'},
        {'author': 'Михаил Лермонтов', 'name': 'Герой нашего времени', 'genre': 'роман', 'pages': '192 страниц'},
        {'author': 'Александр Пушкин', 'name': 'Евгений Онегин', 'genre': 'роман в стихах', 'pages': '224 страниц'},
        {'author': 'Габриэль Гарсиа Маркес', 'name': 'Сто лет одиночества', 'genre': 'роман', 'pages': '544 страниц'},
        {'author': 'Николай Гоголь', 'name': 'Мёртвые души', 'genre': 'поэма', 'pages': '350 страниц'},
        {'author': 'Лев Толстой', 'name': 'Анна Каренина', 'genre': 'роман', 'pages': '850 страниц'},
        {'author': 'Эрих Мария Ремарк', 'name': 'Три товарища', 'genre': 'роман', 'pages': '480 страниц'},
        {'author': 'Маргарет Митчелл', 'name': 'Унесённые ветром', 'genre': 'роман', 'pages': '1400 страниц'},
        {'author': 'Эрнест Хемингуэй', 'name': 'Старик и море', 'genre': 'повесть', 'pages': '127 страниц'},
    ]   
    return render_template('example.html', name=name, numberlab=numberlab, group=group, kurs=kurs, fruits=fruits, books=books)

    @app.route('/lab2')
    def lab2():
        
        return render_template('lab2.html')

    @app.route('/lab2/fashionweek23')
    def fashionweek():

        return render_template('fashionweek23.html')