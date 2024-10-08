from flask import Flask, render_template, request, session, redirect, jsonify
import hashlib
import sqlite3 



# Define the database file name
DATABASE = "ecommerce.db"

app = Flask(__name__, static_url_path='/static')
app.secret_key = "secret_key"


@app.route("/")
def loadHomepage():
    if "username" in session:
        return render_template("index.html", name = session["username"])
    else:
        return render_template("index.html", name= "signin/signup")

# Define the route for the products page
@app.route("/item", methods = ["GET" , "post"])
def item():
    # Open a connection to the database
    with sqlite3.connect(DATABASE) as conn:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute an SQL statement to retrieve all products from the products table
        cursor.execute("SELECT *  FROM Products")
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
            items = products
            return render_template("items.html" , items = items)

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
        if request.form.get("login"):
            name = request.form["username"]
            password = request.form["password"].encode("utf-8")
            password = hashlib.sha256(password).hexdigest()
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE name = ?", (name,))
                result = cursor.fetchone()
                if result is not None:
                    stored_hashed_password = result[4]

                    if password == stored_hashed_password:
                    # if bcrypt.checkpw(password, stored_hashed_password):
                        session["username"] = name
                        return redirect("/")
                    else:
                        return "Invalid username or password"
                else:
                    return "Invalid username or password"
    else:
        if "username" in session:
            return redirect("/")
        else:
            return render_template("login_and_signup.html")
        
        
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        if request.form.get("signup"):
            name = request.form["name"]
            username = request.form["new_username"]
            password = request.form["new_password"].encode("utf-8")
            # hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashlib.sha256(password).hexdigest()
            email = request.form["email"]
            shipping_address = request.form["postal_address"]

            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE name = ?", (username,))
                result = cursor.fetchone()
                if result is not None:
                    return "Username already exists, please choose a different username."
                else:
                    cursor.execute("INSERT into Customers (name, username, email, password_hash, shipping_address) VALUES (?, ?, ?, ?, ?)", (name, username, email, hashed_password,shipping_address))
                    session["username"] = username
                    return render_template("index.html")
    else:
        if "username" in session:
            return redirect("/index")
        else:
            return render_template("login_and_signup.html")

# Home route
@app.route("/home")
def home():
    if "username" in session:
        # return "Hello, " + session["username"]
        return render_template("home.html", username = session["username"])
    else:
        return redirect("/login_or_signup")

# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

@app.route("/login_or_signup")
def hide():
    return render_template("login_and_signup.html")

@app.route("/banner")
def banner():
    return render_template("banner.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/add_to_cart")
def add_to_cart():
    # data = request.get_json()
    # itemid = data.get('itemId')
    
    username = session['username']
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id FROM Customers WHERE username = ?", (username,))
        customerID = cursor.fetchone()
        
        Customer = customerID
        itemid = itemid
        if Quantity == 0:
            Quantity = 1
        else:
            Quantity= Quantity
        
        # Check if the row with the customer_id and product_id exists in the table
        cursor.execute("SELECT COUNT(*) FROM cart WHERE customer_id = ? AND product_id = ?", (Customer, itemid,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Present :)")
            # Lower value in the stock column
            cursor.execute("UPDATE products SET stock = stock - ? WHERE product_id = ?", (Quantity, itemid,))
            # update item count in cart table
            cursor.execute("UPDATE cart SET quantity = quantity + ? WHERE customer_id = ? AND product_id = ?", (Quantity, Customer, itemid,))
        else:
            # Lower value in the stock column
            cursor.execute("UPDATE products SET stock = stock - ? WHERE product_id = ?", (Quantity, itemid,))
            # Insert Item to cart
            cursor.execute("INSERT INTO cart (customer_id,product_id,quantity) VALUES (?,?,?)", (Customer, itemid, Quantity,))
            print("not present :(")
            
        conn.commit()
    
    
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT stock FROM Products WHERE product_id = ?", (itemid,))
        result = cursor.fetchone()
        quantity = 1
        if result == None:
            return "Error"
        stock = result[0]
        
        if stock>0:
            cursor.execute("UPDATE Products SET stock = stock - 1 WHERE product_id = ?", (itemid,))
            cursor.execute("INSERT INTO Cart (product_id,quantity) VALUES (?,?)", (itemid,quantity))
            conn.commit()
            return "Item Added to cart"
        else:
            return "Item Out of stock"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




