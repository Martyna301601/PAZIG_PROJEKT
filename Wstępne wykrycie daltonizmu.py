import tkinter as tk 
from tkinter import * 
from PIL import ImageTk, Image 

class LoginForn: 
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)


def page():
    window = tk.Tk()
    LoginForn(window)
    window.mainloop()

if __name__ == '__main__':
    page()