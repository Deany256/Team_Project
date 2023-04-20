import sqlite3

# Define the database file name
DATABASE = "ecommerce.db"

with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch the results as a list of tuples
    table_names = [row[0] for row in cursor.fetchall()]

    # Print the table names
    for i in range(len(table_names)):
        print(f"{i}: {table_names[i]}")
        
    choice = int(input("Which table would you like to work on: "))
    
    match choice:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        
    