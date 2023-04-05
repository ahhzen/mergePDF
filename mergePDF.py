#This is a simple python program to merge PDF files
#It uses the PyPDF2 library

import PyPDF2
import pypdf
import os

#When executing the mergePDF.py file, the python program will look for all the PDF files in the folder and merge them into a single PDF file
#User will only need to specify the target PDF file name and the program will automatically merge all the PDF files in the folder into a single PDF file

#User will need to specify the target PDF file name
#check if the file name is valid and with PDF extension
#Also provide a way to abort the input if user wish to terminate the python program

while True:
    targetPDF = input("Please enter the target PDF file name: ")
    if targetPDF.endswith('.pdf'):
        break
    elif targetPDF == 'q':
        print("You have terminated the program")
        exit()
    else:
        print("Please enter a valid PDF file name")


#Create a list to store all the PDF files in the folder
pdfFiles = []

#Loop through all the files in the folder
for filename in os.listdir('.'):
    #Check if the file is a PDF file
    if filename.endswith('.pdf'):
        #If the file is a PDF file, add it to the list
        pdfFiles.append(filename)   

#Check list is not empty before merging then loop through the list and merge the PDF files 
if len(pdfFiles) > 0:
    #Sort the list
    pdfFiles.sort(key=str.lower)
    #Create a PDF writer object
    #pdfWriter = PyPDF2.PdfFileWriter()
    #pdfWriter = PyPDF2.PdfWriter()

    pdfWriter = pypdf.PdfWriter()
    #Loop through the list and merge the PDF files
    pageCount = 0
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')

        #check file is read successfully
        if pdfFileObj == None:
            print("Error reading file " + filename)
            #read next file
            continue

        #pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pdfReader = pypdf.PdfReader(pdfFileObj)

        #check anything that could go wrong when reading the PDF file
        if pdfReader == None:
            print("Error reading file " + filename)
            #read next file
            continue

        #Loop through all the pages and add them including the first page
        #get total number of pages in the PDF file using len(
        totalPages = len(pdfReader.pages)
        for pageNum in range(0, totalPages):
            pageObj = pdfReader.pages[pageNum]
            pdfWriter.add_page(pageObj)


    #Save the result into a PDF file
    pdfOutput = open(targetPDF, 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    #Print success message to the user specifying the target PDF file name and all the source PDF file names
    print("The following PDF files have been merged into " + targetPDF + ":")
    for filename in pdfFiles:
        print(filename)
        
else:
    print("No PDF files found in the folder")

