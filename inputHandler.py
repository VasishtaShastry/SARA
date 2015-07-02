class InputHandler:
    

    def takeAlienDetails(alien):
        alien.codeName = input("Code name : ")
        alien.bloodColor = input("Blood Color: ")
        while True:
                try:        
                        alien.numberOfAntennas = int(input("Number of Antennas: "))
                        alien.numberOfLegs = int(input("Number of Legs: "))
                        break
                except Exception as e:
                        print("Invalid Input : Integer Required")
                        print("\nTry Again\n")
                        continue
        alien.homePlanet = input("Home Planet: ")
        return alien
        
    def enquireRequiredFormat(FORMATS_AVAILABLE ):
        

        print("To which format would like to export?")
        for key in FORMATS_AVAILABLE:
            print (key, ". ", FORMATS_AVAILABLE[key][0])

        try:
            to_format = int(input())
        except Exception as e:
            print ("Error in input: ", e)

        if to_format > len(FORMATS_AVAILABLE):
            print("\n****Wrong Selection***\n")
            sys.exit(0)
        
        return to_format