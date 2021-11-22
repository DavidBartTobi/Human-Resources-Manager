from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

import gui

class Department:

    def __init__(self):

        self.top = Toplevel()
        gui.Window(self.top, "Add Department", "332x150")

        self.background_label = Label(self.top, bg=gui.Background_Color())

        self.name_label = Label(self.top, text="Department Name", anchor=W, width=20, bg=gui.Background_Color())
        self.min_label = Label(self.top, text="Min. Employee Required", anchor=W, width=20, bg=gui.Background_Color())

        self.name = ttk.Entry(self.top, width=20)
        self.min_employee = ttk.Entry(self.top, width=20)

        self.finish_button = ttk.Button(self.top, text="ADD", command=self.add_department, cursor='hand2')

        self.name.focus_force()
        self.top.bind('<Return>', lambda func: self.add_department())

        self.activate_grid()

    def activate_grid(self):

        self.background_label.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=W+N+E+S)
        self.name_label.grid(row=1, column=0, padx=(20,0), pady=20)
        self.min_label.grid(row=2, column=0, padx=(20,0), pady=(0,20))
        self.name.grid(row=1, column=1, pady=20, padx=20)
        self.min_employee.grid(row=2, column=1, pady=(0,20), padx=20)
        self.finish_button.grid(row=3, column=0, columnspan=2, pady=(0,20))


    def add_department(self):
        if len(self.name.get()) == 0 or len(self.min_employee.get()) == 0:
            messagebox.showerror("Error", f"Please fill all fields")
            self.top.lift()
            self.top.bind('<Return>', lambda func: self.add_department())
            return
        if not self.min_employee.get().isnumeric():
            messagebox.showerror("Error", f"Employee Number contains letters and\or symbols")
            self.top.lift()
            self.top.bind('<Return>', lambda func: self.add_department())
            return

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        insert = "INSERT INTO Departments (name, min_employee) VALUES (?,?);"
        data_tuple = (self.name.get(), self.min_employee.get())
        c.execute(insert, data_tuple)

        self.name.delete(0, END)
        self.min_employee.delete(0, END)

        messagebox.showinfo("Confirmation", f"Department Registered")
        self.top.lift()
        self.name.focus_force()

        conn.commit()
        conn.close()