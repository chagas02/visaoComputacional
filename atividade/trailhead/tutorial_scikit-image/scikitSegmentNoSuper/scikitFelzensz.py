# Usando segmentação de Felzenswalb

from skimage.segmentation import felzenszwalb, mark_boundaries
from skimage.data import astronaut
import matplotlib.pyplot as plt

plt.figure(figsize=(15,15))
astronaut = astronaut()

# computing the Felzenszwalb's
# Segmentation with sigma = 5 and minimum
# size = 100
astronaut_segments = felzenszwalb(astronaut, scale = 2, sigma=5, min_size=100)

plt.subplot(1,2,1)
plt.imshow(astronaut)
plt.show()

# Marking the boundaries of
# Felzenszwalb's segmentations
plt.subplot(1,2,2)
plt.imshow(mark_boundaries(astronaut, astronaut_segments))
plt.show()