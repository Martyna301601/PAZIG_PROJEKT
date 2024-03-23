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

        # LEWA STRONA ZDJĘCIE
        self.side_left = Image.open('logowanie.jpg')
        photo = ImageTk.PhotoImage(self.side_left)
        self.side_left_label = Label(self.login_frame, image=photo, bg='#040405')
        self.side_left_label.image = photo
        self.side_left_label.place(x=150, y=100)


def page():
    window = tk.Tk()
    LoginForn(window)
    window.mainloop()

if __name__ == '__main__':
    page()