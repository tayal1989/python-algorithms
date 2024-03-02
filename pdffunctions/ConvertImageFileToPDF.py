from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image


def convert_png_to_pdf(input_image_path, output_pdf_path):
    image = Image.open(input_image_path)
    pdf_path = output_pdf_path

    # Create a canvas with the size of the image
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=image.size)

    # Draw the image on the canvas
    pdf_canvas.drawImage(input_image_path, 0, 0)

    # Save the canvas as PDF
    pdf_canvas.save()


# Example usage
pdf_filepath = "/Users/zupee/Personal/docs/LearningBillsCertificate/2023-24/"
input_image_path = pdf_filepath + "GitHub-Completion-Certificate.png"
output_pdf_path = pdf_filepath + "GitHub-Completion-Certificate.pdf"
convert_png_to_pdf(input_image_path, output_pdf_path)
