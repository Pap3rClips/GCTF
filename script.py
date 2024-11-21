from PIL import Image

image = Image.open('embed.png')
largeur, hauteur = image.size
new_image = Image.new(mode='RGB', size=(largeur, 10000))

for pixel_y in range(hauteur):
    if image.getpixel((1, pixel_y)) == (255, 255, 255):
        for pixel_x in range(largeur):
            new_image.putpixel((pixel_x, pixel_y), image.getpixel((pixel_x, pixel_y)))
            print("pixel added !")


new_image.save('new.png')