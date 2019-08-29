import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(response.text)
print(data["joke"])
# print(f"status: {data['status']}")
