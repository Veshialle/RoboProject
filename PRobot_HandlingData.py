import time
import calendar

def calculatedate(date):
    month = 0
    newdate = 0
    print(date)

    if date[0] == 'P':
        newdate = date[14:]  # erasing "Pubblicato il "

    elif date[0] == 'C':
        newdate = date[12:]  # erasing "Caricato il "
    else:
        newdate = date
    print(newdate)
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
    moredaysforme = year // 4        # counting bissextile years from 2005 to the year before this
    year = year * 365 + moredaysforme   # this conversion is not optimized for all the non-bissextile years
    days = (day + month + year)  # total number of days from the day christ was born
                                    # till the day the video was uploaded on youtube
    return days
def convertviews(views):
    intviews = 0
    cont = 0
    for i in views:
        if i != ".":
            intviews += int(i) * (10**cont)         #converted the string with dot to a mirror number
            cont += 1
    strviews = str(intviews)
    print(strviews)
    cont1 = 0
    intviews = 0
    for x in strviews:
        intviews += int(x) * (10**cont1)            #re mirrored the number of views
        cont1 += 1
    print(views)
    return intviews

def calculateaverage(date, views):
    intviews = convertviews(views)
    chargeddate = calculatedate(date)
    today = calculatedate(time.strftime("%d/%b/%Y"))
    totaldays = today - chargeddate
    averageviews = intviews / totaldays
    print(averageviews)
    return averageviews


