import sqlite3

try:
    db_connection = sqlite3.connect('mydatabase.db')
    cursor_obj = db_connection.cursor()
    cursor_obj.execute('''CREATE TABLE IF NOT EXISTS PRODUCTS(ITEM_NAME TEXT, PRICE REAL)''')
    item_name = input('Enter item name:')
    price = input("Enter item price")
    cursor_obj.execute("INSERT INTO PRODUCTS(ITEM_NAME, PRICE) VALUES ('"+item_name+"', "+price+")")

    db_connection.commit()
    cursor_obj.close()
except sqlite3.Error as error:
    print("Error")
finally:
    if db_connection:
        db_connection.close()