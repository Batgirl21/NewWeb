
from msilib.sequence import AdminUISequence

from flask import Flask, flash, redirect, render_template,request, jsonify, send_file, session, url_for
import sqlite3 as sql
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import sqlalchemy

from sqlalchemy.sql import func


from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.utils import secure_filename
from flask import current_app



app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     UserId = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(80), nullable=False)


    
#     self.UserId = UserId
#     self.password = password



# def connect_db():
#     conn = sql.connect('database.db')
#     conn.row_factory = sql.Row
#     return conn

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()

# def get_db():
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

# def close_db(error):
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

# @app.route('/aa')
# def index():
#     db = get_db()
#     cur = db.execute('SELECT * FROM table_name')
#     rows = cur.fetchall()

@app.route('/')
def hello_world():
    return render_template('index.html')

    try:
        cur = db.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        return f'Connected to database. Result of query: {result}'
    except Exception as e:
        return f'Error connecting to database: {e}'

@app.route('/admin')
def hello_admin():
    Property = [
        {'name': 'Property 1', 'description': 'Description of Property 1', 'price': 50000},
        {'name': 'Property 2', 'description': 'Description of Property 2', 'price': 45000},
        {'name': 'Property 3', 'description': 'Description of Property 3', 'price': 80000}
    ]
    return render_template('admin.html', Property=Property)



@app.route('/')
def product_list():
    Property = [
        {'name': 'Property 1', 'description': 'Description of Property 1', 'price': 50000},
        {'name': 'Property 2', 'description': 'Description of Property 2', 'price': 45000},
        {'name': 'Property 3', 'description': 'Description of Property 3', 'price': 80000}
    ]
    return render_template('admin.html', Property=Property)

#@app.route('/')
#def admin_log():
   #return render_template('admin.html', database = database.query.all())

# @app.route('/new', methods = ['GET', 'POST'])
# def new():
#    if not request.form['UserId'] or not request.form['password']:
#          flash('Please enter all the fields', 'error')
#    if request.method == 'POST':
#       database = database(request.form['UserId'], request.form['password'])

    #   db.session.add(admin)
     # db.session.commit()
@app.route('/login', methods = ['POST', 'GET'])
def login():
    Property = [
        {'name': 'Property 1', 'description': 'Description of Property 1', 'price': 50000},
        {'name': 'Property 2', 'description': 'Description of Property 2', 'price': 45000},
        {'name': 'Property 3', 'description': 'Description of Property 3', 'price': 80000}
    ]
    if request.method =='POST':
        email = request.form['email']
        password =  request.form['password']
        if(email == ""):
            return  render_template('index.html')
    with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("select * from admin where email=? and password=?",(email,password) )
         row = cur.fetchone()
         print (row)
         if (row == None):
            return  render_template('index.html', user = row)
         else:
            cur.execute("select * from property")
            Property = cur.fetchall()
            print(Property)
            con.commit()
            msg = "Record successfully added"
    
            return render_template("admin.html", Property=Property)
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reservationFormCustom',methods = ['POST', 'GET'])
def reservationFormCustom():
    if request.method =='POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
    with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO admin (firstName, lastName, email, phone, password) VALUES (?, ?, ?, ?, ?)", (firstName, lastName, email, phone, password))
         con.commit()
         msg = "Record successfully added"
    
    return render_template("index.html", msg=msg)
    con.close()
    
    
@app.route('/add_property', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # Do something with the data (e.g. store it in a database)
        with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO property (name, description, price) VALUES (?, ?, ?)", (name, description, price))
         cur.execute("select * from property")
         Property = cur.fetchall()
         print(Property)
         con.commit()
         msg = "Record successfully added"
    
    return render_template("admin.html", Property=Property)
        # Redirect to the properties page
        #return redirect('/properties')

    #return render_template('add_property.html')

@app.route('/properties')
def properties():
    # Get the properties from the database (or any other data source)
    properties = []

    return render_template('properties.html', properties=properties)


if __name__ == "__main__":
#   with app.app_context():
#    db.create_all() 

 app.run(port=5000, debug= True)

