import requests
from bs4 import BeautifulSoup

res = requests.get("https://memoryleaks.ir")
#print(res.text)
soap = BeautifulSoup(res.text, 'html.parser')

a_tags = soap.find_all('a')
print(a_tags)

for a_tag in a_tags:
    print(a_tag.get('href'))