import matplotlib.pyplot as plt
from atividade.sala.src.pdi_utils import show_image, load_chest_ray_x
import cv2
from skimage import exposure
from skimage.color import rgb2gray


chest_xray_image = cv2.imread('imgs/contrast_00000109_005.png')
chest_gray = cv2.cvtColor(chest_xray_image, cv2.COLOR_BGR2GRAY)

show_image(chest_gray, 'Original x-ray')
plt.title('Histogram of image')
plt.hist(chest_gray.ravel(), bins=255)
plt.show()

# Use histogram equalization to improve the contrast
#xray_image_eq = cv2.equalizeHist(chest_gray)
xray_image_eq = exposure.equalize_hist(chest_gray)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')

# Show the histogram equalized
plt.hist(xray_image_eq.ravel(), bins=300)
plt.show()