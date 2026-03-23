# penjelasan program yang dibuat

Program dimulai dengan membuat sebuah list kosong bernama nilai untuk menyimpan nilai mahasiswa. Proses ini sangat cepat karena hanya membuat tempat penyimpanan data, sehingga kompleksitasnya O(1). Selanjutnya program melakukan perulangan sebanyak 10 kali untuk meminta input nilai mahasiswa. Pada setiap perulangan, program menerima nilai dari pengguna lalu menambahkannya ke dalam list. Karena proses ini dilakukan sebanyak jumlah data yang dimasukkan, maka kompleksitasnya adalah O(n), di mana n adalah jumlah mahasiswa.

<p align="center">
  <img src="https://github.com/pudingmatcha/Srukturdata-kelas-c-informatika/blob/main/gambar/Screenshot%202026-03-23%20140235.png" width="750">
</p>

Setelah semua nilai dimasukkan, program mencari nilai tertinggi menggunakan fungsi max(). Fungsi ini harus memeriksa semua nilai dalam list untuk menentukan nilai terbesar, sehingga kompleksitasnya O(n). Kemudian program mencari nilai terendah menggunakan fungsi min(). Sama seperti sebelumnya, fungsi ini juga memeriksa semua data dalam list sehingga kompleksitasnya O(n). Program lalu menghitung nilai rata-rata dengan menjumlahkan semua nilai menggunakan sum() dan membaginya dengan jumlah data menggunakan len(). Proses penjumlahan semua nilai memerlukan pemeriksaan seluruh data sehingga kompleksitasnya O(n). Setelah itu program menghitung jumlah mahasiswa yang lulus dengan melakukan perulangan pada semua nilai. Jika nilai lebih besar atau sama dengan 60, maka mahasiswa dianggap lulus. Karena program memeriksa setiap nilai satu per satu, kompleksitasnya juga O(n). Kemudian program menghitung jumlah mahasiswa yang tidak lulus dengan mengurangi jumlah total mahasiswa dengan jumlah yang lulus. Proses ini hanya operasi matematika sederhana sehingga kompleksitasnya O(1). Program juga menghitung persentase mahasiswa yang lulus dan tidak lulus menggunakan operasi pembagian dan perkalian sederhana. Proses ini juga memiliki kompleksitas O(1) karena tidak memerlukan perulangan. Terakhir, program menampilkan semua hasil seperti daftar nilai, nilai tertinggi, nilai terendah, rata-rata nilai, jumlah mahasiswa yang lulus, dan jumlah yang tidak lulus. Proses menampilkan hasil ini juga cepat sehingga kompleksitasnya O(1).

<p align="center">
  <img src="https://github.com/pudingmatcha/Srukturdata-kelas-c-informatika/blob/main/gambar/Screenshot%202026-03-23%20140248.png" width="750">
</p>

Secara keseluruhan, kompleksitas waktu dari program ini adalah O(n) karena sebagian besar proses utama seperti input nilai, mencari nilai maksimum, minimum, menghitung rata-rata, dan menentukan kelulusan harus memeriksa seluruh data nilai mahasiswa. Artinya, semakin banyak data mahasiswa yang dimasukkan, maka waktu yang dibutuhkan program juga akan bertambah secara sebanding (linear) dengan jumlah data tersebut.

Setelah dibuatnya perhitungan terhadap nilai mahasiswa dapat disimpulkan juga dalam bentuk grafik sebagai berikut:

<p align="center">
  <img src="https://github.com/pudingmatcha/Srukturdata-kelas-c-informatika/blob/main/gambar/Screenshot%202026-03-23%20233710.png" width="750">
</p>

<p align="center">
  <img src="https://github.com/pudingmatcha/Srukturdata-kelas-c-informatika/blob/main/gambar/Screenshot%202026-03-23%20233721.png" width="750">
</p>

Berdasarkan grafik yang ditampilkan, dapat dilihat bahwa nilai tertinggi yang diperoleh mahasiswa adalah 95, sedangkan nilai terendah adalah 50. Rata-rata nilai mahasiswa adalah 75,9, yang menunjukkan bahwa secara umum nilai mahasiswa cukup baik. Dari total 10 mahasiswa, terdapat 9 mahasiswa yang lulus dan 1 mahasiswa yang tidak lulus.

# Dibuat oleh : Pande Putu Vidya Reswara
# NIM : 2501010064
