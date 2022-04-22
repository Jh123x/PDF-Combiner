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
        
    
    def concat(self, output_name: str) -> None:
        """Concatenate the PDF files"""
        mergedPDF = PdfFileMerger(strict=False)
        for filename in self.get_pdf_names():
            print(f"Merging {filename}")
            mergedPDF.append(PdfFileReader(os.path.join(self.path_name,filename), strict=False))
        print("Writing to output file")
        mergedPDF.write(output_name)
        print("File saved as {}".format(output_name))


def concat_files(dirname: str, output_name: str) -> None:
    """The main function to run the file"""

    #Create the PDFConcat obj
    pdfconcat = PDFConcat(dirname)

    #Create the PDF file
    pdfconcat.concat(output_name)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='PDF Combiner')
    parser.add_argument('-p', type=str, help='The path to the folder containing the files to combine', default="input", required=False)
    parser.add_argument('-o', type=str, help="Output of the pdf file", default="output.pdf", required=False)


    args = parser.parse_args()
    concat_files(args.p, args.o)
    