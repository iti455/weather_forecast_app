import requests

def get_location():
    """Ask the user to manually enter their city"""
    return input("Enter your city name: ")

def get_weather(city):
    """Fetch weather data using WeatherAPI.com"""
    api_key = "31da17907c394732bf6120558252505"  # Replace with your actual WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            return f"Error: {data['error']['message']}"

        weather = {
            "City": data["location"]["name"],
            "Region": data["location"]["region"],
            "Country": data["location"]["country"],
            "Temperature": f"{data['current']['temp_c']} °C",
            "Condition": data['current']['condition']['text'],
            "Humidity": f"{data['current']['humidity']}%",
            "Wind Speed": f"{data['current']['wind_kph']} km/h"
        }

        return weather
    except Exception as e:
        return f"An error occurred: {str(e)}"

def display_weather():
    """Main function to run the weather app"""
    print("🌦️ Real-Time Weather Forecast App")
    print("----------------------------------")
    city = get_location()
    print(f"\nFetching weather for: {city}\n")
    weather_info = get_weather(city)

    if isinstance(weather_info, dict):
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print(weather_info)

if __name__ == "__main__":
    display_weather()
