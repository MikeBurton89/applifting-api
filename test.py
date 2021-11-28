import requests
import json

products = {'id': '5', 'name': 'cacca', 'description': 'cose'}

BASE = 'http://127.0.0.1:5000/products/'

response = requests.post(
    BASE, data=json.dumps(products))
print(response.json())
