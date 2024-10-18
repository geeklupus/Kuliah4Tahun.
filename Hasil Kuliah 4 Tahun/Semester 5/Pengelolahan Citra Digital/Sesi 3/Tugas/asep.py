import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    # Konversi RGB ke grayscale menggunakan formula: 0.299R + 0.587G + 0.114B
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

def create_histogram(grayscale_img):
    # Hitung histogram untuk nilai intensitas 0-255
    histogram = np.zeros(256)
    for pixel_value in grayscale_img.flatten():
        histogram[int(pixel_value)] += 1
    return histogram

def plot_histogram(histogram):
    plt.figure(figsize=(12, 6))
    plt.bar(range(256), histogram, color='gray', alpha=0.7)
    plt.title('Histogram Grayscale')
    plt.xlabel('Intensitas Pixel (0-255)')
    plt.ylabel('Jumlah Pixel')
    plt.grid(True, alpha=0.2)
    plt.savefig('histogram_result.png')
    plt.show()

def main():
    # Baca gambar (ganti 'input_image.jpg' dengan nama file gambar Anda)
    image = imageio.imread('input_image.jpg')
    
    # Konversi ke grayscale
    grayscale = rgb_to_grayscale(image)
    
    # Simpan gambar grayscale
    imageio.imwrite('grayscale_image.jpg', grayscale.astype(np.uint8))
    
    # Hitung histogram
    histogram = create_histogram(grayscale)
    
    # Plot dan simpan histogram
    plot_histogram(histogram)
    
    # Analisis hasil
    total_pixels = np.sum(histogram)
    max_intensity = np.argmax(histogram)
    
    print(f"\nHasil Analisis:")
    print(f"Jumlah total pixel: {total_pixels}")
    print(f"\nJumlah pixel untuk setiap intensitas:")
    for i, count in enumerate(histogram):
        if count > 0:  # Hanya tampilkan intensitas yang memiliki pixel
            print(f"Intensitas {i}: {int(count)} pixel")
    
    print(f"\nIntensitas yang paling dominan: {max_intensity}")
    print(f"Jumlah pixel pada intensitas dominan: {int(histogram[max_intensity])}")

if __name__ == "__main__":
    main()