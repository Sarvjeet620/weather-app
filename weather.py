# Weather Application using OpenWeatherMap API
# Yeh program real-time weather information display karega

import requests  # Internet se data fetch karne ke liye
import json # JSON data handle karne ke liye
from dotenv import load_dotenv
import os
import requests

print("=== Python Weather App ===")
print("Kisi bhi city ka mausam jaaneye!\n")

def get_weather_data(city_name):
    """
    Yeh function OpenWeatherMap API se weather data fetch karta hai
    city_name: jis city ka weather chahiye
    """
    
    # API Key - (Note: Actual use ke liye aapko free API key sign up karni padegi)
    load_dotenv()

    API_KEY = os.getenv("API_KEY")  # Apna API key yahan daalein
    
    # API URL - OpenWeatherMap ka endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Complete URL banayein with parameters
    complete_url = f"{base_url}?q={city_name}&appid={API_KEY}&units=metric"
    # q={city_name} - city ka naam
    # appid={API_KEY} - authentication ke liye
    # units=metric - temperature Celsius mein
    
    try:
        # API call karna - data fetch karna
        response = requests.get(complete_url)
        
        # Check karna ki request successful hai ya nahi
        if response.status_code == 200:
            # JSON data parse karna
            weather_data = response.json()
            return weather_data
        else:
            print(f"❌ Error: City '{city_name}' not found!")
            return None
            
    except requests.exceptions.RequestException as e:
        # Internet connection error handle karna
        print(f"❌ Network Error: Please check your internet connection")
        return None

def display_weather_info(weather_data, city_name):
    """
    Yeh function weather data ko beautiful format mein display karta hai
    weather_data: API se mila hua raw data
    city_name: user ka input city
    """
    
    if weather_data is None:
        return  # Agar data nahi mila toh return ho jao
    
    # Main weather information extract karna
    main_info = weather_data.get('main', {})      # Temperature, humidity etc.
    weather_info = weather_data.get('weather', [{}])[0]  # Weather condition
    wind_info = weather_data.get('wind', {})      # Wind information

    # Temperature information
    current_temp = main_info.get('temp', 0)              # Current temperature
    feels_like = main_info.get('feels_like', 0)          # Feels like temperature
    min_temp = main_info.get('temp_min', 0)              # Minimum temperature
    max_temp = main_info.get('temp_max', 0)              # Maximum temperature
    humidity = main_info.get('humidity', 0)              # Humidity percentage

    # Weather condition
    description = weather_info.get('description', '')     # Weather description
    weather_main = weather_info.get('main', '')           # Main weather

    # Wind information
    wind_speed = wind_info.get('speed', 0)               # Wind speed
    
    # Beautiful display banayein
    print(f"\n{'='*50}")
    print(f"🌍 WEATHER FORECAST - {city_name.upper()}")
    print(f"{'='*50}")
    
    print(f"📊 Current Temperature: {current_temp}°C")
    print(f"🤔 Feels Like: {feels_like}°C")
    print(f"📈 Today's High: {max_temp}°C")
    print(f"📉 Today's Low: {min_temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"☁️  Weather: {description.title()}")
    
    # Weather condition ke according emoji show karna
    weather_emoji = get_weather_emoji(weather_main)
    print(f"🎯 Condition: {weather_emoji} {weather_main}")
    
    print(f"{'='*50}")

def get_weather_emoji(weather_condition):
    """
    Weather condition ke according emoji return karta hai
    """
    emoji_map = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️'
    }
    return emoji_map.get(weather_condition, '🌤️')  # Default emoji

def get_weather_advice(weather_main):
    """
    Weather condition ke according advice deta hai
    """
    advice_map = {
        'Clear': 'Perfect day for outdoor activities! 🎉',
        'Clouds': 'Light jacket le jaayein. 🧥',
        'Rain': 'Umbrella le kar jaayein! ☔',
        'Thunderstorm': 'Ghar mein rahein safe. 🏠',
        'Snow': 'Warm clothes pehnein. 🧤',
        'Mist': 'Drive carefully! 🚗'
    }
    return advice_map.get(weather_main, 'Have a nice day! 😊')

def main():
    """
    Main program function - user interaction handle karta hai
    """
    
    print("Welcome to Python Weather App! 🌤️")
    
    while True:
        # User se city name input lena
        print("\n" + "="*40)
        city_name = input("📍 City ka naam daalein (or 'exit' to quit): ").strip()
        
        # Exit condition check karna
        if city_name.lower() == 'exit':
            print("👋 Weather App se bahar ja rahe hain! Shukriya!")
            break
        
        # Empty input check karna
        if not city_name:
            print("❌ Please city ka naam daalein!")
            continue
        
        # Weather data fetch karna
        print(f"🔍 Searching weather for {city_name}...")
        weather_data = get_weather_data(city_name)
        
        # Agar data mil gaya toh display karna
        if weather_data:
            display_weather_info(weather_data, city_name)
            
            # Extra advice show karna
            weather_main = weather_data.get('weather', [{}])[0].get('main', '')
            advice = get_weather_advice(weather_main)
            print(f"💡 Advice: {advice}")
        
        # Continue karne ka option dena
        continue_search = input("\n🔍 Kya aap kisi aur city ka weather check karna chahenge? (y/n): ")
        if continue_search.lower() != 'y':
            print("👋 Shukriya! Weather App use karne ke liye!")
            break

# Program start karne ke liye
if __name__ == "__main__":
 main()