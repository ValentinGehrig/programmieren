import random
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

#Sample air quality data for five cities
CITIES = {
    "New York": {"PM2.5": 12, "PM10": 25, "NO2": 30, "SO2": 8, "CO": 0.5},
    "London": {"PM2.5": 15, "PM10": 28, "NO2": 40, "SO2": 10, "CO": 0.6},
    "Tokyo": {"PM2.5": 18, "PM10": 32, "NO2": 35, "SO2": 7, "CO": 0.4},
    "Paris": {"PM2.5": 10, "PM10": 20, "NO2": 25, "SO2": 6, "CO": 0.3},
    "Berlin": {"PM2.5": 14, "PM10": 26, "NO2": 33, "SO2": 9, "CO": 0.5}
}

def fetch_air_quality(city):
    return CITIES.get(city, None)

def process_data(data):
    if not data:
        return None

    df = pd.DataFrame(list(data.items()), columns=["Pollutant", "Concentration (µg/m³)"])
    return df

def visualize_data(df, city):
    if df is None:
        print("No data to visualize.")
        return

    df.plot(kind='bar', x='Pollutant', y='Concentration (µg/m³)', legend=False)
    plt.title(f"Air Quality Data for {city}")
    plt.xlabel("Pollutants")
    plt.ylabel("Concentration (µg/m³)")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def on_submit():
    city = city_var.get()
    data = fetch_air_quality(city)
    df = process_data(data)
    visualize_data(df, city)

#Tkinter UI Setup
root = tk.Tk()
root.title("Air Quality Visualizer")
root.geometry("400x300")

city_var = tk.StringVar()

label = tk.Label(root, text="Select a city:")
label.pack()

city_dropdown = ttk.Combobox(root, textvariable=city_var, values=list(CITIES.keys()))
city_dropdown.pack()
city_dropdown.current(0)

submit_button = tk.Button(root, text="Fetch Data", command=on_submit)
submit_button.pack()

root.mainloop()
