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

    formats_available = ExportHandler.fetch_plugins()
    to_req_format = InputHandler.enquireRequiredFormat(formats_available)


    ret = ExportHandler.convert_to_dest_format(formats_available, to_req_format, alien)

    if ret < 0:
        print ("Conversion error:", ret)
