from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_path, dpi=1200):
    images = convert_from_path(pdf_path, dpi=dpi)

    for i, image in enumerate(images):
        image_path = f"{output_path}/page_600dpi_{i+1}.png"
        image.save(image_path, "PNG")

    print("Conversion complete!")

pdf_path = "Dataset/Ai Research/128611501_GM Financial_Issued 100215 (2).PDF"  # Path to the input PDF file
output_path = "HighRes_Images"  # Output directory to save the images
dpi = 600  # DPI (dots per inch) for high-quality output

convert_pdf_to_images(pdf_path, output_path, dpi)
