import os
import requests

# Fetch weather data from OpenWeatherMap API
def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def display_weather(data):
    city = data.get("name")
    temperature = data["main"].get("temp")
    humidity = data["main"].get("humidity")
    weather_condition = data["weather"][0].get("description")

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Fetch API key from environment variable
    if not api_key:
        print("Error: API key not found. Set the OPENWEATHER_API_KEY environment variable.")
        return

    city = input("Enter the city name: ")

    try:
        weather_data = fetch_weather(api_key, city)
        display_weather(weather_data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    main()