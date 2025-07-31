from pypdf import PdfReader, PdfWriter


def merge_pdfs(file1, file2, output_file):
    pdf_writer = PdfWriter()
    
    # Open and add pages from the first PDF file
    with open(file1, 'rb') as f:
        pdf_reader1 = PdfReader(f)
        for page in pdf_reader1.pages:
            pdf_writer.add_page(page)

    # Open and add pages from the second PDF file
    with open(file2, 'rb') as f:
        pdf_reader2 = PdfReader(f)
        for page in pdf_reader2.pages:
            pdf_writer.add_page(page)

    # Write the merged PDF to output file
    with open(output_file, 'wb') as f:
        pdf_writer.write(f)


folder_path = "/Users/vishalagarwal/personal/receipts/driver-salary/"
file1 = folder_path + 'NainaCarDL.pdf'
file2 = folder_path + '2025-26/' + '2025-11-Driver-Salary.pdf'
output_file = folder_path + '2025-26/' + '2025-11-DL-Driver-Salary.pdf'

merge_pdfs(file1, file2, output_file)
