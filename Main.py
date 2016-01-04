import requests
import time
import calendar
from bs4 import BeautifulSoup

f1 = open('results.txt', 'a+')  # file used to store the results
f2 = open('source.txt', 'a+')  # file used to get the starting url
f3 = open('seen.txt', 'a+')  # file used to store the visited urls
links = []
visitedlinks = []


def calculatedate(date):
    totdays = 0
    if date[0] == 'P':
        newdate = date[14:]  # erasing "Pubblicato il "

    elif date[0] == 'C':
        newdate = date[12:]  # erasing "Caricato il "

    day = int(newdate[:2])  # extracting number of the day
    Wmonth = newdate[3:6]  # extracting number of days from the past months
    if (Wmonth == 'gen') or (Wmonth == 'Jan'):
        month = 00
    elif (Wmonth == 'feb') or (Wmonth == 'Feb'):
        month = 31
    elif (Wmonth == 'mar') or (Wmonth == 'Mar'):
        month = 59
    elif (Wmonth == 'apr') or (Wmonth == 'Apr'):
        month = 90
    elif (Wmonth == 'mag') or (Wmonth == 'May'):
        month = 120
    elif (Wmonth == 'giu') or (Wmonth == 'Jun'):
        month = 151
    elif (Wmonth == 'lug') or (Wmonth == 'Jul'):
        month = 181
    elif (Wmonth == 'ago') or (Wmonth == 'Aug'):
        month = 212
    elif (Wmonth == 'set') or (Wmonth == 'Sep'):
        month = 243
    elif (Wmonth == 'ott') or (Wmonth == 'Oct'):
        month = 273
    elif (Wmonth == 'nov') or (Wmonth == 'Nov'):
        month = 304
    elif (Wmonth == 'dic') or (Wmonth == 'Dec'):
        month = 334
    year = int(newdate[7:11])  # extracting year

    if (calendar.isleap(year)) and (month > 31):
        month += 1

    year = (year - 2005)            # subracted the year when youtube came to the great world of internet and coverted
    moredaysforme = year / 4        # counting bissextile years from 2005 to the year before this
    year = year * 365 + moredaysforme   # this conversion is not optimized for all the non-bissextile years
    days = (day + month + year)  # total number of days from the day christ was born
                                    # till the day the video was uploaded on youtube
    return days

def calculateaverage(date, views):
    chargeddate = calculatedate(date)
    today = calculatedate(time.strftime("%d/%b/%Y"))
    totaldays = today - chargeddate
    averageviews = views / totaldays
    print (averageviews)
    return averageviews

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
                print(title1)
                f1.write("Title: " + title1 + "\n")  # writing on results.txt

            # finding the date of the video
            for date in soup.findAll("strong", {'class': 'watch-time-text'}):
                date1 = date.string
                f1.write("date: " + date1 + "\n")  # writing on results.txt

            # finding the number of views of the video
            for views in soup.findAll("div", {'class': 'watch-view-count'}):
                views1 = views.string
                f1.write("Views: " + views1 + "\n")  # writing on results.txt
                averageviews = calculateaverage(date1, views1)
                f1.write("Average views per day: " + str(averageviews) + "\n")
                print(str(averageviews))
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
for url1 in f2.readlines():  # setting up the list of the urls to be seen
    links.append(url1)

f3.seek(0)  # setting the pointer at the begin of the file (normally using 'a+' mode sets the pointer at the end)
for url2 in f3.readlines():  # setting up the list of the visited links
    if url2 not in visitedlinks:
        visitedlinks.append(url2)

crawler(5)  # starting the crawler
f1.close()  # closing streams
f2.close()
f3.close()
