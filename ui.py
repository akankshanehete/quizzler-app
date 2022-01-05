from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # declaring that the parameter quiz_brain is an object of the QuizBrain class
        self.quiz = quiz_brain
        # creating GUI window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lb = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_lb.grid(row=0, column=1)

        # creating quetion canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        # creating question text
        self.question_text = self.canvas.create_text(150, 125,
                                                     text='Question Goes HERE',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'),
                                                     width=280
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # creating true and false buttons
        true_img = PhotoImage(file="./true.png")
        false_img = PhotoImage(file="./false.png")
        self.right_btn = Button(image=true_img, highlightthickness=0, command=self.check_answer_true) # add command here
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn = Button(image=false_img, highlightthickness=0, command=self.check_answer_false) # add command here
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_lb.config(text="Score: " + str(self.quiz.score))
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_answer_true(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            print("configured")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question())






