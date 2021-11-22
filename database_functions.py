import sqlite3


def get_departments():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = []
    names = c.execute('SELECT name FROM Departments')
    for i in names.fetchall():
        lst.append(i[0])
    conn.commit()
    conn.close()
    return lst

def get_department_ids():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = []
    ids = c.execute('SELECT department_id FROM Departments')
    for i in ids.fetchall():
        lst.append(i[0])
    conn.commit()
    conn.close()
    return lst

def get_hiring_requirements(dep_var):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    get_dep_id = c.execute(("SELECT department_id FROM Departments WHERE name=?"), (dep_var.get(),))
    dep_id = get_dep_id.fetchone()[0]
    get_emp_count = c.execute(("SELECT employee_count FROM Departments WHERE department_id=?"), (dep_id,))
    emp_count = get_emp_count.fetchone()[0]
    get_min_emp = c.execute(("SELECT min_employee FROM Departments WHERE department_id=?"), (dep_id,))
    min_emp = get_min_emp.fetchone()[0]

    conn.commit()
    conn.close()

    return emp_count, min_emp

def edit_employee_count(action, dep_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    emp_count = c.execute(("SELECT employee_count FROM Departments WHERE department_id=?"), (dep_id,)).fetchone()[0]
    if action == 'decrease':
        emp_count -= 1
    if action == 'increase':
        emp_count += 1

    c.execute(("UPDATE Departments SET employee_count=? WHERE department_id=?"), (emp_count, dep_id))
    conn.commit()
    conn.close()

def edit_employee_info(employe_type, id, address_id, f_name, l_name, phone, email, street, city, country, zipcode,
                       department_id, birth, hired):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute((f"UPDATE {employe_type+'s'} SET first_name=?, last_name=?, department=?, phone_number=?, email=?, birth_date=?,"
               f" date_hired=? WHERE {employe_type.lower()}_id=?"), (f_name, l_name, department_id, phone, email,
                                                                         birth, hired ,id))
    c.execute(("UPDATE Addresses SET street_address=?, city=?, country=?, zipcode=? WHERE"
               " address_id=?"), (street, city, country, zipcode, address_id))

    conn.commit()
    conn.close()

def edit_salary(emp_id, salary):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(("UPDATE Employees SET monthly_salary=? WHERE employee_id=?"), (salary, emp_id))
    conn.commit()
    conn.close()

def add_employee(insert, data_tuple):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(insert, data_tuple)
    conn.commit()
    conn.close()

def get_emplist_employee_info():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    emp_list = c.execute("SELECT Employees.employee_id, Employees.first_name, Employees.last_name, Addresses.city, "
                         "Addresses.street_address, Employees.phone_number, Employees.email, Employees.birth_date, "
                         "Departments.name FROM Employees JOIN Addresses ON Employees.address = Addresses.address_id"
                         " JOIN Departments ON Employees.department = Departments.department_id").fetchall()
    conn.commit()
    conn.close()
    return emp_list

def get_employees_names():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    full_names = []
    counter = 0

    first_names = c.execute('SELECT first_name FROM Employees')
    for i in first_names.fetchall():
        full_names.append(i[0])

    last_names = c.execute('SELECT last_name FROM Employees')
    for j in last_names.fetchall():
        full_names[counter] += f" {j[0]}"
        counter += 1

    conn.commit()
    conn.close()
    return full_names

def get_employee_ids():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = []
    ids = c.execute('SELECT employee_id FROM Employees')
    for i in ids.fetchall():
        lst.append(i[0])
    conn.commit()
    conn.close()
    return lst

def get_bonus(emp_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    bonus = c.execute(('SELECT bonus FROM Employees where employee_id=?'), (emp_id,)).fetchone()[0]

    conn.commit()
    conn.close()
    return bonus

def get_emplist_manager_info():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    mang_list = c.execute("SELECT Managers.manager_id, Managers.first_name, Managers.last_name, Addresses.city, "
                          "Addresses.street_address, Managers.phone_number, Managers.email, Managers.birth_date, "
                          "Departments.name FROM Managers JOIN Addresses ON Managers.address = Addresses.address_id "
                          "JOIN Departments ON Managers.department = Departments.department_id").fetchall()
    conn.commit()
    conn.close()
    return mang_list

def get_manager_names():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    full_names = []
    counter = 0

    first_names = c.execute('SELECT first_name FROM Managers')
    for i in first_names.fetchall():
        full_names.append(i[0])

    last_names = c.execute('SELECT last_name FROM Managers')
    for j in last_names.fetchall():
        full_names[counter] += f" {j[0]}"
        counter += 1

    conn.commit()
    conn.close()
    return full_names

def get_manager_ids():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = []
    ids = c.execute('SELECT manager_id FROM Managers')
    for i in ids.fetchall():
        lst.append(i[0])
    conn.commit()
    conn.close()
    return lst

def get_employee_bdays(type):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lst = []
    bdays = c.execute(f'SELECT birth_date FROM {type}')
    for i in bdays.fetchall():
        lst.append(i[0])
    conn.commit()
    conn.close()
    return lst

def get_employment_date(emp_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    date = c.execute(('SELECT date_hired FROM Employees where employee_id=?'), (emp_id,)).fetchone()[0]

    conn.commit()
    conn.close()
    return date

def add_bonus(emp_id, bonus):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    bns = c.execute(("SELECT bonus FROM Employees WHERE employee_id=?"), (emp_id,)).fetchone()[0]
    bns += bonus
    c.execute(("UPDATE Employees SET bonus=? WHERE employee_id=?"), (bns, emp_id))

    conn.commit()
    conn.close()

def count_employees(type):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    count = c.execute(f"SELECT COUNT(*) from {type}").fetchone()[0]
    conn.commit()
    conn.close()
    return count

def get_department_name(emp_id, type):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    e_dep_id = c.execute((f"SELECT department FROM {type+'s'} WHERE {type.lower()}_id=?"), (emp_id,)).fetchone()[0]
    e_dep_name = c.execute(("SELECT name FROM Departments WHERE department_id=?"), (e_dep_id,)).fetchone()[0]
    conn.commit()
    conn.close()
    return e_dep_name

def get_department_id(emp_id, type):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    dep_id = c.execute((f"SELECT department FROM {type+'s'} WHERE {type.lower()}_id=?"), (emp_id,)).fetchone()[0]
    conn.commit()
    conn.close()
    return dep_id

def delete_employee(emp_id, type):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    address_id = c.execute((f"SELECT address FROM {type+'s'} WHERE {type.lower()}_id=?"), (emp_id,)).fetchone()[0]
    c.execute((f"DELETE FROM {type+'s'} WHERE {type.lower()}_id=?"), (emp_id,))
    c.execute((f"DELETE FROM Addresses WHERE address_id=?"), (address_id,))
    conn.commit()
    conn.close()

def delete_all_entries():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Employees")
    c.execute("DELETE FROM Managers")
    c.execute("DELETE FROM Addresses")
    c.execute("DELETE FROM Departments")
    c.execute("DELETE FROM sqlite_sequence WHERE name = 'Employees'")
    c.execute("DELETE FROM sqlite_sequence WHERE name = 'Managers'")
    c.execute("DELETE FROM sqlite_sequence WHERE name = 'Addresses'")
    c.execute("DELETE FROM sqlite_sequence WHERE name = 'Departments'")
    conn.commit()
    conn.close()


def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE Addresses ( 
            address_id integer primary key autoincrement not null unique, 
            street_address text not null,
            country text not null,
            city text not null,
            zipcode text not null
            )""")

    c.execute("""CREATE TABLE Employees (
            employee_id integer primary key autoincrement not null unique,
            first_name text not null,
            last_name text not null,
            department integer,
            address integer not null,
            phone_number text not null,
            email text not null,
            birth_date text not null,
            monthly_salary real,
            date_hired text not null,
            bonus integer default 0
            )""")

    c.execute("""CREATE TABLE Managers (
            manager_id integer primary key autoincrement not null unique,
            first_name text not null,
            last_name text not null,
            department integer,
            address integer not null,
            phone_number text not null,
            email text not null,
            birth_date text not null,
            monthly_salary real,
            date_hired text not null
            )""")

    c.execute("""CREATE TABLE Departments (
            department_id integer primary key autoincrement not null unique,
            name text not null,
            employee_count integer default 0,
            min_employee integer not null
            )""")

    conn.commit()
    conn.close()