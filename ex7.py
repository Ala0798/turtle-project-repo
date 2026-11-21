import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # Conversie din JSON într-un obiect Python
    print(posts)
else:
    print("Eroare la cerere!")