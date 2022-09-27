#Criando uma nova imagem a partir do recorte da imagem original
import cv2
imagem = cv2.imread('rodovia.png')
recorte = imagem[100:300, 100:200] #aqui fica os parâmetros do recorte.
cv2.imshow("Original", imagem)
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey(0)
cv2.imwrite("recorte.jpg", recorte)