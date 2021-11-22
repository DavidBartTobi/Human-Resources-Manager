from tkinter import messagebox, ttk
from tkinter import *
from tkcalendar import Calendar
from datetime import date
import sqlite3

import gui, database_functions

def update_employee(employee_type):
    def edit():
        def complete_edit():
            previous_dep_id = database_functions.get_department_id(emp_id,employee_type)
            dep_id=1
            for i in department_options:
                if i == department_var.get():
                    index = department_options.index(i)
                    dep_id = department_ids[index]
                    break

            if previous_dep_id != dep_id:
                database_functions.edit_employee_count('decrease', previous_dep_id)
                database_functions.edit_employee_count('increase', dep_id)

            if check_empty_fields_error(f_name.get(), l_name.get(), phone.get()) is False:
                edit_top.lift()
                return

            if check_numeric_fields_error(phone.get(), "Phone number") is False:
                edit_top.lift()
                return

            database_functions.edit_employee_info(employee_type, emp_id, loaded_data[0][3], f_name.get(), l_name.get(), phone.get(), email.get(),
                                                  street.get(), city.get(), country.get(), zipcode.get(), dep_id, birth.get(), hired.get())


            messagebox.showinfo("Confirmation", f"{employee_type} Details Updated")
            edit_top.lift()


        select_top.destroy()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        emp_id = 1
        for i in id_list:
            if f"No.: {i})" in employee_var.get():
                emp_id = i
                break
        loaded_data = c.execute(
            (f"SELECT * FROM {employee_type_plural} JOIN Addresses ON {employee_type_plural}.address ="
             f" Addresses.address_id WHERE {employee_type.lower()}_id=?"),
            (emp_id,)).fetchall()
        conn.commit()
        conn.close()

        edit_top = Toplevel()
        gui.Window(edit_top, f"Add {employee_type}", "510x370")

        background_label = Label(edit_top, bg=gui.Background_Color())

        first_label = Label(edit_top, text="First Name", anchor=W, width=13, bg=gui.Background_Color())
        last_label = Label(edit_top, text="Last Name", anchor=W, width=13, bg=gui.Background_Color())

        phone_label = Label(edit_top, text="Phone Number", anchor=W, width=13, bg=gui.Background_Color())
        email_label = Label(edit_top, text="E-mail Address", anchor=W, width=13, bg=gui.Background_Color())

        street_label = Label(edit_top, text="Street Address", anchor=W, width=13, bg=gui.Background_Color())
        city_label = Label(edit_top, text="City", anchor=W, width=13, bg=gui.Background_Color())

        country_label = Label(edit_top, text="Country", anchor=W, width=13, bg=gui.Background_Color())
        zip_label = Label(edit_top, text="Zipcode", anchor=W, width=13, bg=gui.Background_Color())

        salary_label = Label(edit_top, text="Monthly Salary", anchor=W, width=13, bg=gui.Background_Color())
        department_label = Label(edit_top, text="Department", anchor=W, width=13, bg=gui.Background_Color())

        birth_label = Label(edit_top, text="Birth Date", anchor=W, width=13, bg=gui.Background_Color())
        hired_label = Label(edit_top, text="Date Hired", anchor=W, width=13, bg=gui.Background_Color())

        f_name = ttk.Entry(edit_top, width=20)
        l_name = ttk.Entry(edit_top, width=20)

        phone = ttk.Entry(edit_top, width=20)
        email = ttk.Entry(edit_top, width=20)

        street = ttk.Entry(edit_top, width=20)
        city = ttk.Entry(edit_top, width=20)
        country = ttk.Entry(edit_top, width=20)
        zipcode = ttk.Entry(edit_top, width=20)

        salary = ttk.Entry(edit_top, width=20, state=DISABLED)

        previous_dep_id = loaded_data[0][3]
        department_options = database_functions.get_departments()
        department_ids = database_functions.get_department_ids()
        department_var = StringVar()
        department_var.set(department_options[previous_dep_id-1])
        department = ttk.OptionMenu(edit_top, department_var, None, *department_options)
        department.configure(width=15)

        birth = ttk.Entry(edit_top, width=20)
        hired = ttk.Entry(edit_top, width=20)

        birth_calendar = ttk.Button(edit_top, text='Calendar', command=lambda: calendar_popup(birth, edit_top), cursor='hand2')
        hired_calendar = ttk.Button(edit_top, text='Calendar', command=lambda: calendar_popup(hired, edit_top), cursor='hand2')
        finish_button = ttk.Button(edit_top, text="          EDIT", command=complete_edit, width=15, cursor='hand2')

        upload_loaded_data(loaded_data, f_name, l_name, phone, email, street, city, country, zipcode,
                           birth, hired)

        gui.activate_grid(background_label, first_label, last_label, phone_label, email_label,
                          street_label, city_label, country_label, zip_label, salary_label,
                          department_label, birth_label, hired_label, f_name, l_name,
                          phone, email, street, city, country, zipcode, salary,
                          department, birth, hired, birth_calendar, hired_calendar,
                          finish_button)



    def enter_password():
        def confirm_password():
            if password.get() == '1234':
                pw_top.destroy()

                dep_id = database_functions.get_department_id(emp_id, employee_type)
                database_functions.delete_employee(emp_id, employee_type)
                database_functions.edit_employee_count('decrease', dep_id)
                messagebox.showinfo("Confirmation", f"{employee_type} Deleted")
            else:
                messagebox.showerror("Error", "Incorrect Password")
                pw_top.lift()
                password.focus_force()
                pw_top.bind('<Return>', lambda func: confirm_password())

        select_top.destroy()

        emp_id = 1
        for i in id_list:
            if f"No.: {i})" in employee_var.get():
                emp_id = i
                break

        pw_top = Toplevel()
        gui.Window(pw_top, "Enter Password", "225x115")

        background_pw_label = Label(pw_top, bg=gui.Background_Color())
        background_pw_label.grid(row=0, column=0, rowspan=3, sticky=W + N + E + S)

        password = ttk.Entry(pw_top, width=20)
        password.grid(row=1, column=0, pady=20, padx=50)

        enter_pw_button = ttk.Button(pw_top, text="Enter", command=confirm_password, cursor='hand2')
        enter_pw_button.grid(row=2, column=0, pady=(0, 25))

        password.focus_force()
        pw_top.bind('<Return>', lambda func: confirm_password())


    employee_type_plural = employee_type+'s'

    if employee_type == 'Employee':
        employee_list = database_functions.get_employees_names()
        id_list = database_functions.get_employee_ids()

    else:
        employee_list = database_functions.get_manager_names()
        id_list = database_functions.get_manager_ids()

    if len(employee_list) == 0:
        messagebox.showerror("Error", f"There are no {employee_type_plural.lower()} currently registered")
        return

    select_top = Toplevel()
    gui.Window(select_top, f"Select {employee_type}", "357x125")

    counter = 0
    for i in id_list:
        employee_list[counter] += f" (ID No.: {str(i)})"
        counter += 1

    employee_var = StringVar()
    employee_var.set(employee_list[0])

    background_label = Label(select_top, bg=gui.Background_Color())
    background_label.grid(row=0, column=0, columnspan=2, rowspan=3, sticky=W + N + E + S)

    employee_menu = ttk.OptionMenu(select_top, employee_var, None, *employee_list)
    employee_menu.grid(row=1, column=0, columnspan=2, pady=20, padx=70)
    employee_menu.configure(width=28)

    select_button = ttk.Button(select_top, text="EDIT", command=edit, cursor='hand2')
    select_button.grid(row=2, column=0, pady=(0, 30))
    delete_button = ttk.Button(select_top, text="DELETE", command=enter_password, cursor='hand2')
    delete_button.grid(row=2, column=1, pady=(0, 30))


