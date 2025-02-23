# *args = allows users to pass multiple non-key arguments, result in tuple
# **kwargs = allows users to pass multiple keyword arguments, result in dictionary
# * is known as unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Nayan", "Pathak")


# def address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# address(street=3214, city="Birtamode", state="1", zip_code=57204, )

def shipping_label(*args, **kwargs):
    for i in args:
        print(i, end=" ")
    print()
    for a,b in kwargs.items():
        print("{} : {}".format(a, b))

shipping_label("Ujjwal", "Nayan", "Sita", "Sitoshna", age="22", city="Btm", zip="57204")