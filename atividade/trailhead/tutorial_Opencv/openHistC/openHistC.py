#Histograma de uma imagem colorida

from matplotlib import pyplot as plt
import cv2

img = cv2.imread('rodovia.png')
cv2.imshow("Imagem Colorida", img)

canais = cv2.split(img)
cores = ("b", "g", "r")

plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")

i=0
for (canal, cor) in zip(canais, cores):
#Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cor)
    plt.xlim([0, 256])
    plt.savefig('histcolor%01i.jpg' %i, format="png")
    plt.show()
    i+=1