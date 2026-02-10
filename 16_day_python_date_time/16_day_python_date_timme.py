# Python has got datetime module to handle date and time
import datetime

print(dir(datetime))

now = datetime.datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(day, month, year, hour, minute, second, timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")
print("time:", time)

# American format
american_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print("american format:", american_format)

world_format = now.strftime("%d/%m/%Y, %H:%M:%S")
print("world format:", world_format)

date_string = "5 December, 2026"
print("date_string:", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

from datetime import date

date_example = date(2026, 1, 1)
print(date_example)
print("current date:", date_example.today())

today = date.today()
print("Currenct year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import time

a = time()
print("a =", a)

b = time(10, 30, 50)
print("b =", b)

c = time(hour=10, minute=30, second=50)
print("c = ", c)

d = time(10, 30, 50, 200555)
print("d = ", d)

from datetime import date, datetime
today = date(year=2020, month=12, day=5)
new_year = date(year=2021, month=1, day=1)

time_left_for_newyear = new_year - today
print(time_left_for_newyear)

date_one = datetime(year= 2020, month= 12, day= 5, hour = 0, minute = 32, second = 0)
date_two = datetime(year= 2021, month= 1, day = 1, hour = 0, minute = 0, second = 0)

difference = date_two - date_one
print("Time left for new year:", difference)

from datetime import timedelta

date_one = timedelta(weeks=12, days=10, hours=4, seconds=20)
date_two = timedelta(days=7, hours=5, minutes=3, seconds=30)

difference = date_two - date_one
print(difference)