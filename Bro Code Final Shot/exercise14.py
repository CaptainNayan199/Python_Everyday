# alarm clock using python

import time
import datetime

import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm.mp3"


if __name__ == "__main__":
    alarm_time = input("Enter the ALARM time (HH:MM:SS) : ")
    set_alarm(alarm_time)
