
from api_client import get_json
from pprint import pprint


GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


# Exercise 1
def exercise_1():
    print("--- Exercise 1 ---")
    data = get_json(GEO_URL, params={"name": "Stockholm", "count": 1})
    pprint(data, sort_dicts=False)
    city = data["results"][0]
    print(city["latitude"], city["longitude"])


# Exercise 2
def exercise_2():
    print("--- Exercise 2 ---")
    data = get_json(WEATHER_URL, params={
        "latitude": 59.33,
        "longitude": 18.06,
        "current": "temperature_2m,wind_speed_10m",
    })
    pprint(data, sort_dicts=False)
    current = data["current"]
    units = data["current_units"]
    print(current["temperature_2m"], units["temperature_2m"])
    print(current["wind_speed_10m"], units["wind_speed_10m"])


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
