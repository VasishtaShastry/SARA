# SARA
<h2>SARA - Single Alien Registry Application</h2>

A <u> basic python console application </u> which recieves five variables(details about an alien) and writes it into a file of format of user choice

**main.py** controls whole work flow</br>
**base.py** provides an abstact class for the format conversion</br>
**toPDF.py** using [pyfpdf](https://github.com/reingart/pyfpdf) it creates a new file and writes collected data into the file</br>
**toTXT.py** Creates a simple text file and writes data into the file</br>
**ExportHandler.py** Handels Export by asking required format and calling appropriate function</br>
**Alien.py** Contains a class which bounds details of an alien and takes input

# python version - 3

## Please install [pyfpdf](https://github.com/reingart/pyfpdf)

### How to implement 'plug in'

1.open main.py after donloading</br>
2.go to FORMATS_AVAILABLE dictionary</br>
3.enter details in mentioned format and also as mentioned in example</br>
4.copy your file</br>
5.Re-run

###Thank You

