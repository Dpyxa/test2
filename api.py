import requests

responce = requests.get('https://randomuser.me/api/?results=10')

data = responce.json()
