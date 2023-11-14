from flask import Blueprint, render_template, request, redirect
import psycopg2

lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="knowledge_base_for_anastasia_udodova",
        user="anastasia_udodova_knowledge_base",
        password="0123456789")

    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    conn.close()
    cur.close()

    cur.execute("SELECT * FROM users")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"


@lab5.route('/lab5/users')
def get_users():
    connection = dbConnect()
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM users")

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('lab5.html', users=results)

