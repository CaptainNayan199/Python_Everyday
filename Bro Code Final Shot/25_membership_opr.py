# membership operator are used to test whether a value or variable is found in a sequence(string, list, tuple, sets or dictionaries)

# num = [1,2,3,4,5]
# fruits = ("Mango", "Orange", "Banana", "Cherry", "Litchi")
# cars = {"Lambo", "Bugatti", "Mercedes", "Ferari", "Volkswagen"}
# name = "Nayan Pathak"
# dicti = {"Name":"Nayan", "Age":22, "Address":"Birtamode", "isMarried": False}
#
# if 6 not in num:
#     print("No it is not!")
#
# if "Litchi" in fruits:
#     print("Yes there is!")
#
# if "Lambo" not in cars:
#     print("No there is not!")
#
# if 'N' in name:
#     print("Yes it's there!")
#
# if "Nayan" in dicti.values():
#     print("Yes there is !")
#
# if "Address" in dicti.keys():
#     print("Yes there is !")
#
# if "Name" in dicti:
#     print("Yesssss")


email = "nayanpathak233199@gmail.com"

if '@' in email and '.' in email:
    print("Valid email")