import smtplib
import datetime as dt
import pandas as pd
import random

SENDER_EMAIL = "sender@email.com"     #This is a placeholder, not a real email.
RECEIVER_EMAIL = "receiver@email.com" #This is a placeholder, not a real email.
PASSWORD = "sender password"
SUBJECT = "Happy Birthday!"
name = ""

def send_birthday_wishes():
    """Sends birthday wishes to a specific person."""
    global name
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs= RECEIVER_EMAIL,
            msg=f"Subject:{SUBJECT}\n\n{name}"
        )

now = dt.datetime.now()
today_day = now.weekday()
today_month = now.month

try:
    df = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error: You should create a birthday csv file with data to be send.")
else:
    birthdays_dict = {(row["month"], row["day"]) : row.to_dict() for _, row in df.iterrows()}
    if (today_month, today_day) in birthdays_dict:
        try:
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
                content = file.read()
                name = content.replace("[NAME]", birthdays_dict[(today_month, today_day)]["name"])
                send_birthday_wishes()
        except FileNotFoundError:
            print("Error: You should have a letter.txt file to send.")





