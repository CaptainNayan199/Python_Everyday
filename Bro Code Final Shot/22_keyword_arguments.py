# keyword arguments : an arguments preceded by an identifier

# def average(a,b,c):
#     print("The average is : {} ".format((a+b+c)/3))
#
# average(10,20,30)


# def greetings(name, age, roll_num, rem):
#     print("Hello {}! You are {} years old. Your roll number is {} & your remarks is `{}`".format(name, age, roll_num, rem))
#
# greetings(rem="Good", name="Ujjwal", age=23, roll_num= 37)


# for x in range(1,11):
#     print(x, end=" ")

# print(1,2,3,4,5, sep="-")

def get_num(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

ph = get_num(country=977, area=123, first=9816, last=4821)
print(ph)