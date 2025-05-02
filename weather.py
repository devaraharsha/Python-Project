import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        print(f"\nWeather in {city.title()}:\n")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.title()}")
    else:
        print("\n❌ City not found or invalid API key.")

# Main part
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    api_key = "c25929edfe0e9d9c04691b18ca9ab7d8"  # Replace this with your actual API key
    get_weather(city, api_key)
