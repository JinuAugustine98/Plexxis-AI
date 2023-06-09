import os
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError

def convert_folder_to_images(folder_path, output_path, dpi=1200):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Get a list of all PDF files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

    # Iterate over each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)

        try:
            # Get the page count of the PDF file
            page_count = get_pdf_page_count(pdf_path)

            # Convert PDF to images
            images = convert_from_path(pdf_path, dpi=dpi)

            # Save the images
            for i, image in enumerate(images):
                image_path = os.path.join(output_path, f"{pdf_file}_page_{i+1}.png")
                image.save(image_path, "PNG")

            print(f"Conversion complete for {pdf_file}. Pages: {page_count}")
        except PDFPageCountError:
            print(f"Error getting page count for {pdf_file}")
        except Exception as e:
            print(f"Error converting {pdf_file}: {str(e)}")

    print("Conversion process complete!")

def get_pdf_page_count(pdf_path):
    try:
        with open(pdf_path, "rb") as file:
            pdf_data = file.read()
            return len(pdf_data.split(b"/Type /Page")) - 1
    except Exception as e:
        raise PDFPageCountError(f"Error getting page count: {str(e)}")

# Set the input folder path containing PDF files
folder_path = r"Input_PDFs"

# Set the output folder path to save the images
output_path = r"Output_Images"

# Set the DPI (dots per inch) for high-quality output
dpi = 600

convert_folder_to_images(folder_path, output_path, dpi)
