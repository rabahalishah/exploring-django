
import requests

endpoint = "http://localhost:8000/api/products/"

# response_data = requests.get(endpoint)

response_data = requests.get(endpoint)


print(response_data.json())
