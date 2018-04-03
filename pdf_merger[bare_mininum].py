# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 13:48:34 2018

@author: Jamie M JOHNS 2018
code is subject to improvement and optimization

Source: https://github.com/JamieMJohns/Merge-multiple-.pdf-into-a-single-.pdf-with-python

This pthon code was created and tested in spyder 2.7

Description: This is simplification of other code found on same source,above,
              it is the bareminum code for combining multiply pdf (from one folder) into a single pdf
              the pdf will be listed in new pdf by chronoglogical order of their file names


"""

import os # required module for find paths(directories) and files
from PyPDF2 import PdfFileMerger ## required module (PyPDF2) and function (PdfFileMerger) for merging pdf files

cwd='D:\\mydocuments\\my_pdf_files' #path to directory of with all pdf files to combine (note use '\\' for '\')
path, dirs, files = os.walk(cwd).next()  #test if input directory does not result in an error (gets list of all paths and file in directory cwd)
files_pdf=[j for j in files if '.pdf' in j] #create list of only pdf files (from initial list; files)
file_paths=[cwd+'\\'+j for j in files_pdf] # create list of full file path to each pdf (note: "\\" is needed for "\")

new_pdf='pdf_merged.pdf' # file name new merged pdf (note: will over write pdf in "cwd" of same name)


merger = PdfFileMerger() #create pdf merge object

for pdf in file_paths: #for each pdf (path) in list of pdf file paths (and including a integer paramter j starting from 1)
    merger.append(pdf) # merge add pdf as next file in merge object

merger.write(cwd+'\\'+new_pdf) #save merged files to pdf of specified name (output location is same as "cwd" above)
merger.close() #close all pdf file dependcies on this program
