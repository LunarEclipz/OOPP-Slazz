import datetime as dt

timeNow = dt.datetime.now().strftime("%Y-%m-%d")

d = dt.timedelta(days=14)
timeNow2 = dt.datetime.strptime(timeNow, "%Y-%m-%d")
u = timeNow2 + d
print(u)


