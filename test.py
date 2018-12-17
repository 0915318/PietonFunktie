from easygui import *
import os
from pprint import pprint

class Settings(EgStore):

    def __init__(self, filename):  # filename is required
        #-------------------------------------------------
        # Specify default/initial values for variables that
        # this particular application wants to remember.
        #-------------------------------------------------
        self.userId = "userid"
        self.targetServer = "targetserver"

        #-------------------------------------------------
        # For subclasses of EgStore, these must be
        # the last two statements in  __init__
        #-------------------------------------------------
        self.filename = filename  # this is required
        self.restore()            # restore values from the storage file if possible

settingsFilename = os.path.join("C:", "\School\Python\OP2\PietonFunktie", "settings.txt")  # Windows example
settings = Settings(settingsFilename)

msg = "Enter logon information"
title = "Demo of multpasswordbox"
fieldNames = ["Server ID", "User ID", "Password"]
fieldValues = []  # we start with blanks for the values
fieldValues = multpasswordbox(msg,title, fieldNames)

# we save the variables as attributes of the "settings" object
settings.userId = fieldValues[1]
settings.targetServer = fieldValues[2]
settings.store()    # persist the settings

# run code that gets a new value for userId
# then persist the settings with the new value
user = "biden_joe"
settings.userId = user
settings.store()