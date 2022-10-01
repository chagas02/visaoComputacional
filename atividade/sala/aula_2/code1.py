from skimage import filters
from skimage.color import rgb2gray
from show_image import show_image
import matplotlib.pyplot as plt

image = plt.imread('imgs/cat.jpg')
gray_image = rgb2gray(image)

thresh = filters.threshold_otsu(gray_image)
binary_image = gray_image <= thresh

show_image(image, 'Original')
show_image(binary_image, 'imagem Binarizada invertida')