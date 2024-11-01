import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width = image.shape[:2]
    max_dim = max(height, width)
    outputImage = np.zeros((max_dim, max_dim, image.shape[2]), dtype=image.dtype)

    center, centerX, centerY = max_dim//2, max_dim//2, max_dim//2

    for y in range(-height//2, height//2):
        for x in range(-width//2, width//2):
            newX = int((cos_deg * x - sin_deg * y) + centerX)
            newY = int((sin_deg * x + cos_deg * y) + centerY)

            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y + height//2, x + width//2]

    return outputImage

image = img.imread('C://LupusKae//image.png')
rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.show()