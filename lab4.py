from flask import Blueprint, render_template, request, redirect, url_for
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html', username=username)

    error = 'Неверный логин и/или пароль'
    return render_template('login.html', error=error, username=username, password=password)
    
@lab4.route('/lab4/holodilnik', methods = ['GET', 'POST'])
def holodilnik():
    if request.method == 'GET':
        return render_template('holodilnik.html')

    temperature = request.form.get('temperature')
    if not temperature:
        vtemp  = 'Ошибка: не задана температура!'
    elif int(temperature) < -12:
        vtemp = 'Не удалось установить температуру - слишком низкое значение!'
    elif int(temperature) > -1:
        vtemp = 'Не удалось установить температуру - слишком высокое значение!'
    elif int(temperature) > -12 and int(temperature) < -9:
        vtemp = f"Установлена температура: {temperature}°C ***"
    elif int(temperature) >= -8 and int(temperature) <= -5:
        vtemp = f"Установлена температура: {temperature}°C **"
    elif int(temperature) >= -4 and int(temperature) <= -1:
        vtemp = f"Установлена температура: {temperature}°C *"
    
    return render_template('holodilnik.html', vtemp=vtemp)

@lab4.route('/lab4/zerno', methods = ['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")

    return render_template('zerno.html')

@lab4.route('/lab4/payzerno', methods = ['GET', 'POST'])
def payzerno():
    if request.method == 'GET':
        return render_template("payzerno.html")

    price = 0
    zerno = request.form.get('zerno')
    
    if zerno == 'Ячмень':
        price = 12000
    elif zerno == 'Овёс':
        price = 8500
    elif zerno == 'Пшеница':
        price = 8700
    elif zerno == 'Рожь':
        price = 14000
    else:
        price = 0
    
    weight = int(request.form.get('weight'))

    if weight > 50:
        final_price = (weight * price) - ((weight * price) * 10 / 100)
        sale = 'Применина скидка 10% за большой объем!'
    elif weight <= 0:
        final_price = 'Ошибка!'
        sale = 'Неверное значение веса!'
    else:
        final_price = weight * price
        sale = 0

    if weight > 500:
        final_price = 'Ошибка!'
        sale = 'Такого объема сейчас нет в наличии!'
    
    return render_template('payzerno.html', zerno=zerno, price=price, weight=weight, final_price=final_price, sale=sale)

@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    text_color = request.form.get('text_color')
    background_color = request.form.get('background_color')
    font_size = request.form.get('font_size')

    if text_color == background_color:
        error = 'Цвет текста не должен совпадать с цветом фона'
        
        return render_template('cookies.html', error=error)

    headers = {
        'Set-Cookie': [
            'text_color=' + text_color + '; path=/',
            'background_color=' + background_color + '; path=/',
            'font_size=' + font_size + '; path=/'
        ],
        'Location': '/lab4/cookies'
    }
    return '', 303, headers