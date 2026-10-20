
from api_client import get_json
from pprint import pprint


GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def find_city(name):
    data = get_json(GEO_URL, params={"name": name, "count": 1})
    if not data or "results" not in data:
        return None
    return data["results"][0]


def get_weather(lat, lon):
    return get_json(WEATHER_URL, params={
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    })


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


# Exercise 3# A non-existing city returns a dict without the "results" key
    print(get_json(GEO_URL, params={"name": "asdfghjkl", "count": 1}))

def exercise_3():
    print("--- Exercise 3 ---")
    name = input("City: ").strip()
    city = find_city(name)
    print(city["latitude"], city["longitude"])
    weather = get_weather(city["latitude"], city["longitude"])
    current = weather["current"]
    units = weather["current_units"]
    print(f"{city['name']}, {city['country']}: "
          f"{current['temperature_2m']}{units['temperature_2m']}, "
          f"wind {current['wind_speed_10m']} {units['wind_speed_10m']}")


# Exercise 4
def exercise_4():
    print("--- Exercise 4 ---")
    # A non-existing city returns a dict without the "results" key
    #print(get_json(GEO_URL, params={"name": "asdfghjkl", "count": 1}))
    
    name = input("City: ").strip()
    city = find_city(name)
    if city is None:
        print(f"City '{name}' not found.")
        return

    weather = get_weather(city["latitude"], city["longitude"])
    current, units = weather["current"], weather["current_units"]
    print(f"{city['name']}, {city['country']}: "
          f"{current['temperature_2m']}{units['temperature_2m']}, "
          f"wind {current['wind_speed_10m']} {units['wind_speed_10m']}")


# Running exercises
if __name__ == "__main__":
    #exercise_1()
    #exercise_2()
    #exercise_3()
    exercise_4()
