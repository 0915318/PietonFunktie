from easygui import *
import sys

msg = "Do you want to continue?"
title = "Please Confirm"
if ccbox(msg, title):     # show a Continue/Cancel dialog
    pass  # user chose Continue
else:  # user chose Cancel
    sys.exit(0)