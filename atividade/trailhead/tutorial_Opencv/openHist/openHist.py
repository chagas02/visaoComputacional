#Criando um histograma de uma imagem P&B

from matplotlib import pyplot as plt
import cv2
img = cv2.imread('rodovia.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem P&B", img)

#Função calcHist para calcular o histograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()

plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")

plt.plot(h)
plt.xlim([0, 256])

plt.savefig("histGray.jpg", format="png" )
plt.show()

cv2.waitKey(0)