def add_bonus():
    def complete_add_bonus():

        if not bonus_entry.get().isnumeric():
            messagebox.showerror("Error", "Bonus contains letters and\or symbols")
            top.lift()
            return

        bonus = int(bonus_entry.get())

        emp_id = 0
        for i in id_list:
            if f"No.: {i})" in employee_var.get():
                emp_id = i
                break
        response = messagebox.askquestion("Confirm", "Are you sure?")
        if response == "yes":
            database_functions.add_bonus(emp_id, bonus)
            messagebox.showinfo("Confirmation", "Bonus Added Successfully")
            top.destroy()
            return
        top.lift()

    employee_list = database_functions.get_employees_names()
    id_list = database_functions.get_employee_ids()

    if len(employee_list) == 0:
        messagebox.showerror("Error", f"There are no employees currently registered")
        return

    counter = 0
    for i in id_list:
        employee_list[counter] += f" (ID No.: {str(i)})"
        counter += 1

    employee_var = StringVar()
    employee_var.set(employee_list[0])

    top = Toplevel()
    gui.Window(top, "Add Bonus", "357x155")
    background_label = Label(top, bg=gui.Background_Color())
    background_label.grid(row=0, column=0, rowspan=4, sticky=W + N + E + S)

    employee_menu = ttk.OptionMenu(top, employee_var, None, *employee_list)
    employee_menu.grid(row=1, column=0, pady=20, padx=70)
    employee_menu.configure(width=28)

    bonus_entry = ttk.Entry(top, width=20)
    bonus_entry.grid(row=2, column=0, pady=(0, 20))

    finish_button = ttk.Button(top, text="Add", command=complete_add_bonus, cursor='hand2')
    finish_button.grid(row=3, column=0, columnspan=2, pady=(0, 30))


