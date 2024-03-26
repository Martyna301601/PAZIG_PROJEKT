import tkinter as tk 
from tkinter import * 
from PIL import ImageTk, Image 

class LoginForn: 
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        ########TŁO##########
        self.bg_frame = Image.open('tlo.png')
        self.bg_frame = self.bg_frame.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()))  #dostosowania rozmiaru ramki do aktualnego rozmiaru ekranu
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)

        ########LOGIN RAMKA##########
        self.login_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.login_frame.place(x=200, y=70)

        self.txt = 'TEST NA DALTONIZM'
        self.heading = Label(self.login_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=80, y=30, width=500, height=30)

        ########LEWA STRONA ZDJĘCIE##########
        self.side_left = Image.open('logowanie.jpg')
        photo = ImageTk.PhotoImage(self.side_left)
        self.side_left_label = Label(self.login_frame, image=photo, bg='#040405')
        self.side_left_label.image = photo
        self.side_left_label.place(x=150, y=100)

        ########OBRAZ LOGOWANIA#########
        self.sign_image = Image.open('mail2.jpg')
        self.sign_image = self.sign_image.resize((120, 120))
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_image_label = Label(self.login_frame, image=photo, bg='#040405')
        self.sign_image_label.image = photo
        self.sign_image_label.place(x=625, y=130)

        self.sign_label = Label(self.login_frame, text='Podaj maila', bg='#040405', fg='white', font=('yu gothic ui', 13, 'bold'))
        self.sign_label.place(x=640, y=240)

        ########LOGOWANIE#########
        self.username_label = Label(self.login_frame, text='Mail', bg='#040405', font=('yu gothic ui', 13, 'bold'), fg='#4f4e4d')
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=590, y=335, width=270)

        self.username_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=359)


def page():
    window = tk.Tk()
    LoginForn(window)
    window.mainloop()

if __name__ == '__main__':
    page()