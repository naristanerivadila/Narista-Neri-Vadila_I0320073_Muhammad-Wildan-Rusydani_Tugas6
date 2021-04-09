print("SOAL 2")
print("Membuat program menghitung nilai rata-rata dari nilai yang diinput oleh user dengan menggunakan perintah "
      "perulangan FOR atau WHILE ")

#inputkan banyak data
n = int(input("Masukkan banyak data : "))

print()
data = []
jumlah = 0

for i in range(0,n):
    nilai = int(input("Masukkan data ke-%d: " %(i+1)))
    data.append(nilai)
    jumlah += data[i]
    rata_rata = float(jumlah/n)

print("Rata-rata = %0.2f" % rata_rata)



