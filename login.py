def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sign Up Type 1 and For Sign In Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError


def getdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("database.txt", 'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("database.txt", 'w')
    info = info + " " + name + " " + password
    f.write(info)


def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("database.txt", 'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Enter a valid username or Signup"


print(choices())
