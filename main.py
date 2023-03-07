import argparse
import os  # For getting files
from pypdf import PdfMerger, PdfReader  # For PDF functions

README_TXT = "Place the pdfs ending with .pdf in this folder\nThe combiner will combine them according to alphabetical order\nPlease make sure pdf files end with .pdf\n"


class PDFConcat(object):
    def __init__(self, path_name: str) -> None:
        """Constructor for the PDFConcat obj"""

        # Store the paths
        self.path_name: str = path_name

    def get_pdf_names(self) -> tuple:
        """Check the pdf names of those who are in the folder"""
        return [f for f in os.listdir(self.path_name) if os.path.isfile(os.path.join(self.path_name, f)) and f.endswith(".pdf")]

    def concat(self, output_name: str) -> None:
        """Concatenate the PDF files"""
        mergedPDF: PdfMerger = PdfMerger()
        pdf_names = self.get_pdf_names()
        if len(pdf_names) == 0:
            print("No PDF files found")
            return
        for filename in pdf_names:
            print(f"Merging {filename}")
            mergedPDF.append(
                PdfReader(
                    os.path.join(
                        self.path_name,
                        filename
                    ),
                    strict=False
                ),
                import_outline=False,
            )
        print("Writing to output file")
        mergedPDF.write(output_name)
        print("File saved as {}".format(output_name))


def concat_files(dirname: str, output_name: str) -> None:
    """The main function to run the file"""

    # Create the PDFConcat obj
    pdfconcat = PDFConcat(dirname)

    # Create the PDF file
    pdfconcat.concat(output_name)


def create_folder_if_not_exists(dirname: str) -> None:
    """Create the folder if it does not exist"""
    if os.path.exists(dirname):
        return print(f"{dirname} exists, skipping folder creation")

    README_PATH = os.path.join(dirname, "README.txt")
    os.makedirs(dirname)
    with open(README_PATH, "w") as f:
        f.write(README_TXT)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='PDF Combiner'
    )
    parser.add_argument(
        '-p',
        type=str,
        help='The path to the folder containing the files to combine (default: input).\nWill create the folder if it does not exist',
        default="input",
        required=False,
    )
    parser.add_argument(
        '-o',
        type=str,
        help="Output name of the pdf file (default: output.pdf)",
        default="output.pdf",
        required=False
    )

    args = parser.parse_args()

    path = args.p
    output = args.o

    create_folder_if_not_exists(path)
    concat_files(path, output)
    input("Press Enter to continue")
