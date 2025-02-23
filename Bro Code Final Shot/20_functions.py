# functions in python are a block of code

# def func_name():
#     print("My first function!")
#
# func_name()

# def func_sec(name, age):
#     print(f"Hello {name}. You are {age} years old.")
# func_sec("Nayan", 22)

# def disp_inv(username, amount, due_date):
#     print(f"Hello {username}. Your bill of ${amount:.2f} is due: {due_date}")
#
# disp_inv("Nayan", 4000, "11/21")

# return is used in function to end and send a result back to the caller
# def add(a,b):
#     return a+b
#
# mm = add(10,20)
# print(mm)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last


full_name = create_name("nayan", "pathak")
print(full_name)