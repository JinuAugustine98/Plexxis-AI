import os
import sys
from pdf2image import convert_from_path

def convert_folder_to_images(folder_path, output_path, dpi=1200):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Get a list of all PDF files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

    # Iterate over each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)

        # Convert PDF to images
        try:
            images = convert_from_path(pdf_path, dpi=dpi)
        except Exception as e:
            print(f"Error converting {pdf_file}: {str(e)}")
            continue

        # Save the images
        for i, image in enumerate(images):
            image_path = os.path.join(output_path, f"{pdf_file}_page_{i+1}.png")
            try:
                image.save(image_path, "PNG")
            except Exception as e:
                print(f"Error saving image for {pdf_file}: {str(e)}")
                continue

    print("Conversion complete!")

# Set the input folder path containing PDF files
folder_path = "Input_PDFs"

# Set the output folder path to save the images
output_path = "Output_Images"

# Set the DPI (dots per inch) for high-quality output
dpi = 600

# Set the system encoding to UTF-8
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding("utf-8")

convert_folder_to_images(folder_path, output_path, dpi)
