from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Harshitji@1',
    port=3306
)

if db.is_connected():
    print("Connected to MySQL!")

@app.route("/")
def home():
    return "Flask is working properly buddy!"

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)