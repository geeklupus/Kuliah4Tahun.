import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menerapkan filter
def apply_filters(image):
    # Low-pass filter (Gaussian Blur)
    low_pass = cv2.GaussianBlur(image, (5, 5), 0)
    
    # High-pass filter (menggunakan Laplacian)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    high_pass = cv2.convertScaleAbs(laplacian)

    # High-boost filter
    high_boost = cv2.addWeighted(image, 1.5, low_pass, -0.5, 0)

    return low_pass, high_pass, high_boost

# Memuat citra
image_color = cv2.imread('image_color.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Menerapkan filter pada citra grayscale
low_pass_gray, high_pass_gray, high_boost_gray = apply_filters(image_gray)

# Menerapkan filter pada citra berwarna
low_pass_color, high_pass_color, high_boost_color = apply_filters(image_color)

# Menampilkan hasil
plt.figure(figsize=(12, 8))

# Citra Grayscale
plt.subplot(2, 4, 1)
plt.title('Citra Grayscale')
plt.imshow(image_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.title('Low-pass (Grayscale)')
plt.imshow(low_pass_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.title('High-pass (Grayscale)')
plt.imshow(high_pass_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.title('High-boost (Grayscale)')
plt.imshow(high_boost_gray, cmap='gray')
plt.axis('off')

# Citra Berwarna
plt.subplot(2, 4, 5)
plt.title('Citra Berwarna')
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 4, 6)
plt.title('Low-pass (Berwarna)')
plt.imshow(cv2.cvtColor(low_pass_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 4, 7)
plt.title('High-pass (Berwarna)')
plt.imshow(cv2.cvtColor(high_pass_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 4, 8)
plt.title('High-boost (Berwarna)')
plt.imshow(cv2.cvtColor(high_boost_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()