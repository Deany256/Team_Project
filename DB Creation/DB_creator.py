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
                brand TEXT,
                category TEXT,
                stock INTEGER,
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
                email TEXT UNIQUE,
                password_hash TEXT,
                shipping_address TEXT,
                shipping_postcode TEXT,
                cart_total REAL NOT NULL DEFAULT 0
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
                order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                total_price REAL,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
            );
        """)
        
# Define the function to create the Orders table
def create_order_details_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Order_Details (
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                PRIMARY KEY (product_id,order_id),
                FOREIGN KEY (product_id) REFERENCES Products (product_id)
                FOREIGN KEY (order_id) REFERENCES Orders (order_id)
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
                order_id INTEGER,
                carrier TEXT,
                cost REAL,
                delivery_type TEXT,
                FOREIGN KEY (order_id) REFERENCES Orders (order_id)
            );
        """)

# Define the function to create the Payment table
# def create_payment_table():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Payment (
#                 payment_id INTEGER PRIMARY KEY,
#                 method TEXT,
#                 details TEXT
#             );
#         """)
        
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
        #   (product_name, short_description, long_description, brand, category, stock, price)
            ("Framework 13", "13 inch Laptop by Framework.", "LONG Description", "Framework", "Laptop", 15, 799.99),
            ("Nvidia RTX 4070", "Nvidia RTX 4070 FE GPU.", "Long DEScription", "Nvidia", "GPU", 5, 499.99),
            ("Corsair 16GB DDR4 RAM", "Corsair LPX 2x8GB 3200MHz DDR4 RAM Kit.", "Long Description", "Corsair", "RAM", 6, 39.99),
            ("Crucial 16GB DDR4 RAM", "Crucial Ballistix 2x8GB 3200MHz DDR4 RAM Kit.", "Long Description", "Crucial", "RAM", 12, 39.99),
            ("AMD Ryzen 5 5600X", "AMD Ryzen 5 5600X 6-Core CPU.", "Long Description", "AMD", "CPU", 5, 149.99),
        ]
        cursor.executemany("""
            INSERT INTO Products (product_name, short_description, long_description, brand, category, stock, price)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, products)
        conn.commit()
        
def fill_customers_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        customers = [
        #   (name, email, password_hash, shipping_address, shipping_postcode, cart_total)
            ("George", "George@email.com", "password123", "shipping_address", "shipping_postcode", 0),
            ("Archie", "Archie@email.com", "password_hash123", "shipping_address", "shipping_postcode", 0),
            ("McDonald", "McDonald@email.com", "password_hashing", "shipping_address", "shipping_postcode", 0),
        ]
        cursor.executemany("""
            INSERT INTO Customers (name, email, password_hash, shipping_address, shipping_postcode, cart_total)
            VALUES (?, ?, ?, ?, ?, ?);
            """, customers)
        conn.commit()

def fill_orders_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        orders = [
        #   (customer_id, total_price)
            (1, 799.99),
            (2, 499.99),
            (1, 149.99),
        ]
        cursor.executemany("""
            INSERT INTO Orders (customer_id, total_price)
            VALUES (?, ?);
            """, orders)
        conn.commit()
        
def fill_order_details_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        order_details = [
        #   (order_id, product_id, quantity)
            (1, 1, 1),
            (2, 2, 1),
            (3, 5, 1),
        ]
        cursor.executemany("""
            INSERT INTO Order_Details (order_id, product_id, quantity)
            VALUES (?, ?, ?);
            """, order_details)
        conn.commit()

# create_products_table()
# create_customers_table()
# create_orders_table()
# create_order_details_table()
# create_cart_table()
# create_shipping_table()
# create_reviews_table()

# create_payment_table()
# close_DB()

# fill_products_table()
# fill_customers_table()
# fill_orders_table()
fill_order_details_table()