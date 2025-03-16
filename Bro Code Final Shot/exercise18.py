# weather app

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt
from tornado.httpclient import HTTPError

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.label_city = QLabel("Enter your city name", self)
        self.input_city = QLineEdit(self)
        self.getWeatherButton =  QPushButton("Get Weather", self)
        self.label_temp = QLabel(self)
        self.label_emojis = QLabel(self)
        self.label_desc = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(900,400, 800,800)
        self.setWindowTitle("Weather Application")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_city)
        vbox.addWidget(self.input_city)
        vbox.addWidget(self.getWeatherButton)
        vbox.addWidget(self.label_temp)
        # vbox.addWidget(self.label_city)
        vbox.addWidget(self.label_emojis)
        vbox.addWidget(self.label_desc)

        self.setLayout(vbox)

        self.label_city.setAlignment(Qt.AlignCenter)
        self.input_city.setAlignment(Qt.AlignCenter)
        self.label_temp.setAlignment(Qt.AlignCenter)
        self.label_emojis.setAlignment(Qt.AlignCenter)
        self.label_desc.setAlignment(Qt.AlignCenter)


        self.label_city.setObjectName("label_city")
        self.input_city.setObjectName("input_city")
        self.getWeatherButton.setObjectName("getWeatherButton")
        self.label_temp.setObjectName("label_temp")
        self.label_emojis.setObjectName("label_emojis")
        self.label_desc.setObjectName("label_desc")

        self.setStyleSheet("""
            QLabel{
                font-family : calibri;
            }
            QLabel#label_city{
                font-size:50px;
                
            }
            QLineEdit#input_city{
                font-size : 50px;
            }
            QPushButton#getWeatherButton{
                font-size : 40px;
                font-weight : bold;
            }
            QLabel#label_temp{
                font-size : 75px;
            }
            QLabel#label_emojis{
                font-size : 100px;
                font-family : segoe UI emoji;
            }
            QLabel#label_desc{
                font-size : 60px;
            }
        """)

        self.getWeatherButton.clicked.connect(self.getWeather)

    def getWeather(self):
        api_key = "444ec8e9388510e16af2648c61f4e49e"
        city = self.input_city.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as error:
            match response.status_code:
                case 400:
                    self.display_errors("There is bad request.\nPlease check your input!")
                case 401:
                    self.display_errors("Invalid API key!")
                case 403:
                    self.display_errors("Access is denied!")
                case 404:
                    self.display_errors("City Not found! Sorry!")
                case 500:
                    self.display_errors("Internal Server Error! Please try again later!")
                case 502:
                    self.display_errors("Bad Gateway! Invalid response from the server!")
                case 503:
                    self.display_errors("Service unavailable\nServer is down!")
                case 504:
                    self.display_errors("Gateway timeout\nNo response from the server!")
                case _:
                    self.display_errors("HTTP error occurred!\n%s" %error)
        except requests.exceptions.ConnectionError:
            self.display_errors("Connection Error!\nCheck your Internet Connection!")
        except requests.exceptions.Timeout:
            self.display_errors("Time out Error!\nRequest Timed Out!")
        except requests.exceptions.TooManyRedirects:
            self.display_errors("Too many redirects!\nCheck the URL!")
        except requests.exceptions.RequestException as req_error:
            self.display_errors(f"Request Error : {req_error}")





    def display_errors(self, mssg):
        self.label_temp.setStyleSheet("font-size : 30px;")
        self.label_temp.setText(mssg)
        self.label_emojis.clear()
        self.label_desc.clear()

    def display_weather(self, data):
        self.label_temp.setStyleSheet("font-size : 60px;")
        temp_kelvin = data["main"]["temp"]
        temp_c = temp_kelvin - 273.15
        temp_f = (temp_kelvin * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]

        self.label_temp.setText(f"{temp_c:.1f}°C / {temp_f:.1f}°F")
        self.label_emojis.setText(self.get_weather_emoji(weather_id))
        self.label_desc.setText(weather_desc)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <=321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return
        elif weather_id ==  781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <=804:
            return "☁️"
        else:
            return ""





if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

