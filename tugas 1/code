nilai = []
print ("Masukan nilai mahasiswa : ")

for i in range(10):
    n = float(input(f"Nilai mahasiswa no-{i+1}: "))
    nilai.append(n)

tertinggi = max(nilai)
terendah = min(nilai)
rata = sum(nilai) / len(nilai)

lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

tidak_lulus = len(nilai) - lulus
persen_lulus = (lulus / len(nilai)) * 100
persen_tidak_lulus = (tidak_lulus / len(nilai)) * 100

print("\n...............................................")
print("HASIL PENGELOLAAN NILAI MAHASISWA")
print(".................................................")
print(f"Semua nilai      : {nilai}" )
print(f"Nilai tertinggi: {tertinggi}")
print(f"Nilai terendah: {terendah}")
print(f"Nilai rata-rata: {rata}")
print(f"Jumlah mahasiswa yang lulus: {lulus}")
print(f"Jumlah mahasiswa yang tidak lulus: {tidak_lulus}")
