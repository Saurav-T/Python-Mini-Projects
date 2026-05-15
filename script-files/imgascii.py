from PIL import Image
import argparse

chars = "@%#*+=-:. "

def resize(img, new_width=100):
    width, height = img.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return img.resize((new_width, new_height))

def to_grayscale(img):
    return img.convert("L")

def pixels_to_ascii(img):
    pixels = img.getdata()
    chars = "@%#*+=-:. "
    scale = len(chars)

    return "".join(chars[pixel * scale // 256] for pixel in pixels)

def main(path, width):
    img = Image.open(path)
    img = resize(img, width)
    img = to_grayscale(img)

    ascii_str =  pixels_to_ascii(img)
    img_width = img.width

    for i in range(0, len(ascii_str), img_width):
        print(ascii_str[i:i+img_width])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--width", type=int, default=100)

    args = parser.parse_args()
    main(args.image, args.width)