# So what are threads ?
# In python thread are light weight process, threads are fundamental part of modern programming.

# Thread allows a program to operate more efficiently by handling multiple tasks at the same time.
# Threads share same memory space because of which data sharing among threads is completely a normal things. But this freedom can also lead to problem like deadlock and data races(which thread will use a particular data for the first time)

# In python there is a built in module for thread called as `threading`, using it we can create a new thread, manage them, and also communicate between them.

# But PS: in multi threaded python program, only one thread can execute at a time even if the cpu has multiple cores.

# Hence I/o bound task are more preferred to be handle by the concept of multi-threading whereas, cpu bound task are preferred to be handled by multi processing.

# What means I/o bound taks ?
#--> I/o bound tasks are tasks that primarily involve input/output operations, such as reading or writing to files, network operations, or interacting with a database. 
# --> Multi threading is used for this task because even if one thread is waiting other can continue execute.