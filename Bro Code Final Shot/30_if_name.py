# if __name__ == __main__ is used in our program standalone or can be imported as well!

from random import *

def main():
    return randint(1,4)


if __name__ == '__main__':
    print(main())