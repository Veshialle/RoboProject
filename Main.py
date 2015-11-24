import requests
from bs4 import BeautifulSoup


f1 = open('results.txt', 'w')
f2 = open('sources.txt', 'r+')
links = []

for url in f2.readlines():
    links.append(url)

def crawler(maxite):
    count = 1
    if count == 1:
        f1.write("---------- VISITED VIDEOS ----------\n\n")
    for url in links:
        #print(url)
        if count == maxite:
            print("done!")
            break
        source_code = requests.get(str(url))
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for title in soup.findAll("span", {'id': 'eow-title'}, {'class': 'watch-title'}):
            title1 = title.get('title')
            print(title1)
            f1.write("Title: " + title1 + "\n")

        for date in soup.findAll("strong", {'class': 'watch-time-text'}):
            date1 = date.string
            print(date1)
            f1.write("date: " + date1 + "\n")

        for views in soup.findAll("div", {'class': 'watch-view-count'}):
            views1 = views.string
            print(views1)
            f1.write("Views: " + views1 + "\n")
        f1.write("\n \n")

        for link in soup.findAll('a', {'class': 'yt-uix-sessionlink  content-link spf-link        spf-link '}):
            link1 = "https://www.youtube.com" + link.get('href')
            links.append(link1)
            print(link1)

        count += 1


crawler(10)
f1.close()
f2.close()
