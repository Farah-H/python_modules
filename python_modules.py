# Let's have  a look at some built in functions 
# import is the key word we use to call modules from Python library


# # first iteration
# import math
# import random
# # we have a random method in python library wchich we use by importing
 
# print(random.random())= 
# # this generates a float between 0-1

# num_float = 23.44
# print("floor method rounds the figure to the lower figure")
# print(math.floor(num_float))

# print('ceiling method rounds the figure to higher end of the value')
# print(math.ceil(num_float))

# #TASK
# # Take user's input
# number = input('What number would you like to round?')
# # check that the user gave us a float
# if float(number) % 1 == 0 
#     number = (input('You must enter a float, please try again.'))
# # the built in round function already has this control flow
# else:
#     print(round(float(number),0))


# # this would work for linux machinee not windows 
# import os 
# # to find out system configuration or system related information
# # based on the information provided we can handle the user request
# import math, datetime, sys
# working_dir = os.get_cwd()
# print(os.working_dir)
# import os
# os.system("ECHO Hello")

# # let's count the number of CPUs 
# print(os.cpu_count())
# # gives total cpus in our system os 

# import datetime
# print(datetime.datetime.today())

# import sys

# print(sys.path)

# How can we create a customised method and utilise the built in function 
import sys
def system_path():
    print(sys.path)
# What is PIP? 
# PIP is a package manager