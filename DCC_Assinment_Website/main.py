from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sql123'
app.config['MYSQL_DB'] = 'dccweb'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("web.html")

@app.route('/a_1', methods = ["POST", "GET"])
def a_1():
    if request.method == "POST":
        print("HI")
        print(request.method)
        print(request.form["box"])  

        print("TEST")

        cursor = mysql.connection.cursor()
        cursor.execute("sql query 1 %s)", (request.form["box"],))

        data = cursor.fetchone()

        cursor.close()

    return render_template("web.html", a_1_data = data) 


@app.route('/a_2', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("sql query 2 %s", (request.form["box"],))

        data = cursor.fetchall()

        cursor.close()
        
    return render_template("web.html", a_2_data = data) 


@app.route('/a_3', methods = ["POST", "GET"])
def a_3():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("sql query 2 %s));", (request.form["box"],))

        data = cursor.fetchall()

        cursor.close()
    
    if len(data) == 0:
        return render_template("index.html", a_3_data = [["Not Found !!!"]]) 

    return render_template("web.html", a_3_data = data) 

@app.route('/a_4', methods = ["POST", "GET"])
def a_4():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("sql query 4 %s", (request.form["box"],))

        data = cursor.fetchall()

        cursor.close()
    
    if len(data) == 0:
        return render_template("web.html", a_4_data = [["Not Found !!!"]]) 

    return render_template("web.html", a_4_data = data)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
