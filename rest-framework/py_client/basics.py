import requests


# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# response_data = requests.get(endpoint)
response_data = requests.post(endpoint, json={"title": "NEw product", "content":"new content"})

print(response_data.json())

# here params are query params http://localhost:8000/api/?abc=123
