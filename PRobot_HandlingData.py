import time
import calendar
import urllib.request
import os


f4 = open('log.txt', 'a')  # the file log is used to store the time spent for the execution


# function used to convert the date from string format to number of days
def calculatedate(date):
    month = 0

    if date[0] == 'P':
        newdate = date[14:]  # removing "Pubblicato il "

    elif date[0] == 'C':
        newdate = date[12:]  # removing "Caricato il "
    else:
        newdate = date
    day = int(newdate[:2])  # extracting number of the day
    wmonth = newdate[3:6]  # extracting number of days from the past months
    if (wmonth == 'gen') or (wmonth == 'Jan'):
        month = 00
    elif (wmonth == 'feb') or (wmonth == 'Feb'):
        month = 31
    elif (wmonth == 'mar') or (wmonth == 'Mar'):
        month = 59
    elif (wmonth == 'apr') or (wmonth == 'Apr'):
        month = 90
    elif (wmonth == 'mag') or (wmonth == 'May'):
        month = 120
    elif (wmonth == 'giu') or (wmonth == 'Jun'):
        month = 151
    elif (wmonth == 'lug') or (wmonth == 'Jul'):
        month = 181
    elif (wmonth == 'ago') or (wmonth == 'Aug'):
        month = 212
    elif (wmonth == 'set') or (wmonth == 'Sep'):
        month = 243
    elif (wmonth == 'ott') or (wmonth == 'Oct'):
        month = 273
    elif (wmonth == 'nov') or (wmonth == 'Nov'):
        month = 304
    elif (wmonth == 'dic') or (wmonth == 'Dec'):
        month = 334
    year = int(newdate[7:11])  # extracting year

    if (calendar.isleap(year)) and (month > 59):
        month += 1

    year = (year - 2005)
    extradays = year // 4           # counting bissextile years from 2005 to the year before this
    year = year * 365 + extradays   # this conversion is not optimized for all the non-bissextile years
    days = (day + month + year)
    return days


# function used to "clean" the number of views removing dots ("12.345.678") and words ("874 visualizzazioni")
def convertviews(views):
    strviews = views.replace(".", "")
    try:
        intviews = int(strviews)
    except:
        count = 0
        for i in strviews:
            count += 1
            if i == " ":
                spazio = count - 1
        intviews = int(strviews[:spazio])
    return intviews


# function used to calculate the average number of views per day
def calculateaverage(date, views):
    intviews = convertviews(views)
    uppeddate = calculatedate(date)
    today = calculatedate(time.strftime("%d/%b/%Y"))
    totaldays = today - uppeddate
    averageviews = intviews / totaldays
    return averageviews


# function used to download the image preview of the video
def downloadimage(url, title, start, iterdone):
    try:
        resource = urllib.request.urlopen(url)
    except:
        counter(start, iterdone)
        print("Connection lost. Please retry later.")
        exit(1)
    directory = "images/"
    # check if the directory images is missing or not
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    title1 = title.replace('?', '')         # substituting unallowed characters in file names
    title2 = title1.replace('/', '')
    title3 = title2.replace(':', '')
    title4 = title3.replace('*', '')
    title5 = title4.replace('<', '')
    title6 = title5.replace('>', '')
    title7 = title6.replace('|', '')
    title8 = title7.replace('"', '')
    title9 = title8.replace("'", "")
    title10 = title9.replace(chr(92), "")   # char(92) == " \ "
    path = directory + title10 + ".jpg"
    output = open(path, "wb")
    output.write(resource.read())
    output.close()
    return path


# function used to check if source.txt is empty or missing
def checksource():
    if os.stat('source.txt').st_size == 0:
        f1 = open('source.txt', 'a+')  # file used to store the results
        f1.write('https://www.youtube.com/watch?v=vabnZ9-ex7o' + "\n")


# function used to write the total time of execution
def counter(start, numbers):
    now = time.time()
    timetook = now - start
    mins = timetook // 60
    hour = mins // 60
    minutes = mins % 60
    seconds = timetook % 60
    milliseconds = (seconds % 1) * (10 ** 3)
    seconds = seconds // 1
    iterdone = numbers[0]
    alliter = numbers[1]
    f4.write("The execution of " + str(iterdone) + " video analyzed and " + str(alliter) + " iteration took : ")
    if hour != 0:
        f4.write(str(int(hour)) + "h ")
    if minutes != 0:
        f4.write(str(int(minutes)) + "m ")
    if seconds != 0:
        f4.write(str(int(seconds)) + "s ")
    if milliseconds != 0:
        f4.write(str(int(milliseconds)) + "ms \n")
