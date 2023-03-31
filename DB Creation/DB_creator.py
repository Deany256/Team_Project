import sqlite3

# Define the database file name
DATABASE = "ecommerce.db"

# Closes the Database
def close_DB():
    with sqlite3.connect(DATABASE) as conn:
        conn.close()

# Define the function to create the Products table
def create_products_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                short_description TEXT,
                long_description TEXT,
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
        
# Define the function to create the Orders table
def create_orders_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                FOREIGN KEY (product_id) REFERENCES Products (product_id)
            );
        """)

# Define the function to create the Cart table
def create_cart_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cart (
                cart_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                FOREIGN KEY (product_id) REFERENCES Products (product_id)
            );
        """)

# Define the function to create the Shipping table
def create_shipping_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Shipping (
                shipping_id INTEGER PRIMARY KEY,
                carrier TEXT,
                cost REAL,
                delivery_time TEXT
            );
        """)

# Define the function to create the Payment table
def create_payment_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payment (
                payment_id INTEGER PRIMARY KEY,
                method TEXT,
                details TEXT
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

create_products_table()
create_customers_table()
create_orders_table()
create_cart_table()
create_shipping_table()
create_payment_table()
create_reviews_table()
# close_DB()
# fill_products_table()