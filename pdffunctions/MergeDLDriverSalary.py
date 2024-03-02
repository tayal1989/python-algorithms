from PyPDF2 import PdfMerger


def merge_pdfs(file1, file2, output_file):
    pdf_merger = PdfMerger()

    # Open the first PDF file
    with open(file1, 'rb') as f:
        pdf_merger.append(f)

    # Open the second PDF file
    with open(file2, 'rb') as f:
        pdf_merger.append(f)

    # Merge the PDF files
    with open(output_file, 'wb') as f:
        pdf_merger.write(f)


pdf_filepath = "/Users/vishalagarwal/personal/docs/DriverSalary/2023-24/"
file1 = pdf_filepath + 'NainaCarDL.pdf'
file2 = pdf_filepath + '2024-03-Driver-Salary.pdf'
output_file = pdf_filepath + '2024-03-DL-Driver-Salary.pdf'

merge_pdfs(file1, file2, output_file)
