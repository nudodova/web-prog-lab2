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