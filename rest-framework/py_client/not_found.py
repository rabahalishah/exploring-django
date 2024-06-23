

import requests

endpoint = "http://localhost:8000/api/products/32648376437"

# response_data = requests.get(endpoint)

response_data = requests.get(endpoint)


print(response_data.json())
