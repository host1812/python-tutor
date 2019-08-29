import requests

response = requests.get("https://news.ycombinator.com/")

print(response.headers)

print(response.text)
