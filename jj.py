import requests, sys

username = sys.argv[1]
url = 'https://api.github.com/users/{}/repos'. format(username)

res = requests.get(url)

#print(res.text)

for item in res.json():
    print(item.get('name'))