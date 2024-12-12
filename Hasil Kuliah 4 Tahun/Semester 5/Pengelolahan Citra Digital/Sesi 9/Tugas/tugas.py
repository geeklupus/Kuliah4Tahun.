import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Fungsi untuk menerapkan operator Roberts
def roberts_edge_detection(image):
    # Kernel Roberts
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    
    # Menggunakan konvolusi
    gx = convolve(image, kernel_x)
    gy = convolve(image, kernel_y)
    
    # Menghitung magnitude
    edges = np.hypot(gx, gy)
    edges = edges / edges.max()  # Normalisasi
    return edges

# Fungsi untuk menerapkan operator Sobel
def sobel_edge_detection(image):
    # Kernel Sobel
    kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    
    # Menggunakan konvolusi
    gx = convolve(image, kernel_x)
    gy = convolve(image, kernel_y)
    
    # Menghitung magnitude
    edges = np.hypot(gx, gy)
    edges = edges / edges.max()  # Normalisasi
    return edges

# Membaca gambar dan mengubahnya menjadi grayscale
image = imageio.imread('C:\\LupusKae\\image.png')
if image.ndim == 3:  # Jika gambar berwarna
    image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Konversi ke grayscale

# Menerapkan deteksi tepi
edges_roberts = roberts_edge_detection(image)
edges_sobel = sobel_edge_detection(image)

# Menampilkan hasil
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Edges - Roberts')
plt.imshow(edges_roberts, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Edges - Sobel')
plt.imshow(edges_sobel, cmap='gray')
plt.axis('off')

plt.show()