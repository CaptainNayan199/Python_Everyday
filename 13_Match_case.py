# Match case in python language
# first and foremost there is no switch case in python as like in other programming languages
#Match case is a new feature added in python programming language. It was added after 3.10 version.
#Match case is like switch case in other programming languages like C, Java, etc.
#Match case is generally used for comparing values with the patterns

num = int(input("Give me a positive number : "))

match num:
    case "even":
        print(" Number is Even ")
    case "num%2!=0":
        print("Number is odd")
    case _:
        print("Number is zero ")

