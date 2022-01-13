PDFMultiFind
A python program that finds which pdf files contain a given search query.

Contents:
 - PDFMultiFind.py: the program that finds pdfs containing the search query
 - PDFs: a directory containing the pdfs to be searched
 - README.txt - this file

Additional requirements:
Requires that you have Python and PyPDF2 installed.
PyPDF2: https://pypi.org/project/PyPDF2/

Running instructions:
Place your pdf files in the PDFs folder, then run from the command line with python3 PDFShort.py. Type your search query into the terminal, then press enter. The names of the pdf files containing the search query will be printed to the terminal.

Note: doesn't seem to work properly sometimes when the searchy query is longer than 1 word due to how PyPDF2's extractText() method works (whitespace isn't kept). If this happens, removing whitespace from your search query fixes it.
