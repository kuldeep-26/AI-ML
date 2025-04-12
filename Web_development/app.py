from flask import Flask,render_template,url_for,request
import sqlite3
conn = sqlite3.connect("userdata.db")
app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/about')    # http://127.0.0.1:5000/about
def about():
    return render_template('about.html') 

@app.route('/service')    # http://127.0.0.1:5000/service
def service():
    return render_template('service.html') 

@app.route('/contact')    # http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html') 

@app.route('/query')      # http://127.0.0.1:5000/query
def query():
    return render_template('query.html')

@app.route('/user_query',methods = ['GET','POST'])
def user_query():
    if request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        name = request.form['name']
        age = int(request.form['age'])
        address = request.form['address']
        college = request.form['college']
        branch = request.form['branch']
        roll_no = int(request.form['roll_no'])
        query_sub = request.form['query_sub']

        user_data = (name,age,address,college,branch,roll_no,query_sub)

        insert_data_query = """
        insert into userrecord values(?,?,?,?,?,?,?)
        """

        cur = conn.cursor()
        cur.execute(insert_data_query,user_data)
        print("you have successfully inserted your data into table: ",user_data)
        conn.commit()
        cur.close()
        conn.close()

        return "Your data is successfully inserted into the database !"

if __name__ == "__main__":
    app.run(debug = True)