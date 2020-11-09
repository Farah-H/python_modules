# Let's have  a look at some built in functions 
# import is the key word we use to call modules from Python library


# first iteration
import math
import random
# we have a random method in python library wchich we use by importing
 
print(random.random())
# this generates a float between 0-1

num_float = 23.44
print("floor method rounds the figure to the lower figure")
print(math.floor(num_float))

print('ceiling method rounds the figure to higher end of the value')
print(math.ceil(num_float))

# Task 
# get user input of a float number
number = input('What number would you like to round?')
print(round(float(number),0))