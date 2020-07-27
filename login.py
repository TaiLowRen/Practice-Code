selection = input("Enter 1 to login, 2 to make account: ") #takes user input
if selection == "1": #Login
    username = input("Enter username:") #takes user input
    password = input("Enter password:")
    f = open('passwords.txt')
    Flag = 0 
    for i in f.read().split('\n'): #iterates through the passwords.txt file, checks if the password entered has been saved to the passwords.txt file
        if password == i:
            Flag = 1
    if Flag == 1:
        print('Welcome')
    else:
        print("Incorrect Password")

elif selection == "2": #Creation
    username = input("Enter new username:")#takes user input
    password = input("Enter new password:")
    f = open("usernames.txt", "r") 
    Flag = 0 
    for i in f.read().split('\n'): #iterated through the usernames.txt file, checks if the username is taken
        if username == i:
            Flag = 1
    if Flag == 1:
        print('Username already exists')
        f.close
    else:
        f = open("usernames.txt", "a")
        f.write(username + "\n")
        f.close
        q = open("passwords.txt", "a")
        q.write(password + "\n")
        q.close


