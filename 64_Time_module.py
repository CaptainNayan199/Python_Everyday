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
print(time.time()) # this will give the time since the epoch in seconds.

print(time.ctime())