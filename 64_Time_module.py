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

# Here, %Y, %m, %d, %H etc. are format codes.
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23
# %M - minutes [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 61]

# There are lots and lots of things inside a time module. Above were some basics. You can check it in documentation as well. All cannot be covered in one single class.
# So yeah this is it all about time module in python. Tomorrow we will 