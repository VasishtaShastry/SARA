# Recommended to import and extend your class with our Base class
from base import Conversions

# The name of the class should be name of the module with first letter
# capitalized.
class Dummy(Conversions):
    # Declare a class variable FORMAT_NAME and specify the format you're
    # converting to
    FORMAT_NAME="dummy"

    # Should implement/extend convert method. Takes variable of Alien class as
    # argument.
    def convert(self, alien):
        print ("This is a dummy method")
        # Return 0 for success and negative number for failure. and path of the
        # file you created.
        return 0, "Nowhere"
