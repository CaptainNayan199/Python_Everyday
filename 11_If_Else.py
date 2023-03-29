# condition in python: Condition statement in python are same as in other programming languages.
# few conditonal keywords are different in strucutres or else all are same.

#if elif else are main 3 conditional controlling structuring statement in python
# switch case statement are also there, we;ll see about them later on.


#conditional operator in python
# <, >, >, <=, ==, !=

# a = (input("Enter a number : "))
# if a%2==0 and a!=0:
#     print("Even")
# elif a%2==1:
#     print("Odd")
# else :
#     print("Zero")
    
    
#Nested if else statement in python 

a = int(input("Enter a number : "))

if a>0:
    if a <=10:
        print("The number is betweeen 1 to 10")
    elif a >10 and a <=20:
        print("The number is between 11-20")
    else :
        print("Ther number is greater than 20")
elif a<0:
    print("Number is negative")
elif a==0:
    print("Number is zero")
else:
    print("Incorrect number provided")
    