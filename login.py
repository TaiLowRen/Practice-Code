


selection = input("Enter 1 to login, 2 to make account: ")
if selection == "1": #Login
    username = input("Enter username:")
    password = input("Enter password:")

elif selection == "2": #Creation
    username = input("Enter new username:")
    password = input("Enter new password:")
    f = open("saves.txt", "a")
    f.write("Username: " + username)
    f.write(" ")
    f.write("Password: " + password + "\n")
    f.close
