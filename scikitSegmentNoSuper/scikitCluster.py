# Usando Limiarização com Clusterização Iterativa

from skimage.segmentation import slic
from skimage.data import astronaut
from skimage.color import label2rgb
import matplotlib.pyplot as plt

plt.figure(figsize=(15,15))
astronaut = astronaut()

# Applying Simple Linear Iterative
# Clustering on the image
# - 50 segments & compactness = 10
astronaut_segments = slic(astronaut, n_segments=50, compactness=10)
plt.subplot(1,2,1)

# Plotting the original image
plt.imshow(astronaut)
plt.subplot(1,2,2)

# Converts a label image into
# an RGB color image for visualizing
# the labeled regions.
plt.imshow(label2rgb(astronaut_segments, astronaut, kind = 'avg'))
plt.show()
