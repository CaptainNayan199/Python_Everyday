# So what are threads ?
# In python thread are light weight process, threads are fundamental part of modern programming.

# Thread allows a program to operate more efficiently by handling multiple tasks at the same time.
# Threads share same memory space because of which data sharing among threads is completely a normal things. But this freedom can also lead to problem like deadlock and data races(which thread will use a particular data for the first time)

# In python there is a built in module for thread called as `threading`, using it we can create a new thread, manage them, and also communicate between them.