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

# Output : time.struct_time(tm_year=2023, tm_mon=11, tm_mday=1, tm_hour=1, tm_min=3, tm_sec=18, tm_wday=2, tm_yday=305, tm_isdst=0)

# It is quite unreadable, basically it is the datails about our current time, date. Now to make it more readable we need to use strftime.


print(time.strftime("%H:%M:%S", time.localtime())) #this strftime(string format time) takes 2 argument, the first one is format(means how you specify to display what), and the other one is on what basis? so it is on the basis of time.localtime()

print(time.strftime("%H:%M:%S", time.gmtime())) #but using this can give the other output, it is because gmtime is for cordinated universal time.
# and the local time is for users general lcoal time

# About different types of format: you can visit this link : `https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes`


# strptime - string parse time, it converts user info(dat, time) into time object.

user_time = "2023 06:56:04"
print(time.strptime(user_time, "%Y %H:%M:%S"))

# Now this will create a new time object with the user information
# Output : time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1, tm_hour=6, tm_min=56, tm_sec=4, tm_wday=6, tm_yday=1, tm_isdst=-1)

# So yeah this is it, time module in python is not only limited to what i have mentioned, here, plz visit through official documentation as well. 
# It is it for today, in next session, we will look at thread in python which is an important python concept.