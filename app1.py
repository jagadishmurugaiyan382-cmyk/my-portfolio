from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "jagadeesh" and password == "1234":
            return "Login Successful"

        else:
            return "Invalid Login"

    return render_template("login.html")

if __name__ == "_main_":
    app.run(debug=True)