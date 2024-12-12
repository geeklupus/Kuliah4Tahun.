Tepi 

menggunakan arah tepi, satuan menggunakan derajat. 97 diartikan radian/derajat.

tepi memiliki arah dengan arah yang berbeda pada ketergantungan oerubahan.

perubahannya 99 (tegak lurus).

tepi biasanya terdapat pada batas antara dua daerab yg beda intensitas


Dimanakah tepi =
contohnya tepi ketika membuat wajah
erosi = dikecilkan
orasi = dibesarkan

diambil fotonya dianalisa di AI

misalkan tanda tangan backgroundnya digunakan.

beberapa jenis tepi:
tepi yang curam: perubahan intensitas yang sangat tajam
contoh: garis itam diatas latar putih.

tepi landai: perubahan tidak terjadi secara mendalam/tajam, lebih cenderung perlahan.

tepi garis: yang terbentuk pada batas objek yang lebih tipis,
garis pada text yang dicetak tipis dua objek.

tepi atap: perubahan intensitas 2 tahap
Contohnya: memiliki gradasi yang lebih halus.

Step
Rump
Line: 
Roof: atap

Matrix
Tepi Curam:
0 tepi curam : putih
1 tepi yang curam : hitam

Tepi Landai
0,1,2,3

Tepi garis
angka 1 dikelilingi oleh angka 0 

Tepi atas: dari akar 
3
2
1
0


ideal: tepi curam
ramp: landai

noise/derau

harus bisa membedakan derau dengan tepi sebenarnya
noise: tidak punya pola.
apakah perbedaannya? (spill dikit2)
dia punya kurfa.

tujuan pendeteksi tepi
-
- pendeteksi tepi mengekstraksi representasi gambar garis2 dicitra
foto: normal, foto: tepian-nya.

berdasarkan bentuk

Analisis citra
1. ekstrakasi ciri:
faktor kunci dalam mengekstraksi ciri adalah kemampuan mendeteksi keberadaan tepi

2. segmentasi
Setelah tepi objek diketahui memisahkan objek dari background baru diklafirikasi.

3. ente

KETURUAN KALKULUS: SOFTWARE PREFIT KOMA, LAVASIAN KETURUNAN DUA.

G(X)
G(Y)

GRADIENT DALAM PENGELOLAHAN citra

GF(GX,GY)

sobel: Gx(horizontal)

Gx: dikasih nilai 0 akan menguatkan tepi. arahnya 90 derajat.
Gy: tinggal ditranfus -1 -2 -1 0 0 0 

prewit:

GY
-1 0 1
-1 0 1

robets 2x2: hasilnya lebih halus lebih ke noise, dianggap sebagai tepian


laplacian(bentuk standar)

(alternatif dengan bobot lebih kuat ditengah)

matrix 3x3 dikalikan kernel prewit dihitung secara 
Gx= -8
Gy= 26
diakar kuadrat
dapat 27.2

arctan (Gy/Gx)

26/-8
-72.6 derajat

Matrix Magnitudo: 27.2

tan-1

tepi berwarna putih sisanya hitam

kemaren yang dicari 1,1 maka dikasih Pad
modenya konstan itu akan tetap
konstan value = 0

dilooping baru digunakan dengan matrix lainnya
yang sebelah tidak diikutkan, saya cari rangenya dicitranya baru dikalikan.
kiri y-1 kekanan y-2, dilakukan normalisasi