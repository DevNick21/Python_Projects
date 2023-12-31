import requests
import os
from dotenv import load_dotenv

load_dotenv()


MY_LATITUDE = os.getenv("MY_LAT")
MY_LONGITUDE = os.getenv("MY_LONG")

# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()

# data = res.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

res = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
