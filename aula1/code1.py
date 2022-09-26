# Importando os módulos
from skimage import data, color
import matplotlib.pyplot as plt

# Definindo a função show_image
def show_image(image, title='image', cmap_type= 'gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Carreagando a imagem
rocket = data.rocket()

# Convertendo a imagem para a escla de cinza
imagemCinza = color.rgb2gray(rocket)

# Mostrando a imagem Original e na escala de cinza usando a função show_image
show_image(rocket, "Original")
show_image(imagemCinza, "Escala de cinza")

