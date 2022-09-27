import matplotlib.pyplot as plt
from show_image import show_image

foto = plt.imread('foto.jpg')
red = foto[:, :, 0]
plt.hist(red.ravel(), bins=256)
plt.savefig('histograma.png')

histo = plt.imread('histograma.png')
show_image(histo, "tom de vermelho")

