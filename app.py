from flask import Flask, render_template
import sqlite3 

# Define the database file name
DATABASE = 'Basic_DB.db'

app = Flask(__name__)

# Define the route for the products page
@app.route("/")
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
        # conn.close()
        prod_name=products[0][1]
        price = products[0][3]
        desc = products[0][2]
    return render_template("item.html" , prod_name=prod_name, desc = desc, price = price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



