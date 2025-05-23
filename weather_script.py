import requests

def get_weather(city_name, api_key):
    """
    Obtiene datos meteorológicos para una ciudad específica utilizando la API de OpenWeatherMap.

    :param city_name: Nombre de la ciudad.
    :param api_key: Clave de la API de OpenWeatherMap.
    :return: Diccionario con los datos meteorológicos o mensaje de error.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Para obtener la temperatura en grados Celsius
        "lang": "es"       # Idioma de la descripción del clima
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene un error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Reemplaza con tu clave de API de OpenWeatherMap
    API_KEY = "YOUR_API_KEY"
    city = input("Introduce el nombre de la ciudad: ")
    
    weather_data = get_weather(city, API_KEY)
    
    if "error" in weather_data:
        print(f"Error al obtener los datos: {weather_data['error']}")
    else:
        print(f"Clima en {weather_data['name']}:")
        print(f"Temperatura: {weather_data['main']['temp']}°C")
        print(f"Descripción: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humedad: {weather_data['main']['humidity']}%")
        print(f"Velocidad del viento: {weather_data['wind']['speed']} m/s")