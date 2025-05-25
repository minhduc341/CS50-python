import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        if sys.argv[1].rsplit('.')[1].lower() not in ['jpg', 'jpeg', 'png']:
            sys.exit('Invalid input')
        if sys.argv[2].rsplit('.')[1].lower() not in ['jpg', 'jpeg', 'png']:
            sys.exit('Invalid input')
        if sys.argv[1].rsplit('.')[1].lower() != sys.argv[2].rsplit('.')[1].lower():
            sys.exit('Input and output have different extensions')
        try:
            overlay(sys.argv[1], sys.argv[2])
        except FileNotFoundError:
            sys.exit('Input does not exist')

def overlay(image1, image2):
    shirt = Image.open("shirt.png")
    with Image.open(image1) as im:
        photo = ImageOps.fit(im, shirt.size)
        photo.paste(shirt, shirt)
        # Save the image as second argument
        photo.save(image2)
    # return image2

if __name__ == '__main__':
    main()