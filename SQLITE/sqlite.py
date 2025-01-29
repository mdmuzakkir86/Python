import sqlite3


# establishing connection with SQLite3
con = sqlite3.connect('mydatabase1.db')
cursorobj = con.cursor()

# creating table
cursorobj.execute('CREATE TABLE IF NOT EXISTS EMPLOYEE('
                  'NAME TEXT, '
                  'AGE INT, '
                  'ADDRESS CHAR(50), '
                  'SALARY REAL);')

name = input("Enter name: ")
age = input('Enter age: ')
address = input('Enter address: ')
salary = input('Salary: ')

# Inserting values to db
cursorobj.execute("INSERT INTO EMPLOYEE(NAME, AGE, ADDRESS, SALARY) "
                  "VALUES ('"+name+"', "+age+", '"+address+"', "+salary+");")

# Updating values of EMPLOYEE TABLE
# cursorobj.execute("UPDATE EMPLOYEE set SALARY = 40000 WHERE NAME = 'MD MUZAKKIR'")

# Save the changes to database
con.commit()

# Fetching data from Employee table
data = cursorobj.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print('NAME    = ', row[0])
    print('Age     = ', row[1])
    print('Address = ', row[2])
    print('Salary  = ', row[3])
    print('----------------------')

con.close()
