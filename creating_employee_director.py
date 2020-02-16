import sqlite3


# connecting to the db file directly will throw an error if you attempt to overwrite
conn = sqlite3.connect('employee3.db')

# connecting to memory will make a new table each time you run the code
#conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employees(first text, last text, pay integer)")
ß
conn.commit()


# create a class to add employees to database
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

# create functions for inserting, searching, updating and removing data
def insert_emp(emp):
    with conn: # this method is used so closing the connection is not necessary each time
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {"first":emp.first,"last":emp.last, "pay":emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last",
              {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
        {'first':emp.first, 'last':emp.last, 'pay':pay})


def remove_emp(emp):
    c.execute("DELETE from employees WHERE first = :first AND last = :last",
              {'first': emp.first, 'last': emp.last})

# create employees
emp_1 = Employee('Tim', 'Anderson', 60000)
emp_2 = Employee('Diedra', 'Henderson', 70000)
emp_3 = Employee('Zoey', 'Banderson', 80000)
emp_4 = Employee('Brian', 'Granderson', 90000)
emp_5 = Employee('Leslie', 'Anderson', 91000)
emp_6 = Employee('Jainey', 'Doe', 92000)
emp_7 = Employee('Hallie', 'Doe', 93000)

'''
# insert employees
insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)
insert_emp(emp_5)
insert_emp(emp_6)
insert_emp(emp_7)
'''

update_pay(emp_1, 100000)
remove_emp(emp_5)

emps = get_emps_by_name("Anderson")
print(emps)


conn.close()

# fetch functions:
# fetchall will return all results from the above query
# fetchone will return only the first result
# fetchmany will take in a number as an arguement and return as many as you wish

