# importing necessary modules
import requests
import json

# url = 'http://api.postcodes.io/postcodes/'
# argument = input(" please enter you postcode")

# url_target = str(live_response) + argument

# live_response = requests.get(url_target)


# #print(live_response.content)

# #research how to convert this data into dictionary
# #HINT - python json library/module/method can be used to resolve this

# post_code_dictionary = live_response.json()
# #print(post_code_dictionary)

# #iterate through the data and print RESULTS
# def print_results(post_code_dictionary):
#     for key, value in post_code_dictionary.items():
#         # this is a way to loop through the nested dictionary 
#         if isinstance(value, dict) and key == 'result':
#             print(key)
#             print_results(value)
#         elif key == 'status':
#             continue
#         else:
#             print(f'{key}: {value}')


# print_results(post_code_dictionary)

# #print longitude and latitude (locations)
# print(f'Longitude = {post_code_dictionary["result"]["longitude"]}')
# print(f'Latitude = {post_code_dictionary["result"]["latitude"]}')


#Create a function that returns the longitude and latitude of the given postcode
def find_long_lat():
    url = 'http://api.postcodes.io/postcodes/'
    argument = input('Please enter you postcode')

    url_target = str(url) + argument

    live_response = requests.get(url_target)
    postcode_dic = live_response.json()

    print(postcode_dic['result']['longitude'])
    print(postcode_dic['result']['latitude'])
    

print(find_long_lat())
# print(live_response.status_code)

