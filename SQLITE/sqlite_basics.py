import sqlite3


def create_table():
    connection = sqlite3.connect('mydatabase1.db')
    print("Opened database successfully")

    connection.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        VARCHAR(50),
             SALARY         REAL)''')
    print("Table created successfully")

    connection.close()


def insert():
    connection = sqlite3.connect('mydatabase1.db')
    print("Database open successfully")

    connection.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, ADDRESS, SALARY) VALUES "
                       "(101, 'MUZAKKIR', 23, 'MAHBUBNAGAR', 20000.0)")
    connection.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, ADDRESS, SALARY) VALUES "
                       "(102, 'MUZAFFAR', 22, 'HYDERABAD', 30000.0)")
    connection.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, ADDRESS, SALARY) VALUES "
                       "(103, 'ZAMEER', 21, 'RR', 31000.0)")

    connection.commit()
    print('Record inserted successfully')
    connection.close()


def display():
    connection = sqlite3.connect('mydatabase1.db')
    cursor = connection.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY FROM EMPLOYEE")

    for row in cursor:
        print("|------------------------|")
        print('| ID      :', row[0])
        print('| NAME    :', row[1])
        print('| AGE     :', row[2])
        print('| ADDRESS :', row[3])
        print('| SALARY  :', row[4], )
        print("|------------------------|", '\n')


def update():
    connection = sqlite3.connect('mydatabase1.db')
    connection.execute("UPDATE EMPLOYEE SET SALARY = 23000.0 WHERE ID = 101")
    connection.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY) VALUES "
                       "(104, 'FAISAL', 25, 'KARNOOL', 40000.0)")
    connection.commit()
    display()
    print("Total number of rows updated : ", connection.total_changes)


# update()


def delete():
    connection = sqlite3.connect('mydatabase1.db')
    connection.execute("DELETE FROM EMPLOYEE WHERE ID = 104")

    connection.commit()
    display()
    print("Total number of rows updated : ", connection.total_changes)


# create_table()
#insert()
#update()
delete()
