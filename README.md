#  Weather Forecast App

A simple, real-time weather forecast web app built with Python and Flask. Users can enter any city name to get the current weather details powered by WeatherAPI.

## Features

- City-based weather lookup
- Displays temperature, humidity, wind speed, and weather conditions
- Clean and minimal web UI
- Uses real-time data from [WeatherAPI.com](https://www.weatherapi.com/)

## Tech Stack

- Frontend: HTML, CSS (inline styling)
- Backend: Python (Flask)
- API: WeatherAPI

## Project Structure
weather-forecast-app/
├── app.py # Command-line weather app
├── main.py # Flask web application
├── templates/
│ └── index.html # HTML form and weather display
└── README.md

## Install Dependencies
pip install flask requests

## Add Your WeatherAPI Key
Replace "your_weatherapi_key" in main.py and app.py with your actual API key from WeatherAPI.com

## Run the Flask App
python main.py
Open your browser and go to: http://127.0.0.1:5000




