# use json to do json encoding and decoding
import json

car_data = {"name":"tesla", "engine": "electric"}

# to confirm, it's a dict
print(type(car_data))

#json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# this is how we can we can encode from a dictionary and write to a file
with open ('new_json_file.json', 'w') as jsonfile: # w gives write permission
    json.dump(car_data, jsonfile)
    
    
with open('new_json_file.json') as jsonfile:
    car = json.load(jsonfile) # load() copies the data and stores into a variable
    print(type(car))
    print(car['engine'])
    print(car['name'])