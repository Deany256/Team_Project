from flask import Flask, render_template
import sqlite3 

# Define the database file name
DATABASE = 'Basic_DB.db'

app = Flask(__name__)

# Define the route for the products page
@app.route("/products")
def item():
    # Open a connection to the database
    with sqlite3.connect(DATABASE) as conn:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Execute an SQL statement to retrieve all products from the products table
        cursor.execute("SELECT *  FROM Products")
        # Fetch all rows returned by the SQL query
        products = cursor.fetchall()
        # Render the index.html template, passing in the list of prodcuts as a varibable called 'products'
    return render_template("item.html" , products=products)





