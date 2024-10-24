import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def process_image(image_path, title, figure_num):
    # Membaca gambar
    img = imageio.imread(image_path)
    
    # 1. Memisahkan channel RGB
    red_channel = img.copy()
    red_channel[:, :, (1, 2)] = 0  # Set green dan blue ke 0
    
    green_channel = img.copy()
    green_channel[:, :, (0, 2)] = 0  # Set red dan blue ke 0
    
    blue_channel = img.copy()
    blue_channel[:, :, (0, 1)] = 0  # Set red dan green ke 0
    
    # 2. Konversi ke Grayscale
    grayscale = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    
    # 3. Konversi ke Binary/Threshold
    threshold = 127
    binary = np.where(grayscale >= threshold, 255, 0)
    
    # Plotting dengan figure number yang berbeda untuk setiap gambar
    plt.figure(figure_num, figsize=(15, 10))
    
    # Mengatur style untuk seluruh figure
    plt.style.use('default')
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.weight'] = 'bold'
    
    # Mengatur padding/spacing
    plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0.3, wspace=0.3)
    
    # Original Image
    plt.subplot(231)
    plt.imshow(img)
    plt.title(f'Original {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Red Channel
    plt.subplot(232)
    plt.imshow(red_channel)
    plt.title(f'Red Channel - {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Green Channel
    plt.subplot(233)
    plt.imshow(green_channel)
    plt.title(f'Green Channel - {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Blue Channel
    plt.subplot(234)
    plt.imshow(blue_channel)
    plt.title(f'Blue Channel - {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Grayscale
    plt.subplot(235)
    plt.imshow(grayscale, cmap='gray')
    plt.title(f'Grayscale - {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Binary
    plt.subplot(236)
    plt.imshow(binary, cmap='binary')
    plt.title(f'Binary - {title}', pad=20, fontsize=12, fontweight='bold')
    plt.axis('off')
    
    # Mengatur layout secara keseluruhan
    plt.tight_layout(pad=3.0)
    
    # Menyimpan hasil
    imageio.imwrite(f'output/{title}_red.jpg', red_channel)
    imageio.imwrite(f'output/{title}_green.jpg', green_channel)
    imageio.imwrite(f'output/{title}_blue.jpg', blue_channel)
    imageio.imwrite(f'output/{title}_grayscale.jpg', grayscale.astype(np.uint8))
    imageio.imwrite(f'output/{title}_binary.jpg', binary.astype(np.uint8))

# Memproses ketiga gambar dengan figure number yang berbeda
images = [
    ('DaunPepaya.jpg', 'Daun Pepaya', 1),
    ('Singkong.jpg', 'Singkong', 2),
    ('Kenikir.jpg', 'Kenikir', 3)
]

# Proses setiap gambar
for img_path, title, fig_num in images:
    try:
        process_image(img_path, title, fig_num)
        print(f"Berhasil memproses gambar {title}")
    except Exception as e:
        print(f"Error saat memproses {title}: {str(e)}")

# Menampilkan semua plot
plt.show()