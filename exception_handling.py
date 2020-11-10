# we will have a look at the practice use acases and implementation of try, except, raise and finally


# we wil create a variable to store file data using open()
try:
    file = open('orders.text')
except FileNotFoundError as errmssg: # creating an alias for file not found error in except block
    print('Alert something went wrong' + str(errmssg))

# if we still wanted to see the actual exception together with our customised message
    raise

finally: # finally will execute regardless of the above conditions
    print('Hope you had a good customer experience, please visit again.')