import os
from PIL import Image

def find_smallest_image(directory):
    min_area = float('inf')
    smallest_image = ''

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                try:
                    img = Image.open(os.path.join(foldername, filename))
                    area = img.width * img.height
                    if area < min_area:
                        min_area = area
                        smallest_image = os.path.join(foldername, filename)
                except IOError:
                    print(f'Error opening image: {os.path.join(foldername, filename)}')
                continue

    return smallest_image

# Replace '/path/to/your/images' with the path to your images.
smallest_image = find_smallest_image('./blog-vec-slike')

print(f'The smallest image is located at: {smallest_image}')
