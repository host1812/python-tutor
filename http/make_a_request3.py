import requests
from random import choice

def search_jokes(topic):
    
    url = "https://icanhazdadjoke.com/search"
    headers = {"Accept": "application/json"}
    params = {"term": topic,
              "limit": 20}

    data = requests.get(url, headers = headers, params = params).json().get('results')
    # print(data)
    return(data)

def show_header():
    print("HEADER")

def main():
    show_header()
    topic = input("Enter the topic: ")

    results = search_jokes(topic)

    print(f"There was {len(results)} jokes.")
    if results:
        print(f"Here is one of them: {choice(results).get('joke')}")

if __name__ == "__main__":
    main()