name = input("Enter your name: ")
surname = input("Enter your surname: ")

message = "Hello %s %s" % (name, surname)  #python 2&3
message1 = f"Hello {name} {surname}. What's up?"

print(message)
print(message1)
