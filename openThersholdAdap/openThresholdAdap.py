#Usando o threshold adaptativo

import cv2
import numpy as np

img = cv2.imread('rodovia.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (7, 7), 0)

bin1 = cv2.adaptiveThreshold(suave, 255,  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21, 5)

resultado = np.vstack([  np.hstack([img, suave]),  np.hstack([bin1, bin2])  ])

cv2.imshow("Binarização adaptativa da imagem", resultado)
cv2.imwrite('thresholding.jpg', resultado)
cv2.waitKey(0)