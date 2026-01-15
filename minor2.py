#Marrissa mayer
# =====================================
# Image to ASCII Art Converter
# Background forced to black (NO rembg)
# =====================================

from PIL import Image
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def remove_background_simple(image):
    """
    Converts light background to black
    """
    image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # If pixel is very bright → treat as background
            if r > 200 and g > 200 and b > 200:
                pixels[x, y] = (0, 0, 0)
    return image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def image_to_ascii(image_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_name)

    if not os.path.exists(image_path):
        print("❌ Image not found!")
        return

    image = Image.open(image_path)
    image = remove_background_simple(image)
    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width

    ascii_image = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_image += ascii_str[i:i + img_width] + "\n"

    print(ascii_image)

    output_path = os.path.join(script_dir, "ascii_output.txt")
    with open(output_path, "w") as f:
        f.write(ascii_image)

    print("\n✅ ASCII Art saved as ascii_output.txt")

# Run program
if __name__ == "__main__":
    image_to_ascii("image.jpg")

