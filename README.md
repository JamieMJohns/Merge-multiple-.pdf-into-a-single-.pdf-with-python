# Merge-multiple-.pdf-into-a-single-.pdf-with-python  

This repository includes my code (python 2.7) for program which merges multiple .pdf files into a single .pdf file.  

In this repository there are two .py files -  
=> (pdf_merger.py) my original code (with user interface; code was converted to standalone .exe using pyinstaller)  
=> (pdf_merger.exe) above code converted to standalone .exe using pyinstaller; the .exe has so far only been tested on windows10 64-bit.
=> (pdf_merger.py[bare_mininum].pdf) also my code but with the user interface removed; the bare mininum for completing the same task. 

Bug in this current version $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
program will crash when .exe is running in same folder as the pdf 
files which are being combined.  
Temporary fix for now: run .exe from different folder other than the 
folder that the pdf files are in. 
(this bug will be fixed soon and new files uploaded to this
repository)  
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 


Required python modules/packages for both codes are; os and PyPDF2.
