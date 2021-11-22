from tkinter import *
from tkinter import ttk


from employee import Employee
from department import Department
import update_info, get_info


class Main_Window:

    def __init__(self, root):
        self.root = root
        
        self.bg_lbl = Label(self.root, bg='#1e397e')
        self.bg_lbl.grid(row=1, column=0, rowspan=4, columnspan=4, sticky=W + N + E + S)

        self.bg_lbl = Label(self.root, bg='#1e397e', height=6)

        self.employee_button = ttk.Button(self.root, text="        Add Employee", command= lambda: Employee("Employee"), width=21, cursor='hand2')

        self.manager_button = ttk.Button(self.root, text="         Add Manager", command= lambda: Employee("Manager"), width=21, cursor='hand2')

        self.department_button = ttk.Button(self.root, text="      Add Department", command= Department, width=21, cursor='hand2')

        self.update_employee_button = ttk.Button(self.root, text=" Update Employee Info", command= lambda:update_info.update_employee('Employee'), width=21, cursor='hand2')

        self.update_manager_button = ttk.Button(self.root, text="  Update Manager Info", command= lambda:update_info.update_employee('Manager'), width=21, cursor='hand2')

        self.salary_button = ttk.Button(self.root, text="         Update Salary", command=update_info.update_salary, width=21, cursor='hand2')

        self.bonus_button = ttk.Button(self.root, text="            Add Bonus", command=update_info.add_bonus, width=21, cursor='hand2')

        self.check_bonus_button = ttk.Button(self.root, text="        Check Bonuses", command=get_info.check_bonuses, width=21, cursor='hand2')

        self.hiring_button = ttk.Button(self.root, text="   Hiring Requirements", command=get_info.check_hiring_requirements, width=21, cursor='hand2')

        self.employee_list_button = ttk.Button(self.root, text="         Employee List", command=get_info.employee_list, width=21, cursor='hand2')

        self.birthday_list_button = ttk.Button(self.root, text="          Birthday List", command=get_info.birthday_list, width=21, cursor='hand2')

        self.delete_all_button = ttk.Button(self.root, text="       Delete All Entries", command=update_info.delete_all_entries, width=21, cursor='hand2')

        self.status_label = Label(self.root, text="By David Bart  ", bd=1, relief=SUNKEN, anchor=E, bg='#1e397e')

        self.Activate_Grid()


    def Activate_Grid(self):
        self.bg_lbl.grid(row=4, column=0, columnspan=4, sticky=W + N + E + S)

        self.employee_button.grid(row=1, column=0, pady=(40, 0))
        self.manager_button.grid(row=2, column=0, pady=40)
        self.department_button.grid(row=3, column=0)

        self.update_employee_button.grid(row=1, column=1, pady=(40, 0))
        self.update_manager_button.grid(row=2, column=1, pady=40)
        self.salary_button.grid(row=3, column=1)

        self.bonus_button.grid(row=1, column=2, pady=(40, 0))
        self.check_bonus_button.grid(row=2, column=2, pady=40)
        self.hiring_button.grid(row=3, column=2)

        self.employee_list_button.grid(row=1, column=3, pady=(40, 0))
        self.birthday_list_button.grid(row=2, column=3, pady=40)
        self.delete_all_button.grid(row=3, column=3)

        self.status_label.grid(row=5, column=0, columnspan=4, sticky=W + E)

