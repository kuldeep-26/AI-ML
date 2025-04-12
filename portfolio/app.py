from flask import Flask,render_template,url_for,request
import sqlite3
conn = sqlite3.connect("usercontact.db")
app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug = True)