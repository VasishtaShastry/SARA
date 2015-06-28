# A class which bounds all information about a alien and takes input 
import sys
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
