from flask import Flask, render_template, request, session, redirect
import bcrypt
import sqlite3 

# Define the database file name
DATABASE = 'Basic_DB.db'

app = Flask(__name__, static_url_path='/static')
app.secret_key = "secret_key"

# DUMMY DB
users = {"user1": "password1", "user2": "password2"}

@app.route("/")
def loadHomepage():
    return render_template("index.html")

# Define the route for the products page
@app.route("/item", methods = ["GET" , "post"])
def item():
    # Open a connection to the database
    with sqlite3.connect(DATABASE) as conn:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute an SQL statement to retrieve all products from the products table
        cursor.execute("SELECT *  FROM Products WHERE product_id")
        # Fetch all rows returned by the SQL query
        products = cursor.fetchall()
        # updated item route to allow the user to add an item to their basket
        if request.method == "POST":
            if "basket" not in session:
                session["basket"] = []
            session["basket"].append(products)
            return redirect("/basket")
        else:
        # Render the index.html template, passing in the list of prodcuts as a varibable called 'products'
            prod_name=products[0][1]
            price = products[0][3]
            desc = products[0][2]
            return render_template("item.html" , prod_name=prod_name, desc = desc, price = price)

# Add a new route for shopping basket which will display items in the basket
@app.route("/basket" , methods = ["GET" , "POST"])
def basket():
    if "basket" in session:
        basket_items = session["basket"]
    else:
        basket_items = []
#allows user to delete items from basket 
    if request.method == "POST":
        item_index =int(request.form[item_index])
        del session["basket"][item_index]
        return redirect("/basket")
    else:
        return render_template("basket.html" , basket_items = basket_items)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("new_account"):
            name = request.form["new_username"]
            password = request.form["new_password"].encode("utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            email = request.form["email"]
            shipping_address = request.form["postal_address"]

            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE name = ?", (name,))
                result = cursor.fetchone()
                if result is not None:
                    return "Username already exists, please choose a different username."

                cursor.execute("INSERT INTO Customers (name, password_hash, email, shipping_address) VALUES (?, ?, ?, ?)", (name, hashed_password, email, shipping_address))
                conn.commit()
                session["username"] = name
                return redirect("/")
        else:
            name = request.form["username"]
            password = request.form["password"].encode("utf-8")

            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE name = ?", (name,))
                result = cursor.fetchone()
                if result is not None:
                    stored_hashed_password = result[2].encode("utf-8") 
                    if bcrypt.checkpw(password, stored_hashed_password):
                        session["username"] = name
                        return redirect("/")
                    else:
                        return "Invalid username or password"
                else:
                    return "Invalid username or password"
    else:
        if "username" in session:
            return redirect("/test")
        else:
            return render_template("login.html")

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
    return redirect("/")

@app.route("/hide")
def hide():
    return render_template("hide.html")

@app.route("/banner")
def banner():
    return render_template("banner.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



