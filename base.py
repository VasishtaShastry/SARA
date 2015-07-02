alien_details_to_print = {
    "codeName" : "Code Name :",
    "bloodColor" : "Blood Color :",
    "numberOfAntennas" : "Number of Antennas :",
    "numberOfLegs" : "Number of legs : ",
    "homePlanet" : "Home Planet : ",
    }
# base.py
# This is base class for all conversion format codes
class Conversions:
   
    # Returns a variable containig string to be copied to file
    def get_info(self, alien):
        info = ""
        for key, value in alien.__dict__.items():
            if not key.startswith("__"):
                info += "%s : %s\n" % (alien_details_to_print[key],value)
        
        return info
        
    # Abstract class which can be overriden by conversion classes
    def convert(self,alien):
        print ("This is an abstrace class. If you see this message we're "
               "sorry, this is because of an error.")
        return -1;
