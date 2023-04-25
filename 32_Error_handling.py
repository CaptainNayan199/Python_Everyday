# Error handling is very important in any kinds of programming language
#Similiarly it is same for python language
# sometimes we knowingly or unknowingly are going to make an error, it can be because of user, or sometimes even because of server, so we can handle those errors in python language,
# we can use try and exception in python langugage to handle errors and exception.


a = int(input("A number please: "))
print(f"Multiplication table of {a} is : \n")
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
