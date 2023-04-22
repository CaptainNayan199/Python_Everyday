# We can use for loops with else as well in python 


for i in range(10):
    print(i) # now this will print upto 9 
else:
    print("Greater than 10") # this get printed after 9 as 10 is not satisfied in upper for loop, 


for i in range(10):
    print(i)
    if i==4:
        break
else:
    print("Hehehehe")

# Now we used break in for loop, hence the loop is getting break, but else does not gets executed, because else only gets executed if the loop gets successfully, if loop gets break without finishing then the else statement does not gets gets executed.


# Same is the condition with other loops as well

i = 0
while i<10:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("Hehehehe")