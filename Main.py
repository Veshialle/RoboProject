import requests
from bs4 import BeautifulSoup


f1 = open('results.txt', 'w')
f2 = open('source.txt', 'r')
f3 = open('seen.txt', 'a+')
links = []
visitedlinks = []


def crawler(maxite):
    count = 0
    if count == 0:
        f1.write("---------- VISITED VIDEOS ----------\n\n")
    for url in links:
        if count == maxite:
            print("Done! I visited " + str(maxite) + " videos")
            break
        if (url + "\n") not in visitedlinks:
            print(visitedlinks)
            visitedlinks.append(url)
            f3.write(url)
            f3.write("\n")
            source_code = requests.get(str(url))
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            for title in soup.findAll("span", {'id': 'eow-title'}, {'class': 'watch-title'}):
                title1 = title.get('title')
                print(title1)
                f1.write("Title: " + title1 + "\n")

            for date in soup.findAll("strong", {'class': 'watch-time-text'}):
                date1 = date.string
                f1.write("date: " + date1 + "\n")

            for views in soup.findAll("div", {'class': 'watch-view-count'}):
                views1 = views.string
                f1.write("Views: " + views1 + "\n")
                f1.write("\n \n")

            for link in soup.findAll('a', {'class': 'yt-uix-sessionlink  content-link spf-link        spf-link '}):
                link1 = "https://www.youtube.com" + link.get('href')
                if link1 not in visitedlinks:
                    links.append(link1)

        count += 1


for url1 in f2.readlines():
    links.append(url1)

f3.seek(0)
for url2 in f3.readlines():
    if url2 not in visitedlinks:
        visitedlinks.append(url2)

crawler(3)
f1.close()
f2.close()
f3.close()
