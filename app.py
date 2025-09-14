from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient

client = MongoClient("dbconnect")

db = client['sih']
ld = db['login_details']

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('login.html', message=None)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = ld.find_one({"email":email, "password":password})

    if user:
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", message="❌ Invalid email or password. Try again.")
    
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__=='__main__':
    app.run(debug=True)
