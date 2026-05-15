from PIL import Image
import argparse

chars = "@%#*+=-:. "
inverted_chars = " .:-=+*#%@"

def resize(img, new_width=100):
    width, height = img.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return img.resize((new_width, new_height))


def to_grayscale(img):
    return img.convert("L")


def pixels_to_ascii(img, invert=False):
    pixels = img.getdata()
    ascii_chars = inverted_chars if invert else chars
    scale = len(ascii_chars)-1

    return "".join(chars[pixel * scale // 256] for pixel in pixels)


def main(path, width, output_file, invert):
    img = Image.open(path)
    img = resize(img, width)
    img = to_grayscale(img)

    ascii_str = pixels_to_ascii(img, invert)
    img_width = img.width

    lines = []
    for i in range(0, len(ascii_str), img_width):
        # print(ascii_str[i:i+img_width])
        lines.append(ascii_str[i:i+img_width])

    ascii_art = "\n".join(lines)
    print(ascii_art)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ascii_art)
    
    print(f"\nSaved ASCII art to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--width", type=int, default=100)
    parser.add_argument("--output", default="output.txt",
                        help="Output text filename")
    parser.add_argument("--invert", action="store_true",
                        help="Invert brightness mapping")

    args = parser.parse_args()
    main(args.image, args.width, args.output, args.invert)
