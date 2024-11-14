import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]

        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Description: {description}")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "2784f08746a04ca10274e3eb6e829134"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)