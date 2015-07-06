from conversions import Conversions
from main import Alien

# To create and write in to a .txt format- inherits Conversions class
class ToTXT(Conversions):
    FORMAT_NAME = "txt"
    def convert(self, alien):
        path = "Alien details.txt"

        detail = self.get_info(alien)
        with open(path, 'w') as fd:
            fd.write(detail)

        return 0, path
