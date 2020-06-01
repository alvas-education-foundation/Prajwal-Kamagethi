my_file = open("fruits.txt")
content = my_file.read()
my_file.close()
#my_file.read()
with open("fruits.txt") as my_file:
 content =my_file.read()
print(content)
