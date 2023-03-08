import sqlite3

# Define the database file name
DATABASE = "Basic_DB.db"

with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT *  FROM Products")
    cursor.execute("SELECT *  FROM Products WHERE product_id = 1")
    products = cursor.fetchall()
    print(products)