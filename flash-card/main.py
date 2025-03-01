from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FLIP_CARD_TIME = 3000

# ---------------------------- Creating new flash cards ------------------------------- #
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(FLIP_CARD_TIME, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#After 3 seconds change image
flip_timer = window.after(FLIP_CARD_TIME, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front =  PhotoImage(file="images/card_front.png")
card_back  =  PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

title_text = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
word_text= canvas.create_text(400,263, text="", font=("Arial", 60, "bold"))

#Buttons
right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, command=next_card)
right_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, command=next_card)
wrong_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

next_card()




window.mainloop()