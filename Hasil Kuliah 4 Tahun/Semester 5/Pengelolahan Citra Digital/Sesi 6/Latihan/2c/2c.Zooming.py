import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    zoomed_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)
            zoomed_image[y, x] = image[ori_y, ori_x]

    return zoomed_image

image = img.imread('C://LupusKae//image.png')
zoomed_image = zoomMinus(image, 2.0)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(zoomed_image)
plt.show()