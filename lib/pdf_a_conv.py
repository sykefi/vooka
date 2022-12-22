# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:44:37 2022

@author: smassine
"""

def writePdfA():

    """
    A function for converting PDF-files into PDF/A.
    """

    import os
    import ghostscript

    print("\n PDF to PDF/A Conversion \n")

    # ghostscript package used
    # Output: PDF/A - 1b conversion

    filepath1 = input(" Enter input filepath to folder: ")

    Output1 = input(" Enter output filepath to folder: ")

    output = Output1 + "\\"

    filepath = filepath1 + "\\"

    filelist = os.path.isdir(filepath) # specified path is an existing directory or not


    # os.listdir = list the file list in the directory
    for fname in os.listdir(filepath):
        
        print(fname)
        if not fname.endswith(".pdf"):
            continue
        path = os.path.join(filepath, fname) 
        print(path)
        
        #print(fname)
        #print(path)
        ghostScriptExec = ['gs', '-dPDFA', '-dBATCH', '-dNOPAUSE', '-dUseCIEColor', '-sProcessColorModel=DeviceRGB',
                    '-sDEVICE=pdfwrite', '-dFastWebView', '-dAutoRotatePages=/None', '-sPDFACompatibilityPolicy=1',
                    '-sOutputFile='+ output + 'PDFA-' + fname, path]
        ghostscript.Ghostscript(*ghostScriptExec)
        #print(filepath)
        
    print("\n Conversion Completed\n")
    return()