import imageio as img
import numpy as np
import matplotlib.pyplot as plt

image = img.imread("C:/LupusKae/najla.jpg")

sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobelY = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 0, 1]
])

imgPad = np.pad(sobelX,pad_width=1,mode='constant',constant_values=0)
print(imgPad)
