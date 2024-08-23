import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
content1 = soup.select('.titleline>a')
subtext1 = soup.select('.subtext')
content2 = soup2.select('.titleline>a')
subtext2 = soup2.select('.subtext')
total_content = content1 + content2
total_subtext = subtext1 + subtext2

def customize(content, subtext):
    hn=[]
    for i,item in enumerate(content):
        title = content[i].getText()
        points = subtext[i].select('.score')
        # points doesnt have a long list, It will always get replaced when the new loop happens the position of the points become points[0] again.
        link = content[i].get('href', 'none')
        if len(points):
            point = int(points[0].getText().replace(' points',' '))
        if (point>99):
            hn.append({'title': title, 'votes': point, 'link': link})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

pprint(print(customize(total_content,total_subtext)))
