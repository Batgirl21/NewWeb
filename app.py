from flask import Flask, redirect, render_template,request, jsonify, send_file, session, url_for



from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.utils import secure_filename

import io



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(port=5000, debug= True)