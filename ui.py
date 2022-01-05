from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        # creating GUI window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lb = Label(text='Score: 0', fg='white', bg=THEME_COLOR).grid(row=0, column=1)
        # creating quetion canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Question Goes HERE', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # creating true and false buttons
        true_img = PhotoImage(file="./true.png")
        false_img = PhotoImage(file="./false.png")
        self.right_btn = Button(image=true_img, highlightthickness=0) # add command here
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn = Button(image=false_img, highlightthickness=0) # add command here
        self.wrong_btn.grid(row=2, column=1)


        self.window.mainloop()


