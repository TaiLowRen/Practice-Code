selection = input("Enter 1 to login, 2 to make account: ")
if selection == "1": #Login
    username = input("Enter username:")
    password = input("Enter password:")
    f = open('passwords.txt')
    Flag = 0 
    for i in f.read().split('\n'):
        if password == i:
            Flag = 1
    if Flag == 1:
        print('Welcome')
    else:
        print("Incorrect Password")

elif selection == "2": #Creation
    username = input("Enter new username:")
    password = input("Enter new password:")
    f = open("usernames.txt", "r")
    Flag = 0 
    for i in f.read().split('\n'):
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


