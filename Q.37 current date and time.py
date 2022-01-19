
## current date and time:-

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d-%m-%y %I:%M"))



## current date,time and second:-


import time
lt = time.localtime()
days = lt.tm_mday
years = lt.tm_year
month = lt.tm_mon
hours = lt.tm_hour
min = lt.tm_min
sec = lt.tm_sec
print(days,month,years, sep="/")
print (hours,min,sec,sep=":")

