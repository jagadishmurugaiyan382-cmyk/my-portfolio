from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/index1')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            return "Login Successful 🔐"

        else:
            return "Invalid Login"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)