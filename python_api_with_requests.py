# error code = 404 
# success code = 200
# package helps us use the code, we can connect. it allows us to scrape the web
import requests
import emoji

live_response = requests.get('https://www.bbc.co.uk')
# provides an integer as a response code 

if live_response.status_code == 200:
    print('mission accomplished!')
    print(emoji.emojize(":thumbs_up:"))
print(live_response.status_code)
# 200 : means the website is live 

print(live_response.content)

# First Iteration
if live_response.status_code == 200:
    print('mission accomplished!')
    print(emoji.emojize(":thumbs_up:"))
elif live_response.status_code == 404:
    print('Website not found.')
else:
    print('OOPS! Something went wrong, please try later.')

# Second iteration
def check_status_code():
    if live_response.status_code:
        print('mission accomplished!')
        print(emoji.emojize(":thumbs_up:"))
    elif live_response.status_code:
        print('Website not found.')
    else:
        print('OOPS! Something went wrong, please try later.')

# requests module by default gives boolean for success / failure
# wil evaluate to true if code is 200-404, otherwise False 