from PyPDF2 import PdfMerger


def merge_pdfs(file1, file2, file3, output_file):
    pdf_merger = PdfMerger()

    # Open the first PDF file
    with open(file1, 'rb') as f:
        pdf_merger.append(f)

    # Open the second PDF file
    with open(file2, 'rb') as f:
        pdf_merger.append(f)

    # Open the third PDF file
    with open(file3, 'rb') as f:
        pdf_merger.append(f)

    # Merge the PDF files
    with open(output_file, 'wb') as f:
        pdf_merger.write(f)


pdf_filepath = "/Users/zupee/Downloads/"
file1 = pdf_filepath + '2023-24-Apr-Jul-HomeRent-Z88-Vishal-Agarwal.pdf'
file2 = pdf_filepath + '2023-24-Aug-Nov-HomeRent-Z88-Vishal-Agarwal.pdf'
file3 = pdf_filepath + '2023-24-Dec-Mar-HomeRent-Z88-Vishal-Agarwal.pdf'
output_file = pdf_filepath + '2023-24-HomeRent-Z88-Vishal-Agarwal.pdf'

merge_pdfs(file1, file2, file3, output_file)
