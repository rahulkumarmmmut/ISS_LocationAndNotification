import time
import smtplib
import requests
from datetime import datetime

# providing user information
My_lat = "PROVIDE YOUR LATITUDE"
my_long = "PROVIDE YOUR LONGITUDE"
my_email = "PROVIDE YOUR EMAIL ID"
my_pass = "PROVIDE YOUR APP GENERATED GOOGLE PASSWORD"


# Checking if the ISS is close to your location
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_lat = response.json()["iss_position"]["latitude"]
    data_lon = response.json()["iss_position"]["longitude"]
    if My_lat - 5 <= data_lat <= My_lat + 5 and my_long - 5 <= data_lon <= my_long + 5:
        return True


# Checking if the time is night, which is after sunset or before sunrise
def is_night():
    parameters = {
        "lat": My_lat,
        "lng": my_long,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# sending email as a notification
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_pass, my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Look Up \n\n The ISS is above you in the sky"
        )