def update_salary():
    def complete_update_salary(top, employee_var, salary, id_list):

        if len(salary) == 0:
            messagebox.showerror("Error", f"Please enter a salary")
            top.lift()
            return False
        try:
            float(salary)
        except:
            messagebox.showerror("Error", f"Salary contains letters and\or symbols")
            top.lift()
            return False

        emp_id = 0
        for i in id_list:
            if f"No.: {i})" in employee_var.get():
                emp_id = i
                break

        response = messagebox.askquestion("Confirm", "Are you sure?")
        if response == "yes":
            database_functions.edit_salary(emp_id, float(salary))
            messagebox.showinfo("Confirmation", "Salary Successfully Modified.")
            top.destroy()
            return
        top.lift()


    def enter_salary():
        top = Toplevel()
        gui.Window(top, "Update Salary", "350x160")
        background_label = Label(top, bg=gui.Background_Color())
        background_label.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=W + N + E + S)

        employee_label = Label(top, text="Employee:", anchor=W, width=14, bg=gui.Background_Color())
        employee_label.grid(row=1, column=0, padx=(20, 0), pady=20)

        employee_menu = ttk.OptionMenu(top, employee_var, None, *employee_list)
        employee_menu.grid(row=1, column=1, pady=(20), padx=(0, 25))
        employee_menu.configure(width=28)

        salary_label = Label(top, text="New Salary:", anchor=W, width=14, bg=gui.Background_Color())
        salary_label.grid(row=2, column=0, padx=(20, 0), pady=(0, 20))

        salary = ttk.Entry(top, width=20)
        salary.grid(row=2, column=1, pady=(0, 20), padx=(0, 50), sticky=W)

        finish_button = ttk.Button(top, text="Update", command=lambda: complete_update_salary(top, employee_var,
                                                                                              salary.get(), id_list), cursor='hand2')
        finish_button.grid(row=3, column=0, columnspan=2, pady=(0, 30))

    def confirm_password():
        if password.get() == '1234':
            pw_top.destroy()
            enter_salary()
        else:
            messagebox.showerror("Error", "Incorrect Password")
            pw_top.lift()
            password.focus_force()
            pw_top.bind('<Return>', lambda func: confirm_password())

    employee_list = database_functions.get_employees_names()
    id_list = database_functions.get_employee_ids()

    if len(employee_list) == 0:
        messagebox.showerror("Error", f"There are no employees currently registered")
        return

    counter = 0
    for i in id_list:
        employee_list[counter] += f" (ID No.: {str(i)})"
        counter += 1

    employee_var = StringVar()
    employee_var.set(employee_list[0])

    pw_top = Toplevel()
    gui.Window(pw_top, "Enter Password", "225x115")

    background_pw_label = Label(pw_top, bg=gui.Background_Color())
    background_pw_label.grid(row=0, column=0, rowspan=3, sticky=W + N + E + S)

    password = ttk.Entry(pw_top, width=20)
    password.grid(row=1, column=0, pady=20, padx=50)

    enter_pw_button = ttk.Button(pw_top, text="Enter", command=confirm_password, cursor='hand2')
    enter_pw_button.grid(row=2, column=0, pady=(0, 25))

    password.focus_force()
    pw_top.bind('<Return>', lambda func: confirm_password())

