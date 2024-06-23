

import requests

endpoint = "http://localhost:8000/api/products/1"

# response_data = requests.get(endpoint)

response_data = requests.get(endpoint)


print(response_data.json())
