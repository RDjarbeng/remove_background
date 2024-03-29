from rembg import remove
from PIL import Image
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def remove_background(input_path, output_path):
    try:
        # Open the input image
        input_image = Image.open(input_path)
        logging.info(f"Opened image {input_path}")

        # Remove the background
        output_image = remove(input_image)
        logging.info("Background removed")

        # Convert to RGB mode if necessary
        if output_image.mode != 'RGB':
            output_image = output_image.convert('RGB')
            logging.info("Converted to RGB mode")

        # Save the output image
        output_image.save(output_path)
        logging.info(f"Saved output image {output_path}")

        # Close the input image
        input_image.close()
    except FileNotFoundError:
        logging.error(f"The file {input_path} does not exist.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_bg.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_background(input_path, output_path)
