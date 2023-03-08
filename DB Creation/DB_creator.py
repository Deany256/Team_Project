import sqlite3

# Define the database file name
DATABASE = "Basic_DB.db"

# Define the function to create the Products table
def create_products_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                description TEXT,
                price REAL,
                image_url TEXT
            );
        """)

# Define the function to create the Customers table
def create_customers_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                shipping_address TEXT,
                payment_info TEXT
            );
        """)
        
# Define the function to create the Reviews table
def create_reviews_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reviews (
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_id INTEGER,
                rating INTEGER,
                text TEXT,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                FOREIGN KEY (product_id) REFERENCES Products (product_id)
            );
        """)

def fill_products_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        products = [
            ("Laptop", "This is the description for generic laptop.", 799.99),
            ("GPU", "This is the description for generic GPU.", 299.99),
            ("RAM", "This is the description for generic RAM.", 39.99),
        ]
        cursor.executemany("""
            INSERT INTO Products (product_name, description, price)
            VALUES (?, ?, ?);
            """, products)
        conn.commit()

create_customers_table()
create_products_table()
create_reviews_table()
fill_products_table()