import time
import calendar
import urllib.request
import os

def calculatedate(date):
    month = 0
    newdate = 0

    if date[0] == 'P':
        newdate = date[14:]  # erasing "Pubblicato il "

    elif date[0] == 'C':
        newdate = date[12:]  # erasing "Caricato il "
    else:
        newdate = date
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

    if (calendar.isleap(year)) and (month > 59):
        month += 1

    year = (year - 2005)            # subracted the year when youtube came to the great world of internet and coverted
    moredaysforme = year // 4        # counting bissextile years from 2005 to the year before this
    year = year * 365 + moredaysforme   # this conversion is not optimized for all the non-bissextile years
    days = (day + month + year)  # total number of days from the day christ was born
                                    # till the day the video was uploaded on youtube
    return days
def convertviews(views):
    intviews = int(views.replace(".",""))
    return intviews

def calculateaverage(date, views):
    intviews = convertviews(views)
    chargeddate = calculatedate(date)
    today = calculatedate(time.strftime("%d/%b/%Y"))
    totaldays = today - chargeddate
    averageviews = intviews / totaldays
    return averageviews


def downloadimage(url, title):
    resource = urllib.request.urlopen(url)
    directory = "images/"
    #ceck of the directory images
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    title1 = title.replace('?', '')
    title2 = title1.replace('/', '')
    title3 = title2.replace(':', '')
    title4 = title3.replace('*', '')
    title5 = title4.replace('<', '')
    title6 = title5.replace('>', '')
    title7 = title6.replace('|', '')
    title8 = title7.replace('"', '')
    title9 = title8.replace("'", "")
    path = directory + title9 + ".jpg"
    output = open(path, "wb")
    output.write(resource.read())
    output.close()
    return path

def checksource():
    if os.stat('source.txt').st_size == 0:
        f1 = open('source.txt', 'a+')  # file used to store the results
        f1.write('https://www.youtube.com/watch?v=vabnZ9-ex7o' + "\n")
'''
def checkstring(string):
    try:
        string.decode('utf-8')
        print("string is UTF-8, length %d bytes" % len(string))
    except UnicodeError:
        print("string is not UTF-8")
'''