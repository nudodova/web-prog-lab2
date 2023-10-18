from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def labrab():

    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
        errors['age'] = 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    
    price = 0
    drink = request.args.get('drink')

    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    errors = {}
    card = request.args.get('card')
    if card == '':
        errors['card'] = 'Заполните поле!'
    name = request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'
    cvv = request.args.get('cvv')
    if cvv == '':
        errors['cvv'] = 'Заполните поле!'
    return render_template('pay.html', price=price, card=card, name=name, cvv=cvv, errors=errors)

@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    fio = request.args.get('fio')
    if fio == '':
        errors['fio'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    departure = request.args.get('departure')
    if departure == '':
        errors['departure'] = 'Заполните поле!'
    destination = request.args.get('destination')
    if destination == '':
        errors['destination'] = 'Заполните поле!'
    date = request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    typee = request.args.get('typee')
    berth = request.args.get('berth')
    luggage = request.args.get('luggage')
    return render_template('ticket.html', fio=fio, age=age, departure=departure, destination=destination, date=date, typee=typee, berth=berth, luggage=luggage, errors=errors)

