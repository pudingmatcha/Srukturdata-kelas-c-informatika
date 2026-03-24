//code niali tertinggi dan terendah//

import matplotlib.pyplot as plt

nilai = [70, 74, 50, 60, 80, 90, 75, 95, 80, 85]

tertinggi = max(nilai)
terendah = min(nilai)

kategori = ["Nilai Tertinggi", "Nilai Terendah"]
data = [tertinggi, terendah]

plt.bar(kategori, data)

plt.title("Grafik Nilai Tertinggi dan Terendah Mahasiswa")
plt.ylabel("Nilai")

plt.show()


//code kelulusan//

import matplotlib.pyplot as plt

nilai = [70, 74, 50, 60, 80, 90, 75, 95, 80, 85]

lulus = 0
tidak_lulus = 0

for n in nilai:
    if n >= 60:
        lulus += 1
    else:
        tidak_lulus += 1

kategori = ["Lulus", "Tidak Lulus"]
data = [lulus, tidak_lulus]

plt.bar(kategori, data)

plt.title("Grafik Kelulusan Mahasiswa")
plt.ylabel("Jumlah Mahasiswa")

plt.show()
