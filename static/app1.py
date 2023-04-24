from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_items():
    # Connect to the database
    conn = sqlite3.connect('Basic_DB.db')
    cursor = conn.cursor()
    
    # Query all items from the database
    cursor.execute('SELECT * FROM products')
    items = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Pass the items data to the HTML file for rendering
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run()
