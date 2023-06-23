import os
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder, dpi=600, thread_count=1):
    # Create a subfolder in the output folder for the PDF file
    pdf_filename = os.path.basename(pdf_path)
    pdf_name = os.path.splitext(pdf_filename)[0]
    output_subfolder = os.path.join(output_folder, pdf_name)
    os.makedirs(output_subfolder, exist_ok=True)

    # Convert the PDF to images using the provided dpi
    images = convert_from_path(pdf_path, dpi=dpi, thread_count=thread_count)

    # Save each page as a separate image in the output subfolder
    for i, image in enumerate(images):
        image_path = os.path.join(output_subfolder, f"page_{i+1}.png")
        image.save(image_path, "PNG")

    print(f"Conversion complete for {pdf_name}!")

# Usage example
pdf_path = "Dataset/page 2 2.pdf"
output_folder = "HighRes_Images"
dpi = 300
thread_count = 8

convert_pdf_to_images(pdf_path, output_folder, dpi, thread_count)
