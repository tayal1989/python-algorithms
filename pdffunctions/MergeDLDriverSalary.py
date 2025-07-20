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


folder_path = "/Users/vishalagarwal/personal/receipts/driver-salary/"
file1 = folder_path + 'NainaCarDL.pdf'
file2 = folder_path + '2025-26' + '2025-08-Driver-Salary.pdf'
output_file = folder_path + '2025-26' + '2025-08-DL-Driver-Salary.pdf'

merge_pdfs(file1, file2, output_file)
