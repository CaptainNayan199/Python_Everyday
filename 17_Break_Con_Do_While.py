# Lopps in python run or work by each iteration and sometimes it can even rin for infinite times, and hence to stop that condition we should use break statement.
# Break is used to forcefully exit the iteration, but not the loop itself, it just jumps over the next iteration.
# Example : 

for i in range (12):
    if(i>9):
        print("Value is greater than 10, SO I am out")
        break
    print("SOme random stuffs")

for i in range (12):
    if (i==10):
        print("Value is 10")
        continue
    print("SOme random stuffs")

# Emulating/Immitating do while loop in python
# Python has no do while loop but we can emulate it using while loop

i = int(input("ENter a number : "))
while True: # this always runs, irrespective of whether the contdition is true or false
    print(i)
    if(i%2==0):
        print("Even number")
        break
    else:
        print("Odd number")
        break

while True:
    num = int(input("Give me a number : "))