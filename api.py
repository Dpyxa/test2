import requests
# import json

responce = requests.get('https://randomuser.me/api')

data = responce.json()

print (responce.text)
