from skimage import color
from skimage.filters import threshold_otsu, threshold_local
import cv2
import matplotlib.pyplot as plt
from show_image import show_image

# Preparando imagem
mulher = cv2.imread("mulher.jpg")
mulher_gray = color.rgb2gray(mulher)

# Limiarização Global
global_thresh = threshold_otsu(mulher_gray)
binary_global = mulher_gray > global_thresh # se usar <= está inventendo a binarização.


# Limiarização Local
block_size = 45
local_thresh = threshold_local(mulher_gray, block_size)
binary_local = mulher_gray > local_thresh


# Demonstração das imagens processadas
show_image(mulher_gray, "Escala de cinza")
show_image(binary_local, "Binarização local")
show_image(binary_global, "Binarização Global")

plt.savefig('limiarGlobal.jpg') # // salvou imagem em branco