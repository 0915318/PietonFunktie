from easygui import *
import json
from pprint import pprint

with open('db.json') as f:
    data = json.load(f)

users = data["users"]

i = 0
while i < 3:
    user = (users[i]["email"])
    password = (users[i]["pass"])
    print(user,password)
    i += 1

    #user = data["users"][1]["email"]
    #password = data["users"][1]["pass"]

    msg = "Log hier in"
    title = "nice"
    fieldNames = ["User ID", "Password"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multpasswordbox(msg, title, fieldNames)

    # make sure that none of the fields was left blank
    while 1:
      if fieldValues == None: break
      errmsg = ""
      for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
          errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
      if errmsg == "": break # no problems found
      fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
    print("Reply was:", fieldValues)

    if fieldValues[0] == user and fieldValues[1] == password:

        #als je door de inlog bent kom je in de selectie voor wat je wilt doen
        msg = "Hello {}, jouw wachtwoord is {}.... {} {}".format(fieldValues[0],fieldValues[1],user,password)
        title = "Manage"
        choices = ["register", "delete", "upload"]
        choice = choicebox(msg, title, choices)
        if choice == "register":
            msgbox("you want to register")
        elif choice == "delete":
            msgbox("you want to delete")
        elif choice == "upload":
            print("you want to upload")
    else:
        msgbox("Foute info {}, jouw wachtwoord is {}".format(user,password))