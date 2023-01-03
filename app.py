#install requests package
import requests

api_key = ''

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#display weather data
weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

print(weather, temp)