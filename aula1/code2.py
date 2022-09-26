import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title='image', cmap_type= 'gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

foto = plt.imread('foto.jpg')
foto_vertical = np.flipud(foto)
foto_horizontal = np.fliplr(foto)

show_image(foto, "Original")
show_image(foto_vertical, "Foto na vertical")
show_image(foto_horizontal, "Foto na horizontal")
