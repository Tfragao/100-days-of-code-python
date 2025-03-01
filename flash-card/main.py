from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Creating new flash cards ------------------------------- #
def generate_french_word():
    df = pd.read_csv("data/french_words.csv")
    # Convert the DataFrame to a dictionary (French as keys, English as values)
    word_dict = df.set_index("French")["English"].to_dict()
    french_word = random.choice(list(word_dict.keys()))
    #Update text and title on the canvas
    canvas.itemconfig(word_text, text=french_word)
    canvas.itemconfig(title_text, text="French")

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#title_label = Label(text="Title", font=("Arial", 40, "italic"), bg="white")
#word_label = Label(text="Word", font=("Arial", 60, "bold"), bg="white")
#canvas.create_window(400, 150, window=title_label)
#canvas.create_window(400, 263, window=word_label)

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