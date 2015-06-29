FORMATS_AVAILABLE = {
#   "format" : "input text", <module to import from>, <classname>,
    "1" : ("pdf", "toPDF", "ToPDF"),
    "2" : ("txt", "toTXT", "ToTXT"),
#   "FOOBAR" : ("foobar", 3, "<module name>", "classname"),
    }



# Class which gets user required format and calls appropriate funtion to export
# information in that format  
class exportAlienDetails():
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
