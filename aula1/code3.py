import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title='image', cmap_type= 'gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

foto = plt.imread('foto.jpg')
red = foto[:, :, 0]
plt.hist(red.ravel(), bins=256)

# show_image(foto, "Original")
show_image(red, "tom de vermelho")

