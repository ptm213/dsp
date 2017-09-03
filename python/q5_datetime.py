# Hint:  use Google to find python function

####a) 
import datetime
date_start = '01-02-2013' #month - day - year
date_stop = '07-28-2015'

dates = [x.split('-') for x in [date_start, date_stop]] # Dates in list

dates = [list(map(int, x)) for x in dates] # Change value types to integers

dates = [datetime.date(x[2], x[0], x[1]) for x in dates] # Transform to datetime format
daysA = abs(dates[1]-dates[0]) # Difference between dates in days

print(daysA.days)


####b)  
import time

date_start = '12312013'
date_stop = '05282015'

startB = int(date_start)
stopB = int(date_stop)

def start_to_stop_epoch(date_start, date_stop):
    epoch_dates = [int(x) for x in [date_start, date_stop]] # convert to epoch integer

    tuple_dates = [time.gmtime(x) for x in epoch_dates] # convert epoch to tuple time format

    string_dates = [time.strftime("%Y %m %d %H %M %S", x) for x in tuple_dates] # convert to string format
    #print(string_dates)
    split_dates = [x.split(' ') for x in string_dates]

    int_dates = [list(map(int, x)) for x in split_dates]

    dates = [datetime.datetime(x[0], x[1], x[2], x[3], x[4], x[5]) for x in int_dates]
    
    print(abs(dates[1]-dates[0]))

start_to_stop_epoch(startB, stopB)


####c)  
import calendar

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

# convert start/stop to usable format
startC = time.strptime(date_start, '%d-%b-%Y')
stopC = time.strptime(date_stop, '%d-%b-%Y')

# convert start/stop dates to epoch time format
startC = calendar.timegm(startC)
stopC = calendar.timegm(stopC)

start_to_stop_epoch(startC, stopC) # call previously definied function
