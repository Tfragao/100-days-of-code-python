import requests
from datetime import datetime
import smtplib
import threading

SENDER_EMAIL = "sender@email.com"        #This is a placeholder, not a real email.
RECEIVER_EMAIL = "receiver@email.com"    #This is a placeholder, not a real email.
PASSWORD = "your password here "
SUBJECT = "Look Up"
message = "Kizua look up in the sky the International Space Station is passing over your house."

MY_LAT = -1.0625    # Your latitude
MY_LONG = -10.5366  # Your longitude
DEGREE_DIFF = 5

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

def look_up():
    """Sends an email to tell me to look up in the sky."""
    global message
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs= RECEIVER_EMAIL,
            msg=f"Subject:{SUBJECT}\n\n{message}"
        )

def is_my_current_position():
    """ Returns true if the ISS is within the range of the position specified.
    Your position is within +5 or -5 degrees of the ISS position."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    if abs(MY_LAT - iss_latitude) <=5 and abs(MY_LONG - iss_longitude) <=5:
        return True

def is_night():
    """Returns True if it is dark."""
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if (time_now.hour <= sunrise) or (time_now.hour >= sunset):
        return True

def overhead_notifier():
    """Notifies me via an email if the ISS is close to my current position."""
    #If the ISS is close to my current position
    # and it is currently dark
    position = is_my_current_position()
    is_dark  = is_night()
    if is_dark and position:
        look_up()
    #TODO: this could be better implemented,treading.Timer gracefully
    threading.Timer(60, overhead_notifier).start()  # Schedule next execution

#Start the first execution
overhead_notifier()



