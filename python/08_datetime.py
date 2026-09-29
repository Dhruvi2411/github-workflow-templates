import datetime
from datetime import date

date1 = datetime.time(2,30,30)
print(date1)

print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.today().ctime())

date1 = date(2021, 11, 3)
date2 = date(2021, 12, 6)
res = date2 - date1
print(res.days)

