from flask import Flask
app = Flask(__name__)

@app.route("/")
def statrt():
    return "web-сервер на flask"