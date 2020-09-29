from PyPDF2 import PdfFileMerger, PdfFileReader #For PDF functions
import argparse
import os #For getting files

class PDFConcat(object):
    def __init__(self, path_name:str):
        """Constructor for the PDFConcat obj"""

        #Store the paths
        self.path_name = path_name

    def get_pdf_names(self) -> tuple:
        """Check the pdf names of those who are in the folder"""
        return [f for f in os.listdir(self.path_name) if os.path.isfile(os.path.join(self.path_name, f))]
        
    
    def concat(self) -> None:
        """Concatenate the PDF files"""
        mergedPDF = PdfFileMerger()
        for filename in self.get_pdf_names():
            print(f"Merging {filename}")
            mergedPDF.append(PdfFileReader(os.path.join(self.path_name,filename)))
        print("Writing to output file")
        mergedPDF.write("Output.pdf")


def main() -> None:
    """The main function to run the file"""

    #Create the PDFConcat obj
    pdfconcat = PDFConcat('input')

    #Create the PDF file
    pdfconcat.concat()


if __name__ == '__main__':
    main()