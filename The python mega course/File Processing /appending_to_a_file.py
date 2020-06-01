with open("Fruits.txt","a+") as my_file:
 my_file.write("\nGrapes")
 my_file.seek(0)
 data = my_file.read()
print(data)
