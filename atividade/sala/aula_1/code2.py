import numpy as np
import matplotlib.pyplot as plt
from show_image import show_image

foto = plt.imread('foto.jpg')
foto_vertical = np.flipud(foto)
foto_horizontal = np.fliplr(foto)

show_image(foto, "Original")
show_image(foto_vertical, "Foto na vertical")
show_image(foto_horizontal, "Foto na horizontal")
