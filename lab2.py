from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/")
@lab2.route("/index")
def statrt():
    return redirect("/menu", code=302)


@lab2.route("/menu")
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
        <li><a href='/lab2/'>Лабораторная работа 2</a></li>
        <footer>
            &copy; Удодова Анастасия, ФБИ-14,3 курс, 2023
        </footer>
    </body>
</html>
"""  


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def labor():
        
    return render_template('lab2.html')


@lab2.route('/lab2/fashionweek23')
def fashionweek():

    return render_template('fashionweek23.html')