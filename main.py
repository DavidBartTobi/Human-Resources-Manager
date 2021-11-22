from tkinter import Tk,Label
from PIL import ImageTk,Image

import gui
import main_window

def main():
    root = Tk()
    gui.Window(root, "Spacebook CoWorking", "1000x697")

    image = Image.open('logos/spacebook.jpeg')
    image.thumbnail((1000, 500))
    resized_image = ImageTk.PhotoImage(image)
    img_label = Label(root, image=resized_image, bg='#1e397e')
    img_label.grid(row=0,column=0, columnspan=4)

    main_window.Main_Window(root)

    root.mainloop()


if __name__ == '__main__':
    main()