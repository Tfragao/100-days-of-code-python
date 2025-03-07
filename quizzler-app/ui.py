from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.bg_color = "white"
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            200,
            150,
            width=280,
            text="some silly test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2,pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed_btn)
        self.false_btn.config(padx=50, pady=50)
        self.false_btn.grid(column=0, row=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed_btn)
        self.true_btn.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed_btn(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed_btn(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)