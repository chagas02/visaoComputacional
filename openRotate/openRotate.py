#Rotacionando uma imagem

import cv2
img = cv2.imread('rodovia.png')

(alt, lar) = img.shape[:2]  # captura altura e largura
centro = (lar // 2, alt // 2)  # acha o centro

M = cv2.getRotationMatrix2D(centro, 50, 2.0)

img_rotacionada = cv2.warpAffine(img, M, (lar, alt))

cv2.imshow("Imagem rotacionada ", img_rotacionada)
cv2.imwrite("rotacionada.jpg", img_rotacionada)
cv2.waitKey(0)
