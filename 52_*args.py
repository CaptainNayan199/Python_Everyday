# So lets talk about *args in python
#  args - means arguments
#  so *args is important when we have to accept multiple and differenct types of variables
# *args is a parameter that accpets multiple non keyword arguments
# whereas, **kwargs accepts non keyword arguments, we will talk about that in later session.

# *args will pack all the arguments that it gets inside a tuple( ordered and unchangeable)

# Lets see about keyword arguments and non keyword arguments


def std_info(name, age, cllg, sem, num): # a function that has several parameters
    print("Student name is ",name)
    print("He is ", age, " years old")
    print("He studies in ", cllg, " college")
    print("He is in ", sem, " sem")
    print("His contact number is ", num)

std_info("Nayan Pathak",20,"MMC","4th",985432523533) # so this is non keyword arguments, here we are assigning arguments, with respect to parameters in the method, also called as positional arguments.


std_info(name="Nayan Pathak", age = 20, cllg = "MMC", sem = "4th", num = 35237532573) # so this is a keyword arguments, A keyword argument is where you provide a name to the variable as you pass it into the function
# we are assigning a arguments by defining its parameter, we can change the position or the format of assinging arguments as well in this, but not in non keyword arguments.

std_info(age = 20, cllg = "MMC", sem = "4th",name = "Nayan",  num = 375423895723852353)

# *ARGS - 
# eg 1 : 

def sum(*args): # the name does not play a vital role, we can name it as per our need, but * is a must.
    sum = 0
    for i in args: #ITERATING INSIDE A TUPLE
        sum += i
    print(sum)

sum(1,2,3,4,5,6,7,8,9,10)

# eg 2 :

def std_info(*name):
    for i in name:
        print(i)
    
std_info("Nayan", 20, "MMC")

# So yeah this much for today, in next session we will see about **kwargs in brief.
# Thank you! Happy coding