#Sistema de cores: GRAY, HSV E LAB

import cv2

img = cv2.imread('rodovia.png')
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.imwrite("tomDeCinza.jpg", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.imwrite("sistemaHSV.jpg", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.imwrite("sistemaLAB.jpg", lab)

cv2.waitKey(0)

#Separando canais e exibindo-os de forma predominante

import numpy as np

(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
vermelho = cv2.merge([zeros, zeros, canalVermelho])
cv2.imwrite("vermelho.jpg", vermelho)

cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
verde = cv2.merge([zeros, canalVerde, zeros])
cv2.imwrite("verde.jpg", verde)

cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
azul = cv2.merge([canalAzul, zeros, zeros])
cv2.imwrite("azul.jpg", azul)

cv2.waitKey(0)
