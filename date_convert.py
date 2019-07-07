datea='16-02-2016 11:22'
dateb='16-02-2016 11:27'
# d=date2-date1

def convert_date(stg):
	date=(stg.split()[0]).strip().split('-')
	time=stg.split()[1]
	print date,time
	new_format="%s-%s-%s %s"%(date[2],date[1],date[0],time)
	return new_format
convert_date(datea)

date1=convert_date(datea)
date2=convert_date(dateb)

import datetime
from datetime import timedelta

datetimeFormat = '%Y-%m-%d %H:%M'#:%S.%f'
# date1 = '2016-04-10 10:01'#:28.585'
# date2 = '2016-04-12 09:56'#:28.067'
diff = datetime.datetime.strptime(date2, datetimeFormat) - datetime.datetime.strptime(date1, datetimeFormat)
 
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)


# https://www.pythonprogramming.in/date-time.html