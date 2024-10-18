import imageio.v3 as image
import numpy as np

path = "C:\\Users\\febri\\image1.png"
my_image =  image.imread(path)

print(my_image.shape[0])
if(len(my_image.shape) < 3):
    print("Gambarnya harus rgb")
    exit()



red = my_image[:,:,0]
image_red = np.zeros_like(my_image) # Membuat array nol untuk image menjadi warna merah
image_red[:,:,0] = red

grey = my_image[:,:,1]
image_grey = np.zero_like(my_image) # Mmebuat array satu untuk image menjadi warna grey
image_grey[:,:,1] = grey

grey

image.imwrite("C:\\Users\\febri\\image_grey.png", image_grey)
image.imwrite("C:\\Users\\febri\\image1.png", image_red)
print(f"Dimenasi gambar adalah {my_image.shape}")
print(f"Proses Selesai.")
