# A class which bounds all information about a alien and takes input 
import sys
class Alien:
    def __init__(self):
        self.codeName = ""
        self.bloodColor = ""
        self.numberOfAntennas = 0
        self.numberOfLegs = 0
        self.homePlanet = ""
    
    # take_input - take input from user and store them in class variables 
    def takeInput(self):
        self.codeName = input("Code name : ")
        self.bloodColor = input("Blood Color: ")
        while True:
                try:        
                        self.numberOfAntennas = int(input("Number of Antennas: "))
                        self.numberOfLegs = int(input("Number of Legs: "))
                        break
                except Exception as e:
                        print("Invalid Input : Integer Required")
                        print("\nTry Again\n")
                        continue
        self.homePlanet = input("Home Planet: ")
