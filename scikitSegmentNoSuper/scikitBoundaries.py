# Usando Mark Boundaries

import matplotlib.pyplot as plt
from skimage.segmentation import slic, mark_boundaries
from skimage.data import astronaut

plt.figure(figsize=(15, 15))
astronaut = astronaut()

# Applying SLIC segmentation for the edges to be drawn over
astronaut_segments = slic(astronaut, n_segments=100, compactness=1)
plt.subplot(1, 2, 1)

# Plotting the original image
plt.imshow(astronaut)

# Detecting boundaries for labels
plt.subplot(1, 2, 2)

# Plotting the ouput of marked_boundaries
# function i.e. the image with segmented boundaries
plt.imshow(mark_boundaries(astronaut, astronaut_segments))
plt.show()