# Python-Project
# 🌦️ Weather Forecasting Application Using Python

## 📌 Project Overview
This project is a real-time **Weather Forecasting Application** built using Python. It uses the **OpenWeatherMap API** to fetch live weather data based on the user's input (city name) and displays the data in a user-friendly GUI built with Tkinter.

## 🎯 Objective
To build a lightweight desktop application that allows users to:
- Enter a city name
- Get real-time weather information such as:
  - Temperature
  - Weather Condition
  - Humidity

## 🛠️ Technologies Used
- **Python 3.10.0**
- **Requests** (for API calls)
- **JSON**
- **OpenWeatherMap API**

## 🚀 Features
- Real-time weather updates
- Clean and responsive GUI
- Error handling for invalid city names or connection failures
- Easy to use for beginners and non-technical users

 
## Steps to Run the Project
STEP 1:Clone the Repository
First, clone the project to your local machine using the following command:
git clone REPO-URL
cd weather-forecast-app
STEP 2: Install Dependencies

The project uses the requests module to fetch weather data. To install the required dependencies, run:
pip install -r requirements.txt
Add Your OpenWeatherMap API Key

STEP 3:
Go to OpenWeatherMap to sign up and get your free API key.

Create a config.py file in the project directory and add your API key like this:
API_KEY = "your_openweathermap_api_key"
Run the Weather Application

STEP 4: Now that everything is set up, you can run the application with this command:


python weather.py
Enter City Name

Once the application is running, you will be prompted to enter a city name. Type the name of the city, and the app will fetch and display the weather information in the terminal.



## 🖼️ GUI Preview

✅ Sample Output
Enter city name: Hyderabad
Weather in Hyderabad:
Temperature: 32°C
Condition: Clear sky
Humidity: 42%
