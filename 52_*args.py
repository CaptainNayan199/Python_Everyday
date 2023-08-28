# So lets talk about *args in python
#  args - means arguments
#  so *args is important when we have to accept multiple and differenct types of variables
# *args is a parameter that accpets multiple non keyword arguments
# whereas, **kwargs accepts non keyword arguments, we will talk about that later.

# *args will pack all the arguments that it gets inside a tuple

# Lets see about keyword arguments and non keyword arguments


def std_info(name, age, cllg, sem, num): # a function that has several parameters
    print("Student name is ",name)
    print("He is ", age, " years old")
    print("He studies in ", cllg, " college")
    print("He is in ", sem, " sem")
    print("His contact number is ", num)

std_info("Nayan Pathak",20,"MMC","4th",985432523533) # so this is non keyword arguments, here we are assigning arguments, with respect to parameters in the method
