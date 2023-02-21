import requests
from bs4 import BeautifulSoup

# res = requests.get("https://news.ycombinator.com/")
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select(".titleline")
# subline = soup.select('.subline')

# links_test = soup.select('div.titleline')

# def create_custon_hn(links,subline):
#     hn = []

#     for idx,item in enumerate(links):
#         title = links[idx].getText()
#         a_tag = links[idx].find("a")
#         href = a_tag["href"]
#         vote = subline[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points',''))
#             print(points)
#             hn.append({'title': title, 'link': href})
#     return hn


# print(create_custon_hn(links,subline))

res = requests.get("https://news.ycombinator.com/news")
print(res)