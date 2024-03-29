from rembg import remove
from PIL import Image

input_path = "pic.jpg"
output_path = "pic_bg_removed.jpg"
input_image = Image.open(input_path)
output_image = remove(input_image)
rgb_image = output_image.convert('RGB')  # Convert to RGB mode
rgb_image.save(output_path)
input_image.close()