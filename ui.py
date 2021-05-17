from tkinter import *
from quizbrain import QuizBrain
from quizbrain import check_answer

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width =280,
            text="billy",
            fill=THEME_COLOR,
            font=("arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage("images/true.png")
        false_image = PhotoImage("images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, width=100, height=100, command=check_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, width=100, height=100)
        self.false_button.grid(column=1, row=2)

        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)