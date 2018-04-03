# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 13:48:34 2018

@author: Jamie M JOHNS 2018
code is subject to improvement and optimization

Source: https://github.com/JamieMJohns/Merge-multiple-.pdf-into-a-single-.pdf-with-python

This pthon code was created and tested in spyder with python 2.7

The code includes user interface for it's original use of being converted
into a stand alone executable file (.exe)

from the same github source, there is also a another .py file which
is the bare mininum code for completing the same task.

This code is subject to improvement and optimization.


"""

import os # required module for find paths(directories) and files
from PyPDF2 import PdfFileMerger ## required module (PyPDF2) and function (PdfFileMerger) for merging pdf files
os.system('color 1F') #set color of text and background to respectivly be bright white and blue
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' #String for user interface
print '@@@@@@@@@@@@@@ Merge multiple pdf files into one pdf @@@@@@@@@@@@@@@@@@@' #String for user interface
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' #String for user interface
print '                 Code created in Spyder (Python 2.7)' #String for user interface
print '                           By                                           ' #String for user interface
print '                       Jamie Johns                                      ' #String for user interface
print '                          2018           ' #String for user interface
print '   The code was converted to an .exe file using "Pyinstaller"           ' #String for user interface
print 'Description============================================================='#String for user interface
print 'Given path (directory) to a folder of .pdf files, this program will com-' #String for user interface
print 'bine all pdf files (in that folder) into a single pdf file.' #String for user interface
print 'The .pdf files are combined in chronological order of their filenames.\n' #String for user interface
print 'For example, with the following pdf of filenames; ' #String for user interface
print '   file_a.pdf,file_c.pdf,old_file_a.pdf,file_b1.pdf and file_b2.pdf' #String for user interface
print 'The files will be combined in order of (from first to last);' #String for user interface
print '   file_a.pdf,file_b1.pdf,file_b2.pdf,file_c.pdf and old_file_a.pdf' #String for user interface
print 'The name of the output (merged) pdf is chosen by the user.' #String for user interface
print '========================================================================' #String for user interface
raw_input('<Press any key to continue>') #code waits for user response before continuing
# GET DIRECTORY $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
print '\n FIRST, enter directory (path to folder) that contains the pdf files. '  #String for user interface
print '[For example; "C:\My documents\my_pdf_files" (without quotes)]\n\n'  #String for user interface
print 'Does the current directory contain the .pdf files?'  #String for user interface
print 'Current directory:'          #String for user interface                                               
cwd = os.getcwd() #get current directory that python program is located in
print cwd #print directory
chdirr=raw_input('>>If yes, type "y" (without quotes) and press enter:') # ask user if they want to use current directory
print '\n'  #String for user interface
if 'y'==chdirr: #if user wants to use current directory
    print 'You have chosen to use the directory listed above!'  #String for user interface
else:             #else, user must specify directory
    print 'Below, enter the path to the folder of interest (e.g - D:\My_pdf_files)'  #String for user interface
    folderfound=0  #parameter which determines if unproblematic folder has been found (=0 no, =1 yes)
    while folderfound==0: #while errorless directory has not been found 
        try: # test if directory read with no problems
            cwd=raw_input('>>input:  ') #user enter path to directory of interest
            path, dirs, files = os.walk(cwd).next()  #test if input directory does not result in an error (gets list of all paths and file in directory cwd)
            folderfound=1 #if no error above, working directory found (exit while loop)
        except Exception as err1: #If above resulted in error (also record error message as string "err1")
            print 'There was an error with the directory you entered.' #String for user interface
            print 'The python specific error is listed as: ' #String for user interface
            print err1 #Print python specific error
            raw_input('<Press any key to try again>') #wait for user response            
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
files_pdf=[j for j in files if '.pdf' in j] #create list of only pdf files (from initial list; files)
file_paths=[cwd+'\\'+j for j in files_pdf] # create list of full file path to each pdf (note: "\\" is needed for "\")
print '\n'
# find file name for new (merged) pdf######################################################################
ok_pdf_name=0  #parameter which determines if ok pdf filename not given (=0 is no)
while ok_pdf_name==0: #while ok pdf file name not given
    print '\n' #String for user interface
    print 'Below, enter a filename for the new (merged) pdf;' #String for user interface
    print '[Example - enter "new_file" (without quotes) to create "new_file.pdf" ]' #String for user interface
    new_pdf=raw_input('Filename: ') # USER ENTER IN NAME FOR NEW PDF
    new_pdf_full=new_pdf+'.pdf'
    chk_not_exist=[j for j in files_pdf if new_pdf_full==j] #check list of current pdf, that pdf of new file name not exist (risk-overwriting)
    if chk_not_exist: # if above line does not return empty, this line will return TRUE (pdf of same name found)
        print 'It was found that a .pdf of name: '+new_pdf_full #String for user interface 
        print 'already exist in the directory; '
        print cwd
        print '\nDo you want to overwrite this existing file?'
        print 'If yes,below, type "y" (without quotes)' 
        ow=raw_input('>>input: ') # ASK USER IF OK TO USE SPECIFIED NAME AND OVERWRITE EXISTING PDF OF SAME NAME
        if ow=='y': #if user decides to overwrite file
            ok_pdf_name=1 #exit while loop (and continue to next section)
    else: #if no pdf file of same name found
        ok_pdf_name=1 # continue to next section
##################################################################################################
print '\n\n'
print 'PROCESS HAS STARTED!!' #show  user process started
print '0% complete..' #print first percentage complete

merger = PdfFileMerger() #create pdf merge object
err=0 #parameter which keeps track of whether there were any errors during merging of pdf files
nwtxt=open(cwd+'\\'+new_pdf+'_order_of_merge'+'.txt','w') #create new text file which will list order of merged pdf
nwtxt.write('Order that pdf files are added to file:'+'\n') #write string to text file
nwtxt.write(new_pdf_full+'\n') #write string to text file
nwtxt.write('<From first to last>') #write string to text file
nwtxt.write('Files:') #write string to text file
for j,pdf in enumerate(file_paths,start=1): #for each pdf (path) in list of pdf file paths (and including a integer paramter j starting from 1)
    if err==0: #if no error (i.e-continue merging files)
        try: #try to add jth pdf file
            merger.append(pdf) # merge jth pdf file
            pcc=100*j/len(file_paths) #get current percentage complete for entire procewss 
            nwtxt.write(files_pdf[j-1]+'\n') #write pdf file name to txtfile (list of merged pdf)
            print str(pcc)+'% complete....'#Print percentage complete
        except Exception as err1: #if there was an error merging jth pdf file, obtain error message as string "err1"
            merger.close() #close pdf file dependcies on this program
            nwtxt.write('ERROR AT: '+files_pdf[j-1]+'\n') #in text file; print which file there was error
            nwtxt.write('FINAL MERGED PDF WAS NOT CREATED!!\n') #in text file print string
            nwtxt.write('Specific error was:'+'\n\n')  #in text file print string
            nwtxt.write(err1)  #in text file print string
            print '\nERROR!! there was an error when adding file number '+str(j)  #print error info for user
            print '(filename: '+files_pdf[j-1]+')' #print error info for user
            print 'to the new (merged) pdf, check this file and try running the program again.' #print error info for user
            print 'The specific error (as listed in python 2.7) is;' #print error info for user
            print err1 #print python specific error
            err=1
if err==0: #IF THERE WAS NO ERROR DURING ENTIRE MERGE PROCESS
    merger.write(cwd+'\\'+new_pdf_full) #save merged files to pdf of specified name
    merger.close() #close pdf file dependcies on this program
    print 'PROCESS COMPLETE !!!!!!' #user info string
    print '\The new (merged) .pdf file named:' #INFO ABOUT NEW SAVED PDF
    print new_pdf+'.pdf' #INFO ABOUT NEW SAVED PDF
    print 'Was created in the folder:' #INFO ABOUT NEW SAVED PDF
    print cwd #INFO ABOUT NEW SAVED PDF
    print '\nIn addition, a text file named: ' #INFO ABOUT TXT FILE WITH INFO ABOUT ORDER OF MERGING FILES
    print new_pdf+'_order_of_merge'+'.txt' #INFO ABOUT TXT FILE WITH INFO ABOUT ORDER OF MERGING FILES
    print 'was created in the same directory which list order of which pdf files' #INFO ABOUT TXT FILE WITH INFO ABOUT ORDER OF MERGING FILES
    print 'were combined (from first to last)' #INFO ABOUT TXT FILE WITH INFO ABOUT ORDER OF MERGING FILES
    print '\n\n' #user interface string (skip two lines)
nwtxt.close() #close new text file from writing
raw_input('<Press any key to exit the program>') #wait for user to press key before exit program
