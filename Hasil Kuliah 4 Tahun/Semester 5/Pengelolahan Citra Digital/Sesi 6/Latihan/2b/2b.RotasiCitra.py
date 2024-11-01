import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    height, width = image.shape[:2]
    max_dim = max(height, width)
    rotated_image = np.zeros((max_dim, max_dim, image.shape[2]), dtype=image.dtype)

    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    for y in range(-height//2, height//2):
        for x in range(-width//2, width//2):
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)
            newX += width//2
            newY += height//2

            if 0 <= newX < width and 0 <= newY < height:
                rotated_image[y + height//2, x + width//2] = image[newY, newX]

    return rotated_image

image = img.imread('C://LupusKae//image.png')
rotated_image = rotateImage(image, 45)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.show()