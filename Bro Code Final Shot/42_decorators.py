# Decorator is a function that extends the behavior of another function without modifying the base function
# pass the base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper():
        print("You will get sprinkles ! ")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your icecream")


get_ice_cream()
# add_sprinkles(get_ice_cream())