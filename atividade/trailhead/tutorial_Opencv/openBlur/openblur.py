#Usando suavização nas imagens

#Usando o blur
import cv2
import numpy as np

img = cv2.imread('rodovia.png')
img = img[::2,::2] # Diminui a imagem
suave = np.vstack([   np.hstack([img,cv2.blur(img, ( 3,  3))]),np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7,  7))]),np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),])
cv2.imshow("Imagens suavisadas (Blur)", suave)
cv2.imwrite("blur.jpg", suave)
cv2.waitKey(0)

#usando o medianBlur

import numpy as np
import cv2
img = cv2.imread('ponte.jpg')
img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
np.hstack([img,
cv2.medianBlur(img,  3)]),
np.hstack([cv2.medianBlur(img,  5),
cv2.medianBlur(img,  7)]),
np.hstack([cv2.medianBlur(img,  9),
cv2.medianBlur(img, 11)]),
])
cv2.imshow("Imagem original e suavizadas pela mediana", suave)
cv2.waitKey(0)

