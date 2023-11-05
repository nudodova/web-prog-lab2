from flask import Blueprint, render_template, request, redirect, url_for
lab5 = Blueprint('lab5', __name__)


@lab4.route('/lab5/')
def lab():
    return render_template('lab5.html')