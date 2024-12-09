# import data_base
import tkinter as tk
from customtkinter import CTkLabel,CTkEntry,CTkButton,CTkFrame
from tkinter import messagebox
from data_base import add_book
import Library
#-------------tkinter settings-------------
class Books:
    def __init__(self, root : tk.Tk):
        # super().__init__(root)
        self.state_txt = [False,False,False,False]
        self.root = root
        self.root.title("Books")
        self.root.geometry('500x500')
        self.root.resizable(False,False)
        self.root.config(bg='#669999')
        self.start = CTkFrame(root, width=400, height=400,fg_color='white', corner_radius=15).place(x=50, y=30)
        self.label1 = CTkLabel(root, text='book specifications', width=255, height=50, font=('Arial', 25, 'bold'),fg_color='white',bg_color='white', corner_radius=15, anchor='center', text_color='black').place(x=120, y=40)
        self.name = CTkLabel(root, width=300, height=50, fg_color='black', text= 'Name', anchor='w',corner_radius=15, text_color='white',bg_color=  'white', font=('Arial', 20, 'bold')).place(x=100 , y=105)
        self.name = CTkEntry(root, width=190, height=40, border_width=2, border_color='gray',
                             fg_color='white', text_color='black', corner_radius=15, bg_color='black')
        self.name.place(x= 200, y=110)
        self.name.bind('<KeyRelease>', self.chk_name)

        self.family = CTkLabel(root, width=300, height=50, fg_color='black', text= 'family', anchor='w',corner_radius=15, text_color='white',bg_color= 'white',font=('Arial', 20, 'bold')).place(x=100 , y=165)
        self.family = CTkEntry(root, width=190, height=40, border_width=2, border_color='gray', fg_color='white',
                               text_color='black', corner_radius=15, bg_color='black')
        self.family.place(x= 200, y=170)
        self.family.bind('<KeyRelease>', self.chk_family)

        self.book = CTkLabel(root, width=300, height=50, fg_color='black', text= 'book', anchor='w',corner_radius=15, text_color='white',bg_color= 'white', font=('Arial', 20, 'bold')).place(x=100 , y=225)
        self.book = CTkEntry(root, width=190, height=40, border_width=2, border_color='gray', fg_color='white',
                             text_color='black', corner_radius=15, bg_color='black')
        self.book.place(x= 200, y=230)
        self.book.bind('<KeyRelease>', self.chk_book)

        self.price = CTkLabel(root, width=300, height=50, fg_color='black', text= 'price', anchor='w',corner_radius=15, text_color='white',bg_color= 'white', font=('Arial', 20, 'bold')).place(x=100 , y=285)
        self.price = CTkEntry(root, width=190, height=40, border_width=2, border_color='gray', fg_color='white',
                              text_color='black', corner_radius=15, bg_color='black')
        self.price.place(x= 200, y=290)
        self.price.bind('<KeyRelease>', self.chk_price)

        self.button = CTkButton(root, width=140, height=40, fg_color='black', text= 'end', corner_radius=20,border_width= 3, border_color= 'gray', text_color='white',bg_color= 'white', font=('Arial', 25, 'bold'),command=self.submit).place(x= 100, y=360)

        self.button2 = CTkButton(root, width=120, height=40, fg_color='black', text='library?', corner_radius=20,
                                border_width=3, border_color='gray', text_color='white', bg_color='white',
                                font=('Arial', 20, 'bold'), command=self.go_to_library).place(x=282, y=360)

#------------cheng page-------------
    def go_to_library(self):
        self.root.destroy()

        new_page = tk.Tk()
        second = Library.Library1(new_page)

#------------chek name-------------

    def chk_name(self, event):
        fname = self.name.get()
        if len(fname) > 2:
            self.name.configure(border_color='green')
            self.state_txt[0] = True
        else:
            self.name.configure(border_color='red')
            self.state_txt[0] = False

#-----------chek last name---------

    def chk_family(self, event):
        fam = self.family.get()
        if len(fam) > 2:
            self.family.configure(border_color='green')
            self.state_txt[1] = True
        else:
            self.family.configure(border_color='red')
            self.state_txt[1] = False

#-----------chek book-----------

    def chk_book(self, event):
        book = self.book.get()
        if len(book) > 2:
            self.book.configure(border_color='green')
            self.state_txt[2] = True
        else:
            self.book.configure(border_color='red')
            self.state_txt[2] = False

#-----------chek price-------------

    def chk_price(self, event):
        price = self.price.get()
        if len(price) > 2:
            self.price.configure(border_color='green')
            self.state_txt[3] = True
        else:
            self.price.configure(border_color='red')
            self.state_txt[3] = False

#-----------chek submit-------------

    def submit(self):
        # log = tk.Tk()
        name = self.name.get()
        family = self.family.get()
        book = self.book.get()
        price = self.price.get()

        if self.state_txt[0]:
            if self.state_txt[1]:
                if self.state_txt[2]:
                    if self.state_txt[3]:
                        add_book(name,family,book,price)
                        messagebox.showinfo(title='Success', message='Book successfully submitted!')
                    else:
                        messagebox.showerror(title='Error', message='Please enter your price!')
                else:
                    messagebox.showerror(title='Error', message='Please enter your book!')
            else:
                messagebox.showerror(title='Error', message='Please enter your family!')
        else:
            messagebox.showerror(title='Error', message='Please enter your name!')


if __name__ == '__main__':
    root = tk.Tk()
    app = Books(root= root)
    root.mainloop()





