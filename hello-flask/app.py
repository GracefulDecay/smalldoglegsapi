import pymysql
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)





def call_databse(query, type="select"):
    try:
        connection = pymysql.connect(
            host="162.144.4.132",
            database="shelbith_main",
            user="shelbith_super_user",
            password="Louise2016Clem",
            port=3306,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                if type == "insert":
                    connection.commit()
        return result
    except Exception as e:
        print('Error')
        return e


@app.route('/')
def api_endpoints():
    return render_template('documentation.html')

@app.route('/recipe/<recipe>')
def recipe(recipe='None'):
    if int(recipe):
        print('What?')
        name = call_databse('SELECT * FROM Recipes ORDER BY RAND() LIMIT '+ recipe + ';')
        return jsonify(name)
    else:
        name = call_databse('SELECT * FROM Recipes WHERE Name LIKE "' + recipe + '";')
        return jsonify(name)

@app.route('/recipe/all')
def all_recipe():
    name = call_databse('SELECT * FROM Recipes;')
    return jsonify(name)


