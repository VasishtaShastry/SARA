# main.py


import sys
from alien import Alien
from exportHandler import ExportHandler
from exportHandler import *

from inputHandler import InputHandler

if __name__ == '__main__':
    print("Welcome")

    alien = Alien()
    alien = InputHandler.takeAlienDetails(alien)
    
    ExportHandler.fetch_plugins()
    to_req_format = InputHandler.enquireRequiredFormat(FORMATS_AVAILABLE)
    
    
    ret = ExportHandler.convert_to_dest_format(to_req_format, alien)
    
    if ret < 0:
        print ("Conversion error:", ret)