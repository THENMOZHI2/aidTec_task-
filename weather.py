import requests
import tkinter as tk

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

def get_weather_report():
    city_name = city_entry.get()
    api_key = "666a07558ceaf9ecbd4c3999b5d67e73"  # Replace this with your actual OpenWeatherMap API key
    weather_data = get_weather_data(city_name, api_key)

    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        result_label.config(text=f"Weather in {city_name}:")
        temp_label.config(text=f"Temperature: {temperature}K")
        pressure_label.config(text=f"Atmospheric Pressure: {pressure}hPa")
        humidity_label.config(text=f"Humidity: {humidity}%")
        desc_label.config(text=f"Weather Description: {weather_description}")
    else:
        result_label.config(text="City not found.")

# Setting up the GUI
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name: ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=get_weather_report)
submit_button.pack()

result_label = tk.Label(root, text="",fg="blue",font=("Arial",30,"bold"))
result_label.pack()

temp_label = tk.Label(root, text="",bg="lightpink",font=("Arial",30,"bold"))
temp_label.pack()

pressure_label = tk.Label(root, text="",bg="lightblue",font=("Arial",30,"bold"))
pressure_label.pack()

humidity_label = tk.Label(root, text="",bg="lightyellow",font=("Arial",30,"bold"))
humidity_label.pack()

desc_label = tk.Label(root, text="")
desc_label.pack()

root.mainloop()
