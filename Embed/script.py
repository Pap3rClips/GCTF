from PIL import Image

image = Image.open('embed.png')
pixels = image.load()
largeur,hauteur = image.size
data = []
print("Lancement de l'analyse de l'image...")
for y in range(hauteur):
    rouge,vert,bleu = pixels[1,y]
    if rouge==255 and vert==255 and bleu==255:
        ligne = []
        for x in range(largeur):
            pixel = []
            rouge,vert,bleu = pixels[x, y]
            pixel.append(rouge)
            pixel.append(vert)
            pixel.append(bleu)
            ligne.append(pixel)
        data.append(ligne)
print("Image analysé")
new_image = Image.new("RGB", (largeur, len(data)))

print("Restructuration de la nouvelle image...")
for index_ligne in range(len(data)):
    for index_pixel in range(len(data[index_ligne])):
        new_image.putpixel((index_pixel,index_ligne), (data[index_ligne][index_pixel][0],data[index_ligne][index_pixel][1],data[index_ligne][index_pixel][2]))
print("affichage des résultats : ")
new_image.show()
