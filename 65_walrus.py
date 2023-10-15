# Wlarus operator is a new thing in python. It came in practice after python 3.8 version. That means python version older than 3.8 does not support walrus operator. It is very useful operator in python.
# So this operator allows us to assign value to the variable within an expression.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Let's see with an example :
        
userId = [1,2,3,4,5,6,7,8,9,10]

while(i := len(userId)) > 0:
    print(userId.pop())