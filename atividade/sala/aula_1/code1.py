from skimage import data, color
from show_image import show_image

rocket = data.rocket()
imagemCinza = color.rgb2gray(rocket)

show_image(rocket, "Original")
show_image(imagemCinza, "Escala de cinza")

