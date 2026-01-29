import requests
import datetime
import json
import os
import sys
import geocoder


cache_file = "Weather_cache.json"


if os.path.exists(cache_file):
    with open(cache_file) as f:
        cache = json.load(f)

else:
    cache = {}

date_input = input("Enter a date: (YYYY-mm-dd) or press enter for tomorrow: ").strip()

if date_input =="":
    searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    try:
        searched_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYY-mm-dd.")
        sys.exit()

searched_date = searched_date.strftime("%Y-%m-%d")

location_input = input("Enter a city name(or press enter for Bratislava): ").strip()

if location_input == "":
    location_input = "Bratislava"

g = geocoder.osm(location_input, user_agent="rain-forecast-app")

if g.ok and g.latlng:
    latitude, longitude = g.latlng
else:
    print("Geocoder failed. Please enter coordinates manually.")

    try:
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
    except ValueError:
        print("Invalid coordinates.")
        sys.exit()


cache_key = f"{searched_date}|{location_input.lower()}"


if cache_key in cache:
    print("Result loaded from file (no API call).")
    precip = cache[cache_key]

else:
    print("Fetching data from API...")

URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=precipitation_sum&start_date={searched_date}&end_date={searched_date}"
print(URL)
response = requests.get(URL)
result = response.json()




precip = result["daily"]["precipitation_sum"][0]

cache[cache_key] = precip
with open(cache_file, "w") as f:
    json.dump(cache, f, indent=4)

if precip > 0:
    print(f"It will rain. Precipitation: {precip} mm")
elif precip == 0:
    print("It will not rain.")
else:
    print("I don't know.")

