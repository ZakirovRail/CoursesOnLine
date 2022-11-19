import datetime

print(datetime.date(year=2016, month=1, day=6))  # 2016-01-06
print(datetime.date.today())
print(datetime.date.fromtimestamp(1000000000))  # 2001-09-09
print(datetime.date.fromordinal(720669))  # 1974-02-15

print(datetime.date.today() - datetime.date(year=1974, month=2, day=15))  # 17382 days, 0:00:00

d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)
print(d.weekday())  # in 'USA' format
print(d.isoweekday())  # in ISO format
print(d.isoformat())  # 2021-09-18
print(d.strftime('%A %d %B %Y'))  # Saturday 18 September 2021
print('The date is {:%A %d %B %Y}'.format(d))  # The date is Saturday 18 September 2021
print('{date:%A} {date.day} {date:%B} {date.year}'.format(date=d))  # Saturday 18 September 2021






