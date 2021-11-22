from ttkthemes import ThemedStyle
from tkinter import *

def Window(top, title, size):
    top = top
    top.title(title)
    top.geometry(size)
    top.resizable(width=False, height=False)
    w, h = Center_Window(top)
    top.geometry("+%d+%d" % (w, h))
    style = ThemedStyle(top)
    style.set_theme('blue')


def Center_Window(win):
    win.update_idletasks()

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    return x, y

def Background_Color():
    return '#3d66cc'

def activate_grid(background_label, first_label, last_label, phone_label, email_label, street_label, city_label,
                  country_label, zip_label, salary_label, department_label, birth_label, hired_label, f_name,
                  l_name, phone, email, street, city, country, zipcode, salary, department, birth, hired,
                  birth_calendar, hired_calendar, finish_button):

    background_label.grid(row=0, column=0, rowspan=9, columnspan=4, sticky=W+N+E+S)

    first_label.grid(row=1, column=0, padx=(20,0), pady=20)
    last_label.grid(row=1, column=2, padx=(20,0), pady=20)

    phone_label.grid(row=2, column=0, padx=(20,0), pady=(0,20))
    email_label.grid(row=2, column=2, padx=(20,0), pady=(0,20))

    street_label.grid(row=3, column=0, padx=(20,0), pady=(0,20))
    city_label.grid(row=3, column=2, padx=(20,0), pady=(0,20))

    country_label.grid(row=4, column=0, padx=(20,0), pady=(0,20))
    zip_label.grid(row=4, column=2, padx=(20,0), pady=(0,20))

    salary_label.grid(row=5, column=0, padx=(20, 0), pady=(0, 20))
    department_label.grid(row=5, column=2, padx=(20, 0), pady=(0, 20))

    birth_label.grid(row=6, column=0, padx=(20,0), pady=(0,20))
    hired_label.grid(row=6, column=2, padx=(20, 0), pady=(0, 20))

    f_name.grid(row=1, column=1, pady=20)
    l_name.grid(row=1, column=3, pady=20, padx=(0,25), sticky=W)

    phone.grid(row=2, column=1, pady=(0,20))
    email.grid(row=2, column=3, pady=(0,20), padx=(0,25), sticky=W)

    street.grid(row=3, column=1, pady=(0,20))
    city.grid(row=3, column=3, pady=(0,20), padx=(0,25), sticky=W)
    country.grid(row=4, column=1, pady=(0,20))
    zipcode.grid(row=4, column=3, pady=(0,20), padx=(0,25), sticky=W)

    salary.grid(row=5, column=1, pady=(0,20))
    department.grid(row=5, column=3, pady=(0,20), padx=(0,25), sticky=W)

    birth.grid(row=6, column=1, pady=(0,10))
    hired.grid(row=6, column=3, pady=(0,10), padx=(0,25), sticky=W)

    birth_calendar.grid(row=7, column=1, pady=(0,20), padx=(0,25), sticky=W)
    hired_calendar.grid(row=7, column=3, pady=(0,20), padx=(0,25), sticky=W)
    finish_button.grid(row=8, column=0, pady=(0,20), columnspan=4)
