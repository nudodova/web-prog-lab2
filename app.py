from flask import Flask
app = Flask(__name__)

@app.route("/")
def statrt():
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

        <footer>
            &copy; Удодова Анастасия, ФБИ-14,3 курс, 2023
        </footer>
    </body>
</html>
"""
