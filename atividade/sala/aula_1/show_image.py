import matplotlib.pyplot as plt

def show_image(image, title='image', cmap_type= 'gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()