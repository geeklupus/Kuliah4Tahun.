import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def localThres(image, block_size, c):
    imgPad = np.pad(image, pad_width=block_size//2, mode='constant', constant_values=0)
    threshold = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+block_size, j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i, j] = 255 if image[i, j] > (local_mean - c) else 0

    return threshold

# Membaca gambar
image_path = 'C:/LupusKae/image.png'
image1 = img.imread(image_path, as_gray=True)

# Memanggil fungsi dengan parameter yang sesuai
thres = localThres(image1, 15, 10)

# Menampilkan hasil
plt.figure(figsize=(10, 10))
plt.subplot(1, 3, 1)
plt.imshow(image1, cmap="gray")
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(thres, cmap="gray")
plt.title("Thresholded Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(image1, cmap="gray")
plt.title("Original Image Again")
plt.axis('off')

plt.show()