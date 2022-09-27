from show_image import show_image
import cv2
from skimage.filters import threshold_otsu
from skimage import color
import matplotlib.pyplot as plt

foto = cv2.imread('mulher.jpg')
foto_gray = color.rgb2gray(foto)

thresh = 127
thresh = threshold_otsu(foto_gray)
binary_global = foto_gray > thresh

show_image(foto_gray, 'Original')
show_image(binary_global, 'Binarizada')