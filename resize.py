from PIL import Image

def resize_image(image_path, output_path, width, height):
    """
    Resize the image to the specified width and height.
    
    Arguments:
    image_path -- the path to the input image file
    output_path -- the path to save the resized image
    width -- the desired width of the output image
    height -- the desired height of the output image
    """
    with Image.open(image_path) as image:
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        bw_image = resized_image.convert("L")  # Convert to black and white
        bw_image.save(output_path)

# Example usage:
input_image_path = "/Users/jinuaugustine/Downloads/page_2_600dpi.png"
output_image_path = "Dataset/resized.png"
target_width = 6000
target_height = 6000

resize_image(input_image_path, output_image_path, target_width, target_height)
