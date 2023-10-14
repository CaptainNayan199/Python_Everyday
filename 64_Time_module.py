# So today we are going to learn about time module in python
# This module is a built in function/module in python that allows us to work with times and perform times related operations.
# The time-related tasks includes : 
  # reading the current time
  # formatting time
  # sleeping for a specified number of seconds and so on.
  # Let's see in depth

# In Python, the time() function returns the number of seconds passed since epoch (the point where time begins - for python it is 1970 January 1st )


# First to use time module you need to import time module.

pip install time

# then

import time

res = time.time()
print(res) #this will give the time since the epoch in seconds.

res1 = time.ctime(res)
print(res1) #this will give the local time


res = time.time()
print(res)
print("Before 5 sec") 

time.sleep(5) # this will sleep the program for 5 sec and then execute further

print("Before 5 sec")
res1 = time.ctime(res)
print(res1)


import time
timee = time.localtime()
print(time.strftime("%m/%d/%Y , %H:%M:%S"))  #10/14/2023 , 11:24:11