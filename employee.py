from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import date
import sqlite3

import gui, database_functions, update_info
from address import Address

class Employee:

    def __init__(self, employee_type):

        try:
            self.department_options = database_functions.get_departments()
            self.department_ids = database_functions.get_department_ids()
            self.department_var = StringVar()
            self.department_var.set(self.department_options[0])

        except:
            messagebox.showerror("Error", f"Please add departments before registering any employees")
            return

        self.top = Toplevel()
        self.employee_type = employee_type
        gui.Window(self.top, f"Add {employee_type}", "510x370")

        self.background_label = Label(self.top, bg=gui.Background_Color())

        self.first_label = Label(self.top, text = "First Name", anchor=W, width=13, bg=gui.Background_Color())
        self.last_label = Label(self.top, text="Last Name", anchor=W, width=13, bg=gui.Background_Color())

        self.phone_label = Label(self.top, text="Phone Number", anchor=W, width=13, bg=gui.Background_Color())
        self.email_label = Label(self.top, text="E-mail Address", anchor=W, width=13, bg=gui.Background_Color())

        self.street_label = Label(self.top, text="Street Address", anchor=W, width=13, bg=gui.Background_Color())
        self.city_label = Label(self.top, text="City", anchor=W, width=13, bg=gui.Background_Color())

        self.country_label = Label(self.top, text="Country", anchor=W, width=13, bg=gui.Background_Color())
        self.zip_label = Label(self.top, text="Zipcode", anchor=W, width=13, bg=gui.Background_Color())

        self.salary_label = Label(self.top, text="Monthly Salary", anchor=W, width=13, bg=gui.Background_Color())
        self.department_label = Label(self.top, text="Department", anchor=W, width=13, bg=gui.Background_Color())

        self.birth_label = Label(self.top, text="Birth Date", anchor=W, width=13, bg=gui.Background_Color())
        self.hired_label = Label(self.top, text="Date Hired", anchor=W, width=13, bg=gui.Background_Color())

        self.f_name = ttk.Entry(self.top, width=20)
        self.l_name = ttk.Entry(self.top, width=20)

        self.phone = ttk.Entry(self.top, width=20)
        self.email = ttk.Entry(self.top, width=20)

        self.street = ttk.Entry(self.top, width=20)
        self.city = ttk.Entry(self.top, width=20)
        self.country = ttk.Entry(self.top, width=20)
        self.zip = ttk.Entry(self.top, width=20)

        self.salary = ttk.Entry(self.top, width=20)

        self.department = ttk.OptionMenu(self.top, self.department_var, None, *self.department_options)
        self.department.configure(width=15)

        self.birth = ttk.Entry(self.top, width=20)
        self.hired = ttk.Entry(self.top, width=20)
        self.birth.insert(0, "DD/MM/YYYY")
        self.hired.insert(0, "DD/MM/YYYY")
        self.birth.bind("<FocusIn>", self.unbind_birth_date_entry)
        self.hired.bind("<FocusIn>", self.unbind_hired_date_entry)

        self.birth_calendar = ttk.Button(self.top, text='Calendar', command= lambda: self.calendar_popup("birth"), cursor='hand2')
        self.hired_calendar = ttk.Button(self.top, text='Calendar', command= lambda: self.calendar_popup("hired"), cursor='hand2')
        self.finish_button = ttk.Button(self.top, text = "           ADD", command = self.add_employee, width=15, cursor='hand2')

        gui.activate_grid(self.background_label, self.first_label, self.last_label, self.phone_label, self.email_label,
                          self.street_label, self.city_label, self.country_label, self.zip_label, self.salary_label,
                          self.department_label, self.birth_label, self.hired_label, self.f_name, self.l_name,
                          self.phone, self.email, self.street, self.city, self.country, self.zip, self.salary,
                          self.department, self.birth, self.hired, self.birth_calendar, self.hired_calendar,
                          self.finish_button)



    def add_employee(self):

        if update_info.check_empty_fields_error(self.f_name.get(), self.l_name.get(), self.phone.get()) is False:
            self.top.lift()
            return

        if update_info.check_empty_salary_error(self.salary.get()) is False:
            self.top.lift()
            return

        if update_info.check_numeric_fields_error(self.phone.get(), 'Phone Number') is False:
            self.top.lift()
            return

        if update_info.check_numeric_fields_error(self.salary.get(), 'Salary') is False:
            self.top.lift()
            return


        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        add_address = Address(c, self.street.get(), self.city.get(), self.country.get(), self.zip.get())
        address_id = add_address.get_last_row_id()

        conn.commit()
        conn.close()

        for i in self.department_options:
            if i == self.department_var.get():
                index = self.department_options.index(i)
                self.dep_id = self.department_ids[index]
                break

        insert = f"INSERT INTO {self.employee_type+'s'} (first_name, last_name, phone_number, email, birth_date, date_hired, " \
                 "monthly_salary, department, address) VALUES (?,?,?,?,?,?,?,?,?);"
        data_tuple = (self.f_name.get(), self.l_name.get(), self.phone.get(), self.email.get(), self.birth.get(),
                      self.hired.get(), self.salary.get(), self.dep_id, address_id)

        database_functions.add_employee(insert, data_tuple)
        database_functions.edit_employee_count('increase', self.dep_id)

        messagebox.showinfo("Confirmation", f"{self.employee_type} Registered")
        self.top.lift()
        update_info.reset_entries(self.f_name, self.l_name, self.phone, self.email, self.street, self.city,
                                  self.country, self.zip, self.salary, self.birth, self.hired)


    def unbind_birth_date_entry(self, event):
        self.birth.delete(0, "end")
        self.birth.unbind("<FocusIn>")
        return None

    def unbind_hired_date_entry(self, event):
        self.hired.delete(0, "end")
        self.hired.unbind("<FocusIn>")
        return None

    def calendar_popup(self, date_type):

        def select():
            d = cal.selection_get()
            popup.destroy()
            temp_date = d.strftime("%d/%m/%Y")
            if date_type == "birth":
                self.birth.delete(0, END)
                self.birth.insert(0, temp_date)
            if date_type == "hired":
                self.hired.delete(0, END)
                self.hired.insert(0, temp_date)

        popup = Toplevel(self.top)
        w, h = gui.Center_Window(popup)
        popup.geometry("+%d+%d" % (w+360, h-50))
        cal = Calendar(popup,
                       font="Arial 14", selectmode='day',
                       year=date.today().year, month=date.today().month, day=date.today().day)
        cal.pack(fill="both", expand=True)
        ok = ttk.Button(popup, text="ok", command=select, cursor='hand2')
        ok.pack()

