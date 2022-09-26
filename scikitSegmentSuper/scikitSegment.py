#Segmentação por Limiarização - Parametrização manual

from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

coffee = data.coffee()
gray_coffee = rgb2gray(coffee)

plt.figure(figsize=(10, 10))

for i in range(10):
     # Iterating different thresholds
    binarized_gray = (gray_coffee > i*0.1)*1
    plt.subplot(5, 2, i+1)

 # Rounding of the threshold
 # value to 1 decimal point

    plt.title("Threshold: >"+str(round(i*0.1,1)))
# Displaying the binarized image
# of various thresholds

    plt.imshow(binarized_gray, cmap = 'gray')
plt.tight_layout()
plt.show()