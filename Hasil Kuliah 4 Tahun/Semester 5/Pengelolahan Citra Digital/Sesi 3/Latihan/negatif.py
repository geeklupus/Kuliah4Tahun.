import imageio as img
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\negatiff.jpg"

imgNegatif = img.imread(path)
redNegatif = imgNegatif[:,:,0]
rN_hist, bins = np.histogram(redNegatif.flatten(),bins=256,range=[0,256])

imgPositif = img.imread(path)
greenPositif = imgPositif[:,:,1]
rP_hist, bins = np.histogram(greenPositif.flatten(),bins=256,range=[0,256])

rnormalized = rN_hist/rN_hist.sum()
rpnormalized = rP_hist/rP_hist.sum()

imgPositif = 255 - imgNegatif

plt.figure(figsize=(10,10))

plt.subplot(3,2,1)
plt.imshow(imgNegatif)

plt.subplot(3,2,2)
plt.imshow(imgPositif)

plt.subplot(3,2,3)
plt.plot(rN_hist, color='red')

plt.subplot(3,2,4)
plt.plot(rP_hist, color='green')

plt.subplot(3,2,5)
plt.plot(rnormalized, color='red')

plt.subplot(3,2,6)
plt.plot(rpnormalized, color='green')

plt.tight_layout()
plt.show()