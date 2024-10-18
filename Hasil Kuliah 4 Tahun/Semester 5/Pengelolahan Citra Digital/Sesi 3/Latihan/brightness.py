import imageio as img
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk mengubah kecerahan
def bright(image, factor):
    imgBright = image.astype(np.float32)
    imgBright = imgBright + factor
    imgBright = np.clip(imgBright, 0, 255)
    return imgBright.astype(np.uint8)

# Fungsi untuk mengubah kontras
def constrast(image, factor):
    mean = 128
    imgContrast = image.astype(np.float32)
    imgContrast = mean + factor * (imgContrast - mean)
    imgContrast = np.clip(imgContrast, 0, 255)
    return imgContrast.astype(np.uint8)

# Menghindari warning dengan menggunakan imageio v2
import imageio.v2 as img

# Membaca gambar dari path
path = "C:\\image.png"
image = img.imread(path)

# Menerapkan fungsi bright dan constrast
imgBright = bright(image, 50)
imgContrast = constrast(image, 1.5)

# Menampilkan gambar asli, gambar dengan kecerahan ditingkatkan, dan gambar dengan kontras diubah
plt.figure(figsize=(10, 10))

# Menampilkan gambar asli
plt.subplot(3, 1, 1)  # Menggunakan grid 3x1
plt.imshow(image)
plt.title('Gambar Asli')

# Menampilkan gambar dengan kecerahan ditingkatkan
plt.subplot(3, 1, 2)  # Subplot ke-2 dari 3
plt.imshow(imgBright)
plt.title('Gambar dengan Kecerahan Ditingkatkan')

# Menampilkan gambar dengan kontras diubah
plt.subplot(3, 1, 3)  # Subplot ke-3 dari 3
plt.imshow(imgContrast)
plt.title('Gambar dengan Kontras Ditingkatkan')

plt.tight_layout()
plt.show()
