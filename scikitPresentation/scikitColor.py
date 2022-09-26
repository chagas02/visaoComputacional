#Convertendo o formato da imagem
#As imagens utilizadas são da própria biblioteca


from skimage import data;
from skimage.color import rgb2gray, rgb2hsv;
import matplotlib.pyplot as plt;

# Setting the plot size to 15,15;
plt.figure(figsize=(30, 30));

coffee = data.coffee()
plt.subplot(1, 2, 1)

plt.imshow(coffee)

gray_coffee = rgb2gray(coffee)
plt.subplot(1, 2, 2)

plt.imshow(gray_coffee, cmap="gray")
plt.show()

#RGB para HSV

plt.figure(figsize=(15, 15))

coffee = data.coffee()
plt.subplot(1, 2, 1)

plt.imshow(coffee)

hsv_coffee = rgb2hsv(coffee)
plt.subplot(1, 2, 2)

hsv_coffee_colorbar = plt.imshow(hsv_coffee)
plt.colorbar(hsv_coffee_colorbar, fraction=0.046, pad=0.04)
plt.show()