import time 
import os
import pandas

while True:
 if os.path.exists("original.csv"):
  data = pandas.read_csv("original.csv")
  print(data.mean()["st1"])
 else:
  print("The file does not exist")
 time.sleep(2)

