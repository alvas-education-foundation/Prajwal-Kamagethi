import os
import time 
while True:
 if os.path.exists("Fruits.txt"):
  print("File does not exist")
  break
 else:
  with open("Fruits.txt","x") as new_my_file:
   new_my_file.write("Mangoes")
   data = new_my_file.read()
   print(data)
   sleep(2)
