
import time

# time.sleep(3)
# print("Time's up!")

timer = int(input("For how many seconds do you want to set up the timer : "))

for counter in range(timer, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's Up!")
