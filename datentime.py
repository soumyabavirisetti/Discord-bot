import datetime
from pytz import timezone
import calendar

def find_date():
  tz = timezone("Asia/Kolkata")
  x = datetime.datetime.now(tz)
  return x.strftime("%d-%m-%Y")

def find_time():
  tz = timezone("Asia/Kolkata")
  x = datetime.datetime.now(tz)
  return x.strftime("%H:%M:%S")

def find_year():
  tz = timezone("Asia/Kolkata")
  x = datetime.datetime.now(tz)
  return x.strftime("%Y")

def find_month():
  tz = timezone("Asia/Kolkata")
  x = datetime.datetime.now(tz)
  return x.strftime("%B")

def find_day():
  tz = timezone("Asia/Kolkata")
  x = datetime.datetime.now(tz)
  return x.strftime("%A")


