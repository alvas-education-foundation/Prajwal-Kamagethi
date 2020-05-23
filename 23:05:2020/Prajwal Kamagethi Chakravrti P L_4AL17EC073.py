#Write python code to verify user_name = "Micheal" and password ="e3$WT89x". 
#The total number of attempts are 03.
# For every wrong user_name and password Print - Invalid username or Password,
# upon three attempts fails print- Account locked

attempts = 0
while attempts < 3:
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    if user_name=="Micheal" and password=='e3$WT89x':
        print('Logged in successfully')
        break
    else:
        print('Invalid Username or password. Try again.')
    attempts = attempts + 1
    if attempts == 3 :
        print("Account Locked")
