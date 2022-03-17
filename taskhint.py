def register():
    print("I am the register function")
    # ask him about his information

    # save the to file

def login():
    print("I am the login")
    #ask him about username and password

    #check if username and password in the file or not


def mainfunction():
    choice = input("Plz enter your choice l or r ")
    if choice =="l"or choice=="r":
        if choice=="l":
            return login()
        else:
           return register()

    return mainfunction()

mainfunction()