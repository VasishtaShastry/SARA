from base import Conversions
from main import Alien

# To create and write in to a .pdf format
# inherits Conversions class from base module 
# uses pyfpdf module to convert into pdf format  
class ToPDF(Conversions):
    def convert(self, alien):
        path = "Alien details.pdf"
        import fpdf 
        to_pdf_str = self.get_info(alien)

        pdf = fpdf.FPDF(format = 'letter')
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt = to_pdf_str, ln=1, align = "")
        pdf.output(path)

        return 0, path
