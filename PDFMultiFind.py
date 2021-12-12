import PyPDF2
import os
import sys

def search(filename,target):
    """
    Finds if a string is in a pdf

    Arguments:
        filename (string): the name of the pdf to search
        target (string): the string being checked as to whether or not it's
            in the file

    Return:
        returns true if target is in the pdf and false if it isn't
    """
    fin = open("PDFs/" + filename,"rb")
    reader = PyPDF2.PdfFileReader(fin)

    for i in range(reader.numPages-1):
        page = reader.getPage(i)
        if target in page.extractText():
            fin.close()
            return True
    
    fin.close()
    return False


def main():
    files = os.listdir("PDFs")
    matches = []
    target = input()

    for i in files:
        if i[-4:] == ".pdf":
            if search(i,target):
                matches.append(i)

    if len(matches) == 0:
        print("No matches found")
    else:
        for i in matches:
            print(i)

if __name__ == "__main__":
    main()
