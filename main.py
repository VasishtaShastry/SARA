# File name: main.py
# Program structure : conversions class is base class which can be inherited by subsequent conversion codes
# classes 
# which converts file format
# Assumptions:
# 1.The new format should inherit our converstions class and extend the method
# 2.User wants to export information of only one alien ata time

import sys

FORMATS_AVAILABLE = {
#   "format" : "input text", <module to import from>, <classname>,
    "1" : ("pdf", "toPDF", "ToPDF"),
    "2" : ("txt", "toTXT", "ToTXT"),
#   "FOOBAR" : ("foobar", 3, "<module name>", "classname"),
    }
    
# A class which bounds all information about a alien and takes input 
class Alien:
    def __init__(self):
        self.code_name = ""
        self.blood_color = ""
        self.num_of_antennas = 0
        self.num_of_legs = 0
        self.home_planet = ""
    # num in the sense number      
    # take_input - take input from user and store them in class variables 
    def take_input(self):
        self.code_name = input("Code name : ")
        self.blood_color = input("Blood Color: ")
        try:        
                self.num_of_antennas = int(input("Number of Antennas: "))
                self.num_of_legs = int(input("Number of Legs: "))
        except Exception as e:
                print("Invalid Input : Integer Required")
                sys.exit(0)
        self.home_planet = input("Home Planet: ")
            


# Class which gets user required format and calls appropriate funtion to export
# information in that format  
class export_alien_details():
    # function to import appropriate module to convert data into user required 
    # format 
    def convert_to_dest_format(self, to_format, alien):
        try:
            # 
            # Reference: http://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
            module = __import__(FORMATS_AVAILABLE[to_format][1])
            class_name = getattr(module, FORMATS_AVAILABLE[to_format][2])
            instance = class_name()
        except Exception as e:
            print ("Conversion error:", e)
            sys.exit(0)

        print ("Converting to ", FORMATS_AVAILABLE[to_format][0], " format")
        ret, path = instance.convert(alien)
        if ret < 0:
            print ("Conversion error: ", ret)
            sys.exit(0)
        print ("Conversion successful!! Dest file: ", path)
        return 0

    # gets user required format and call convert funtion
    def get_required_format_name(self, alien):
        print("To which format would like to export?")
        for key in FORMATS_AVAILABLE:
            print (key, ". ", FORMATS_AVAILABLE[key][0])

        to_format = input()
        
        if int(to_format) > len(FORMATS_AVAILABLE):
            print("\n****Wrong Selection***\n")
            sys.exit(0)

        ret = self.convert_to_dest_format(to_format, alien)
        if ret < 0:
            print ("Conversion error:", ret)
        
#main
if __name__ == '__main__':
    print("Welcome")

    alien = Alien()
    alien.take_input()

    export_alien_details().get_required_format_name(alien)
