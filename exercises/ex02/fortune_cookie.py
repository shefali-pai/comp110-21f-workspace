"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730466264"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint

# Begin your solution here...
print("Your fortune cookie says...")
a = randint(1, 4)
if a == 1:
    print("You have a very bright future ahead of you!")
else:
    if a == 2:
        print("You are going to make someone very happy soon!") 
    else:
        if a == 3:
            print("You are going to earn a fortune soon!") 
        else:
            print("You are going to be living your best life very soon!") 
print("Now, go spread positive vibes!")