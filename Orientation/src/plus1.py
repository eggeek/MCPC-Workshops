from datetime import datetime
from time import sleep

def func(a, b):
  s = datetime.now()
  sleep(a)
  sleep(b)
  e = datetime.now()
  return e.second - s.second
