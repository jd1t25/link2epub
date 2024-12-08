from bs4 import BeautifulSoup as bs
import requests

url = "https://novelbin.me/novel-book/shadow-slave#tab-chapters-title"
api_url = "https://novelbin.me/ajax/chapter-archive?novelId=shadow-slave"
result = requests.get(url)

doc = bs(result.text, "html.parser")

print(doc)
