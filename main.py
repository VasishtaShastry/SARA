# File name: main.py
# Program structure : conversions class is base class which can be inherited by subsequent conversion codes
# classes 
# which converts file format
# Assumptions:
# 1.The new format should inherit our converstions class and extend the method
# 2.User wants to export information of only one alien ata time

import sys
from alien import Alien
from ExportHandler import export_alien_details

FORMATS_AVAILABLE = {
#   "format" : "input text", <module to import from>, <classname>,
    "1" : ("pdf", "toPDF", "ToPDF"),
    "2" : ("txt", "toTXT", "ToTXT"),
#   "FOOBAR" : ("foobar", 3, "<module name>", "classname"),
    }
    

        
#main
if __name__ == '__main__':
    print("Welcome")

    alien = Alien()
    alien.take_input()

    export_alien_details().get_required_format_name(alien)
