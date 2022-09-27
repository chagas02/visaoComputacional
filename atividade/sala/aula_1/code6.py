from skimage.filters import try_all_threshold
from skimage import color
import cv2
import matplotlib.pyplot as plt

mulher = cv2.imread('mulher.jpg')
mulher_gray = color.rgb2gray(mulher)

fig, ax = try_all_threshold(mulher_gray, figsize=(8, 6), verbose= False)
plt.show()

