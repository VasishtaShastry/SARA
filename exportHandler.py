FORMATS_AVAILABLE = {
#   "format" : "input text", <module to import from>, <classname>,
#   "FOOBAR" : ("foobar", 3, "<module name>", "classname"),
    }

PLUGINS_DIR = "plugins"

import pathlib
import alien
import sys
# gets user required format and calls appropriate function to export

class ExportHandler():
   
    def convert_to_dest_format(to_format, alien):
        
        
        try:
            # Reference: http://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
            module = __import__(PLUGINS_DIR + "." + FORMATS_AVAILABLE[to_format][1])
            class_name = getattr(getattr(module, FORMATS_AVAILABLE[to_format][1]), FORMATS_AVAILABLE[to_format][2])
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

    def fetch_plugins():
        global FORMATS_AVAILABLE

        modules = [str(p).split('/', 1)[-1][:-3] for p in pathlib.Path('./plugins/').iterdir() if p.is_file() and str(p).endswith(".py")]
        classes = [module[0].upper() + module[1:] for module in modules]

        

        for idx, each_module, each_class in zip(range(1, len(modules) +1), modules, classes):
            module = __import__(PLUGINS_DIR + "." + each_module)
            FORMATS_AVAILABLE[idx] = (getattr(getattr(module, each_module), each_class).FORMAT_NAME, each_module, each_class)
            del module
