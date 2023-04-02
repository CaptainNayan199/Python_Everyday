# Match case in python language
# first and foremost there is no switch case in python as like in other programming languages
#Match case is a new feature added in python programming language. It was added after 3.10 version.
#Match case is like switch case in other programming languages like C, Java, etc.
#Match case is generally used for comparing values with the patterns
# PS: there will be no break statement in python match case as like in other programming languages.

num = int(input("Give me a positive number : "))

match num:
    case 1:
        print(" Number is 1 ")
    case 10:
        print("Number is 10")
    case 20:
        print("Number is 20")
    case 50:
        print("Number is 50")
    case 100:
        print("Number is 100") 
    case _:
        print(" Other number provided ")

