import requests
import PRobot_HandlingData
import time
from bs4 import BeautifulSoup
start = time.time()
f1 = open('results.txt', 'a+', encoding='utf8' )  # file used to store the results
f2 = open('source.txt', 'a+')  # file used to get the starting url
f3 = open('seen.txt', 'a+')  # file used to store the visited urls
f4 = open('log.txt', 'a') #the file log is used to store the time spent for the execution
links = []
visitedlinks = []

def crawler(maxite):
    count = 0
    for url in links:
        if count == maxite:  # if i reached the max number of iterations
            print("\nDone!")
            break
        if url not in visitedlinks:  # == if i've not seen the video yet
            visitedlinks.append(url)
            f3.write(url + "\n")
            source_code = requests.get(str(url))
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")

            # finding the title of the video
            for title in soup.findAll("span", {'id': 'eow-title'}, {'class': 'watch-title'}):
                title1 = title.get('title')
                f1.write("Title: " + title1 + "\n")  # writing on results.txt
            # finding the date of the video
            for date in soup.findAll("strong", {'class': 'watch-time-text'}):
                date1 = date.string
                f1.write("date: " + date1 + "\n")  # writing on results.txt

            # finding the number of views of the video
            for views in soup.findAll("div", {'class': 'watch-view-count'}):
                views1 = views.string
                f1.write("Views: " + views1 + "\n")  # writing on results.txt
                averageviews = PRobot_HandlingData.calculateaverage(date1, views1)
                f1.write("Average views per day: " + str(averageviews) + "\n")
            #downloading the preview of the video
            for img in soup.findAll('meta',{'property': "og:image"}):
                img1 = img.get('content')
                path = PRobot_HandlingData.downloadimage(img1, title1)
                f1.write("Directory and name of the downloaded image: " + path + "\n")
            f1.write("Link del video: " + url + "\n")
            f1.write("\n \n")

            # finding all the links of the correlated videos
            for link in soup.findAll('a', {'class': 'yt-uix-sessionlink  content-link spf-link        spf-link '}):
                link1 = "https://www.youtube.com" + link.get('href')
                if link1 not in visitedlinks:  # checking if the link has already been visited
                    links.append(link1)        # if not, add it to the list
                    f2.write("\n" + link1)       # and write it on the source file


        elif url in visitedlinks:
            maxite += 1

        count += 1


f1.seek(0)
f2.seek(0)
#initializing the source.txt file in case of the empty (or inexistent) file
PRobot_HandlingData.checksource()

for url1 in f2.readlines():  # setting up the list of the urls to be seen
    links.append(url1)
PRobot_HandlingData.checksource()
f3.seek(0)  # setting the pointer at the begin of the file (normally using 'a+' mode sets the pointer at the end)
for url2 in f3.readlines():  # setting up the list of the visited links
    if url2 not in visitedlinks:
        visitedlinks.append(url2)
iteration = 30000
crawler(iteration) # starting the crawler
f1.close()  # closing streams
f2.close()
f3.close()
f4.write(PRobot_HandlingData.counter(start, time.time() , iteration))

