from PIL import Image
import argparse

chars = "@%#*+=-:. "

def resize(img, width=100):
    w, h = img.size
    ratio = h / w / 1.65
    return img.resize((width, int(width * ratio)))

def pixel_to_ascii(val):
    return chars[val * (len(chars) - 1) // 255]

def main(path, width):
    img = Image.open(path).convert("RGB")
    img = resize(img, width)

    pixels = img.load()
    w, h = img.size

    for y in range(h):
        line = ""
        for x in range(w):
            r, g, b = pixels[x, y]

            # grayscale brightness
            gray = int(0.299*r + 0.587*g + 0.114*b)

            char = pixel_to_ascii(gray)

            # ANSI color from original pixel
            line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"

        print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--width", type=int, default=100)

    args = parser.parse_args()
    main(args.image, args.width)