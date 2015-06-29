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


        
#main
if __name__ == '__main__':
    print("Welcome")

    alien = Alien()
    alien.takeInput()

    export_alien_details().get_required_format_name(alien)
