from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="mydb"
   )

@app.route('/')
def index():
       return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
       name = request.form['name']
       email = request.form['email']
       cursor = db.cursor()
       cursor.execute("INSERT INTO form_data (name, email) VALUES (%s, %s)", (name, email))
       db.commit()
       return redirect('/')

if __name__ == '__main__':
       app.run(debug=True)