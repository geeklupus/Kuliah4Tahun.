Tugas Kelompok Presentasi
Dengan Teori Keamanan Citra Digital
1 Kelompok 4 - 5 Orang

________________________________________

Segmentasi Citra
ada 2 citra:
1. membagi citra menjadi objek2/klasifikasi dan belum ada partisipasi
2. memisahkan objek dengan background/maka 1 citra diabgi lebih dari 2, objek yg lebih dari 2 (nilai biner) = (forground and background).

citra segmentasi berdasarkan properti yang dipilih seperti kecerahan.
segmentasi jadi jumlah region terhubung tiap region sifatnya homogen. (hijau dan merah segmennya: ada tingkat kemiripan tidak terlalu jauh.)
segmen citra merupakan tahapan sebelum melakukan image/objek recodinition.

partisioning jadi segmen
isolating jadi biner.

Hasil s

Segmentasi
- Quantitaif: ada hubungan dengan angka/jumlah.
- Qualitatif: baik, tidak baik, sangat tidak baik, sangat baik. (Data statistic)
- DETEKSI

Pixel based: 
Region growing: area
Pixel Based Segmentation: Basic Thresholding
- satu abang batas T/Level, S = 100 lebih dari 100 255 sbealiknya 0
Adaptif thresholding: nilai akan berubah2, 
- nilai rata rata ada dibagi beberapa block exited
Range Thresholding
- 

Pengambangan
Pixel disebut titik objek, dan jika tidak 

warna gradian
nilai ambang T:


untuk dapat nilai ambang T:
digabungkan dengan histogram, ada hitam, abu2, putih ada. punya 2 puncak dan lembahnya valleynya jadi bisa threshold dan peak itu background.

nilai


permasalahan global thresholding:

g2: ada beberapa informasi yang hilang


bimodal akan sulit
bagusnya menggunakan multimodal

akan dibagi dilooping dicari rata2, dicek nanti jika g1 lebih besar dari mean maka jadi putih selain itu jadi htiam, harus ganjil tiap block dari gambar contohnya 11 15 19

adaptif threshold:
Otsu method, dengan minimum kelas invarias, nilainya paling kecil itu menjadi solusi.

coba nilai yg level 3, ngikut dari 0,1,2.
3 kiri background 3 kanan forground
8+7+2/36=
6 baris 6 kolom


seat: itu random, umpannya
algoritma bisa dapat warna hijau, itu dapat dari angka2 

Split dan Merge:
- Menggunakan algoristma divide, and conquer
- Citra dibagi split, menjadi sejumlah region yang disjoint

Watershed:
seperti tangki dia akan bergilir ke tangki lain

Clustering:
K-Mean misalkan 3 itu dibagi jadi 3 klustering.

tambahkan disobel dulu, garis tepi nanti hasilnya seperti apa?