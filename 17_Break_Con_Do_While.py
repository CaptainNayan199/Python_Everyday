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

