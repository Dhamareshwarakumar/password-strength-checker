import re


def out(temp, strx):
    if len(temp) == 0:
        requiredarr.append("Atleast one "+strx+" is required")
    elif len(temp) == 1:
        suggestedarr.append("Minimum two "+strx+"s are advisable")
    else:
        pass


def lenchecker(password):
    if len(password) < 8:
        requiredarr.append("Password must have 8 characters")
    elif len(password) < 12:
        suggestedarr.append("minimum 12 character long password is advisable")
    else:
        pass


def passwordchecker(password):

    lenchecker(password)

    temp = re.findall("[a-z]", password)
    out(temp, "small letter")

    temp = re.findall("[A-Z]", password)
    out(temp, "Capital letter")

    temp = re.findall("[0-9]", password)
    out(temp, "Number")

    temp = re.findall(r"[!#$%&()*+,-./:;<=>?@[\]^_{|}~]", password)
    out(temp, "Special Character")


if __name__ == "__main__":
    password = input("Enter Your Password: ")
    requiredarr = []
    suggestedarr = []

    passwordchecker(password)

    if(len(requiredarr) != 0):
        for i in requiredarr:
            print("*", i)
    elif(len(suggestedarr) != 0):
        for i in suggestedarr:
            print("*", i)
    else:
        print("Your password is abolutely strong")
