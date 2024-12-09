import tkinter as tk
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import messagebox
import books
from data_base import select_name_book

class Library1:
    def __init__(self, root :tk.Tk):
        self.root = root
        self.root.title("Library")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg='#669999')
        self.start = CTkFrame(root, width=400, height=400, fg_color='white', corner_radius=15).place(x=50, y=30)
        self.label1 = CTkLabel(root, text='library', width=290, height=140, font=('Arial', 30, 'bold'),fg_color='white', bg_color='white', corner_radius=15, anchor='center',text_color='black').place(x=110, y=50)
        self.name = CTkLabel(root, width=330, height=60, fg_color='black', text='Name Book', anchor='w', corner_radius=15,
                             text_color='white', bg_color='white', font=('Arial', 20, 'bold')).place(x=90, y=155)
        self.name = CTkEntry(root, width=190, height=45, border_width=2, border_color='gray',
                             fg_color='white', text_color='black', corner_radius=15, bg_color='black')
        self.name.place(x=220, y=163)
        self.button = CTkButton(root, width=180, height=55, fg_color='black', text= 'end', corner_radius=20,border_width= 3, border_color= 'gray', text_color='white',bg_color= 'white', font=('Arial', 25, 'bold'),command=self.chk_name_book).place(x= 165, y=260)
        self.button2 = CTkButton(root, width=120, height=40, fg_color='black', text='sign up?', corner_radius=20,border_width=3, border_color='gray', text_color='white', bg_color='white',font=('Arial', 20, 'bold'), command=self.open_book).place(x=195, y=360)

    def open_book(self):
        self.root.destroy()

        new_page = tk.Tk()
        second = books.Books(new_page)


    def chk_name_book(self):
            name_book = self.name.get()
            user = select_name_book(name_book)
            messagebox.showinfo(name_book, user)








if __name__ == '__main__':
    window = tk.Tk()
    app1 = Library1(window)
    app1.root.mainloop()
