import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.thehindu.com")
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('.label'))