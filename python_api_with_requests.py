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