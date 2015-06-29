# main.py
# Assumptions:
# 1.The new format should inherit our converstions class and extend the method
# 2.User wants to export information of only one alien ata time

import sys
from alien import Alien
from ExportHandler import exportAlienDetails

if __name__ == '__main__':
    print("Welcome")

    alien = Alien()
    alien.takeInput()

    exportAlienDetails().get_required_format_name(alien)
