import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def mirrorImage(image):
    height, width = image.shape[:2]
    mirrored_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            mirrored_image[y, x] = image[height - 1 - y, width - 1 - x]

    return mirrored_image

image = img.imread('C://LupusKae//image.png')
mirrored_image = mirrorImage(image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(mirrored_image)
plt.show()