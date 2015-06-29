# base.py
# This is base class for all conversion format codes
class Conversions:
    # function which returns a string to get_info function
    def get_format(self):
        return \
        "Code Name: %s  \n"\
        +"Blood Color: %s  \n"\
        +"Number: %d  \n"\
        +"Number of legs: %d  \n"\
        +"Home Planet: %s  \n"

    # Returns a variable containig string to be copied to file
    def get_info(self, alien):
        info = self.get_format() %(alien.codeName, alien.bloodColor, \
                            alien.numberOfAntennas, alien.numberOfLegs,\
                            alien.homePlanet)
        return info
        
    # Abstract class which can be overriden by conversion classes
    def convert(self, alien):
        print ("This is an abstrace class. If you see this message we're "
               "sorry, this is because of an error.")
        return -1;
