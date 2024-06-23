import requests

endpoint = "http://localhost:8000/api/products/"

# response_data = requests.get(endpoint)
data = {
    "title": "Product withou content. This will be the content too"
}
response_data = requests.post(endpoint, json=data)


print(response_data.json())
