import datetime
from datetime import date
birth = datetime.datetime(2000, 7, 17)

tdate = datetime.datetime.today()

age = tdate.year - birth.year
print("my age is :" + str (age))