def delete_all_entries():
    def verification():
        response = messagebox.askquestion("Confirm", "Are you sure?")
        if response == "yes":
            database_functions.delete_all_entries()
            messagebox.showinfo("Confirmation", "Salary Successfully Modified.")
            return
        pw_top.destroy()

    def enter_password():
        if password.get() == '1234':
            pw_top.destroy()
            verification()
        else:
            messagebox.showerror("Error", "Incorrect Password")
            pw_top.lift()
            password.focus_force()
            pw_top.bind('<Return>', lambda func: enter_password())

    pw_top = Toplevel()
    gui.Window(pw_top, "Enter Password", "225x115")

    background_pw_label = Label(pw_top, bg=gui.Background_Color())
    background_pw_label.grid(row=0, column=0, rowspan=3, sticky=W + N + E + S)

    password = ttk.Entry(pw_top, width=20)
    password.grid(row=1, column=0, pady=20, padx=50)

    enter_pw_button = ttk.Button(pw_top, text="Enter", command=enter_password, cursor='hand2')
    enter_pw_button.grid(row=2, column=0, pady=(0, 25))

    password.focus_force()
    pw_top.bind('<Return>', lambda func: enter_password())

def upload_loaded_data(loaded_data, f_name, l_name, phone, email, street, city, country, zipcode,
                       birth, hired):
    f_name.insert(0, loaded_data[0][1])
    l_name.insert(0, loaded_data[0][2])
    phone.insert(0, loaded_data[0][5])
    email.insert(0, loaded_data[0][6])
    birth.insert(0, loaded_data[0][7])
    hired.insert(0, loaded_data[0][9])
    street.insert(0, loaded_data[0][12])
    city.insert(0, loaded_data[0][14])
    country.insert(0, loaded_data[0][13])
    zipcode.insert(0, loaded_data[0][15])


def check_empty_fields_error(fname, lname, phone):
    if len(fname) == 0:
        messagebox.showerror("Error", f"Please enter a first name")
        return False
    if len(lname) == 0:
        messagebox.showerror("Error", f"Please enter a last name")
        return False
    if len(phone) == 0:
        messagebox.showerror("Error", f"Please enter a phone number")
        return False
    return True

def check_empty_salary_error(salary):
    if len(salary) == 0:
        messagebox.showerror("Error", f"Please enter a salary")
        return False

def check_numeric_fields_error(field, type):
    if not field.isnumeric():
        messagebox.showerror("Error", f"{type} contains letters and\or symbols")
        return False

    return True


def reset_entries(f_name, l_name, phone, email, street, city, country, zipcode, salary, birth, hired):
        f_name.delete(0, END)
        l_name.delete(0, END)
        phone.delete(0, END)
        email.delete(0, END)
        birth.delete(0, END)
        birth.insert(0, "DD/MM/YYYY")
        hired.delete(0, END)
        hired.insert(0, "DD/MM/YYYY")
        salary.delete(0, END)
        street.delete(0, END)
        city.delete(0, END)
        country.delete(0, END)
        zipcode.delete(0, END)


def calendar_popup(date_entry, top):

    def select():
        d = cal.selection_get()
        popup.destroy()
        temp_date = d.strftime("%d/%m/%Y")
        date_entry.delete(0, END)
        date_entry.insert(0, temp_date)

    popup = Toplevel(top)
    w, h = gui.Center_Window(popup)
    popup.geometry("+%d+%d" % (w+360, h-50))
    cal = Calendar(popup,
                   font="Arial 14", selectmode='day',
                   year=date.today().year, month=date.today().month, day=date.today().day)
    cal.pack(fill="both", expand=True)
    ok = ttk.Button(popup, text="ok", command=select, cursor='hand2')
    ok.pack()