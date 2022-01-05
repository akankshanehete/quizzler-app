from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window['bg'] = THEME_COLOR
        self.window.geometry("340x500")

        self.window.mainloop()


