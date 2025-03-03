# multithreading is used to perform multiple tasks, concurrently hence multithreading
# good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(name, last):
    time.sleep(8)
    print(f"Finished walking the dog named {name} {last}!")

def take_trash(frommm):
    time.sleep(2)
    print(f"Finished taking the trash out from {frommm}")

def get_mail():
    time.sleep(4)
    print("You get the mail from the mail box")

thread1 = threading.Thread(target=walk_dog, args=("Kutta", "Kamina" ))
thread1.start()

thread2 = threading.Thread(target=take_trash, args=("dustbin", ))
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("All the task are completed!")