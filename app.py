from flask import Flask, render_template, request, session, redirect
import sqlite3 

# Define the database file name
DATABASE = 'Basic_DB.db'

app = Flask(__name__)
app.secret_key = "secret_key"

# DUMMY DB
users = {"user1": "password1", "user2": "password2"}

@app.route("/")
def Creation():
    return render_template("index.html")

# Define the route for the products page
@app.route("/item")
def item():
    # Open a connection to the database
    with sqlite3.connect(DATABASE) as conn:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute an SQL statement to retrieve all products from the products table
        cursor.execute("SELECT *  FROM Products WHERE product_id = 1")
        # Fetch all rows returned by the SQL query
        products = cursor.fetchall()
        # Render the index.html template, passing in the list of prodcuts as a varibable called 'products'
        prod_name=products[0][1]
        price = products[0][3]
        desc = products[0][2]
    return render_template("item.html" , prod_name=prod_name, desc = desc, price = price)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["username"] = username
            return redirect("/")
        else:
            return "Invalid username or password"
    else:
        if "username" in session:
            return redirect("/test")
        else:
            return render_template("login2.html")

# Home route
@app.route("/test")
def home():
    if "username" in session:
        return "Hello, " + session["username"]
    else:
        return redirect("/login")

# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



