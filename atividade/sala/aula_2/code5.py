from atividade.sala.src.pdi_utils import show_image, load_aerial_image
from scipy.stats import entropy
import matplotlib.pyplot as plt
import numpy as np
import cv2

def compute_entropy(labels, base= None):
    value,counts = np.unique(labels, return_counts= True)
    return entropy(counts, base=base)

image_aerial = cv2.imread('imgs/aerial.png')
gray_aerial = cv2.cvtColor(image_aerial, cv2.COLOR_BGR2GRAY)

# calcular e mostrar o histograma da imagem
hist_n_eq = plt.hist(gray_aerial.ravel(), bins= 256)
plt.show()

#realizar a equalização do histograma
image_eq = cv2.equalizeHist(gray_aerial)

# calcular e mostrar o histograma da imagem equalizada
hist_eq = plt.hist(image_eq.ravel(), bins=256)
plt.show()

# determinar a media do valor dos pixels que ocorrem na imagem não equalizada
x = compute_entropy(image_aerial, base=None)*255

print(x)



