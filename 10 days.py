from datetime import datetime, timedelta, time
# Today's Date
dt = datetime.now()
# For 10 dates 7days apart
for x in range(10):
    print(x+1, "-", end='  ')
    print(dt.strftime('%y/ %m/ %d - %H:%M'))
    dt = dt + timedelta(days=7)
