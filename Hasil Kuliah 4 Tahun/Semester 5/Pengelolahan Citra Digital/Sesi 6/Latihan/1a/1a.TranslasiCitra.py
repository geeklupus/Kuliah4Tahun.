import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)  # Geser vertikal
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Geser horizontal
    
    # Mengisi bagian yang kosong dengan warna hitam
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0
    
    return imgTranslasi

image = img.imread("C://LupusKae//image.png")

imgResult = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.imshow(image)
plt.subplot(2,1,2)
plt.imshow(imgResult)
plt.show()