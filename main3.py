import time
password = 0
name = 0
date = 0
pass_to_site = False
id = 0
tries = 3
counter = 0
tr = True
while tr:
    if counter == 3:
        break
    else:
        pass
    a = input("login or register?")
    if a == "login":
        while tries :
            userlog = input("enter your name ")
            if userlog == id:
                pass_to_site = True
                tries = 0
            else:
                tries -= 1
                if tries == 0:
                    time.sleep((counter +1)*4)
                    print((counter +1)*4)
                    counter += 1
                    if counter == 3:
                        print("you are banned")
                        break
                    tries = 3
    elif a == "register":
        password = input("enter your password: ")
        name = input("enter your name: ")
        date = input("enter your date of birth: ")
        pass_to_site = True
        save = input("wanna save your id? y/n?")
        if save == "y":
            id = name
        else:
            pass
    else:
            pass
    if pass_to_site == True:
        print("Welcome to your page!")
        almfin = int(input("wanna exit and start again or just exit again? 1:2"))
        if almfin == 1:
            tr = True
        else:
            pass
