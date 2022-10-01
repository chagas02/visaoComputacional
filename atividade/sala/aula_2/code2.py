from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from show_image import show_image
import cv2
import numpy as np

soaps = plt.imread('imgs/soaps.jpg')
gray_soaps= rgb2gray(soaps)

sobelX = cv2.Sobel(gray_soaps, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray_soaps, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

edge_sobel = cv2.bitwise_or(sobelX, sobelY)

show_image(soaps, 'Original')
show_image(sobelX, 'sobel horizontal')
show_image(sobelY, 'sobel vertical')
show_image(edge_sobel, 'imagem com filtro Sobel')