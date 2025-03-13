# weather app
# 444ec8e9388510e16af2648c61f4e49e my api key

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.label_city = QLabel("Enter your city name", self)
        self.input_city = QLineEdit(self)
        self.getWeatherButton =  QPushButton("Get Weather", self)
        self.label_temp = QLabel("27°C",self)
        self.label_emojis = QLabel("☀️", self)
        self.label_desc = QLabel("Sunny",self)
        self.initUI()

    def initUI(self):
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

    def getWeather(self):
        pass

    def display_errors(self, mssg):
        pass

    def display_weather(self, data):
        pass






if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

