# Pomodoro technique is composed of:
    # 25 minutes work
    # 5 minutes break
    # 25 minutes work
    # 5 minutes break
    # 25 minutes work
    # 5 minutes break
    # 25 minutes work
    # 20 minutes break

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global  reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    #If it's 2nd/4th/6th rep:
    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # checkmark for every two reps
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark_label = Label(text="", font=(GREEN, 14), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()