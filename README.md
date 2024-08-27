# Remove background image using python package
Script to remove background from an image. Uses rembg package.

If you don't want to mess around with  code:
I made a web version of the background remover and deployed to [hugging face, check it out here](https://huggingface.co/spaces/rdjarbeng/free-background-remover)
- Also added option to choose different models that work better for different use cases; people, anime, clothing.✅
- Added options to also add post editing options so improve the mask.✅
- Added the option to download the processed image without the background in original quality. ✅

![bg_hugginface_remover_screenshot](https://github.com/user-attachments/assets/cfad08f3-a85b-48a1-b21d-e15c6d41c644)


Using code:
Dependiencies are located in requirements.txt

## Quick way
Modify the code. Run remove_bg.py with input path to image with extension and preferred output path
eg: input_path = 'C:/User/Desktop/image.png'

## Safe way

Run remove_bg_safe.py with input path as above. This just adds some exception handling and is less likely to crash unexpectedly.
