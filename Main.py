import requests
from bs4 import BeautifulSoup


f1 = open('data.txt', 'w')
f2 = open('sources.txt', 'r')
links = []

for url in f2.readlines():
    links.append(url)

def crawler(maxite):
    count = 1
    while 1:
        if count == 1:
            f1.write("---------- VISITED VIDEOS ----------\n\n")
        for url in links:
            print(url)
            #url = "https://www.youtube.com/watch?v=vabnZ9-ex7o"
            source_code = requests.get(str(url))
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            for title in soup.findAll("span", {'id': 'eow-title'}, {'class': 'watch-title'}):
                title1 = title.get('title')
                f1.write("Title: " + title1 + "\n")

            for views in soup.findAll("div", {'class': 'watch-view-count'}):
                views1 = views.string
                f1.write("Views: " + views1 + "\n")

            for desc in soup.find('p', {'id': 'eow-description'}):
                desc1 = desc.string
                f1.write("Description: " + desc1 + "\n")
            f1.write("\n \n")


        if count == maxite:
            print("done!")
            break
        count += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)


crawler(1)
f1.close()
f2.close()
