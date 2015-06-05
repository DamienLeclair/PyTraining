__author__ = 'dleclair'

import time

print(time.time())

start = time.time()
time.sleep(0.5)
stop = time.time()

print(start < stop)

local_time = time.localtime()
print(local_time)

timestamp = time.mktime(local_time)
print(timestamp)

print(time.strftime('%Y'))
print(time.strftime("%A %d %B %Y %H:%M:%S"))

import datetime

date = datetime.date(2010, 12, 25)
print(date)

today = datetime.date.today()
print(today)
today = datetime.date.fromtimestamp(time.time())
print(today)

print(datetime.datetime.now())  # get hours

