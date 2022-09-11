import sys
from PIL import Image, ImageOps
import os

def main():
    command_line_arguments()

    # Open the files

    try:
        img = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    img2 = ImageOps.fit(img, size)
    img2.paste(shirt, shirt)
    img2.save(sys.argv[2])



def command_line_arguments():
    ext = (".png", ".jpg", ".jpeg")
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith(ext):
        sys.exit("Invalid input")
    elif not sys.argv[2].lower().endswith(ext):
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")
    else:
        pass
main()