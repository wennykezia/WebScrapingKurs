# Web Scraping Kurs JPY 2019

Proses web scraping ini bersumber dari website : monexnews.com/kurs-valuta-asing.htm?kurs=JPY ,

dilakukan dengan tujuan untuk mengamati pergerakan kurs JPY (mata uang Jepang) pada tahun 2019. Hasil akhir dari kegiatan ini berupa plot/diagram yang menampilkan nilai rata-rata kurs JPY tiap bulannya.

___

**Proses** : 
- Menyiapkan environment baru dan library yang diperlukan : beautifulSoup4, pandas, flask, dan matplotlib
- GET data dari tampilan website
- Mengubah data menjadi dataframe
- Melakukan data wrangling
- Analisa hasil olahan data

**Hasil Analisa** : 
Nilai rata-rata Bid dan Ask tiap bulannya berada pada range yang berdekatan, sedangkan fluktuasi nilainya cenderung berubah-ubah. Nilai tertinggi berada pada bulan Agustus dan terendah di bulan April. Akan tetapi dari Agustus hingga akhir tahun nilainya terus menerus turun, bahkan hingga nilainya lebih rendah dari nilai di bulan pertama tahun 2019. Keadaan ini menandakan adanya ketidakstabilan nilai jual-beli mata uang Yen sepanjang tahun 2019.

