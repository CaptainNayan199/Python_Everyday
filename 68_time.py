# Time module in python are very essentials module

import time

print(time.ctime(0)) #this will give me my epoch time, yeah i have already talked about epoch time in previous session, but generally epoch means that particular time from where couting is started(for python its jan 1, 1970)
# You may be wondering why there is argument 0? well it is nothing but hwo much seconds later do you want epoch to print times.

print(time.ctime(100000)) #i am saying here, give me the time after 10000..... seconds 


print(time.time()) #now this will give me the total seconds after the epoch, and currently my output is being shown as 1698799910.0859365. It means for me 1698799910.0859365 seconds of time has passed since 1st jan, 1970.

# That means if i pass that number as an argument in the time.ctime function, than i can get my current date and time.


print(time.ctime(1698799910)) #yes exactly i got my date and time which is wed nov 1 6666:36:50 2023

# or

print(time.ctime(time.time())) #this is also going to give me the same output

print(time.gmtime()) 
print(time.localtime())
#this both will give the same output, the first one is utc one and the second id the localtime.