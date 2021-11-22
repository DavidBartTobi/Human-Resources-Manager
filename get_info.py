import gui, database_functions
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date, datetime

def check_bonuses():
    def choose_check_bonus(bonus_type):
        emp_id = 0
        for i in id_list:
            if f"No.: {i})" in employee_var.get():
                emp_id = i
                break
        if bonus_type == 'normal':
            bonus = database_functions.get_bonus(emp_id)
            messagebox.showinfo("Bonus Check", f"{employee_var.get()} has received bonuses in the total of ${bonus}.")

        elif bonus_type == 'annual':
            date_hired = database_functions.get_employment_date(emp_id)
            d, m, y = date_hired.split('/')
            if date.today().toordinal() - date(int(y), int(m), int(d)).toordinal() >= 330:
                messagebox.showinfo("Bonus Check", f"{employee_var.get()} is eligible for the Annual Bonus.")
            else:
                messagebox.showinfo("Bonus Check", f"{employee_var.get()} is ineligible for the Annual Bonus.")

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
    gui.Window(top, "Check Employee Bonuses", "357x125")

    background_label = Label(top, bg=gui.Background_Color())
    background_label.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W + N + E + S)

    employee_menu = ttk.OptionMenu(top, employee_var, None, *employee_list)
    employee_menu.grid(row=1, column=0, columnspan=2, pady=20, padx=70)
    employee_menu.configure(width=28)
    finish_button = ttk.Button(top, text="Normal Bonus", command=lambda: choose_check_bonus('normal'), cursor='hand2')
    finish_button.grid(row=2, column=0, pady=(0, 30))

    finish_button = ttk.Button(top, text="Annual Bonus", command=lambda: choose_check_bonus('annual'), cursor='hand2')
    finish_button.grid(row=2, column=1, pady=(0, 30))


def check_hiring_requirements():
    def complete_check():
        emp_count, min_emp = database_functions.get_hiring_requirements(dep_var)
        amount_required = min_emp - emp_count

        if amount_required > 0:
            messagebox.showwarning("Hiring required", f"The {dep_var.get()} department requires {amount_required} "
                                                      f"more employee(s) in order to reach the minimal requirements")
        else:
            messagebox.showinfo("No Hiring Required", f"The {dep_var.get()} department has met the minimal "
                                                      f"employee requirements")

        top.destroy()

    department_list = database_functions.get_departments()

    if len(department_list) == 0:
        messagebox.showerror("Error", f"There are no departments currently registered")
        return

    dep_var = StringVar()
    dep_var.set(department_list[0])

    top = Toplevel()
    gui.Window(top, "Hiring Requirements", "357x125")

    background_label = Label(top, bg=gui.Background_Color())
    background_label.grid(row=0, column=0, rowspan=3, sticky=W + N + E + S)

    employee_menu = ttk.OptionMenu(top, dep_var, None, *department_list)
    employee_menu.grid(row=1, column=0, pady=20, padx=70)
    employee_menu.configure(width=28)
    finish_button = ttk.Button(top, text="Check", command=complete_check, cursor='hand2')
    finish_button.grid(row=2, column=0, columnspan=2, pady=(0, 30))


def employee_list():
    top = Toplevel()
    gui.Window(top, "Employee List", "715x700")

    emp_list = database_functions.get_emplist_employee_info()
    mang_list = database_functions.get_emplist_manager_info()
    dep_list = database_functions.get_departments()

    row_count = 0
    mang_bool = FALSE

    for department in dep_list:
        for manager in mang_list:
            column_count = 0
            if department in manager:
                id_label = Label(top, text=department, bg='white')
                id_label.grid(row=row_count, column=0, columnspan=8, sticky=W + E, ipadx=10, ipady=5)
                row_count += 1
                id_label = Label(top, text=manager[0], bg='grey')
                id_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                first_label = Label(top, text=manager[1], bg='grey')
                first_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                last_label = Label(top, text=manager[2], bg='grey')
                last_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                city_label = Label(top, text=manager[3], bg='grey')
                city_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                street_label = Label(top, text=manager[4], bg='grey')
                street_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                phone_label = Label(top, text=manager[5], bg='grey')
                phone_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                email_label = Label(top, text=manager[6], bg='grey')
                email_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                birth_label = Label(top, text=manager[7], bg='grey')
                birth_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                row_count += 1
                mang_bool = TRUE

        if mang_bool == FALSE:
            id_label = Label(top, text=department, bg='white')
            id_label.grid(row=row_count, column=0, columnspan=8, sticky=W + E, ipadx=10, ipady=5)
            row_count += 1

        mang_bool = FALSE

        for employee in emp_list:
            column_count = 0
            if department in employee:
                id_label = Label(top, text=employee[0], bg=gui.Background_Color())
                id_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                first_label = Label(top, text=employee[1], bg=gui.Background_Color())
                first_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                last_label = Label(top, text=employee[2], bg=gui.Background_Color())
                last_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                city_label = Label(top, text=employee[3], bg=gui.Background_Color())
                city_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                street_label = Label(top, text=employee[4], bg=gui.Background_Color())
                street_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                phone_label = Label(top, text=employee[5], bg=gui.Background_Color())
                phone_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                email_label = Label(top, text=employee[6], bg=gui.Background_Color())
                email_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                column_count += 1
                birth_label = Label(top, text=employee[7], bg=gui.Background_Color())
                birth_label.grid(row=row_count, column=column_count, sticky=W+E+N+S, ipadx=10, ipady=5)
                row_count += 1



def birthday_list():
    top = Toplevel()
    gui.Window(top, "Birthdays", "350x170")

    d = str(datetime.now().month)

    employee_list = database_functions.get_employees_names()
    employee_ids = database_functions.get_employee_ids()
    employee_bdays = database_functions.get_employee_bdays("Employees")
    manager_list = database_functions.get_manager_names()
    manager_ids = database_functions.get_manager_ids()
    manager_bdays = database_functions.get_employee_bdays("Managers")

    counter = 0
    for i in employee_ids:
        employee_list[counter] += f"  (ID No.: {str(i)})"
        counter += 1

    counter = 0
    for i in manager_ids:
        manager_list[counter] += f"  (ID No.: {str(i)})"
        counter += 1

    print_name_list = ''
    for i in range(len(employee_bdays)):
        if d in employee_bdays[i][3:5]:
            e_dep_name = database_functions.get_department_name(employee_ids[i], "Employee")
            print_name_list += f"{employee_list[i]}  {e_dep_name}  {employee_bdays[i]}\n\n"

    for i in range(len(manager_bdays)):
        if d in manager_bdays[i]:
            m_dep_name = database_functions.get_department_name(manager_ids[i], "Manager")
            print_name_list += f"{manager_list[i]}  {m_dep_name}  {manager_bdays[i]}\n\n"

    list_label = Label(top, text=print_name_list, bg=gui.Background_Color(), width=70, height=70)
    list_label.pack()

