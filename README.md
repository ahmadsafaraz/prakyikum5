# praktikum5

# Penjelasan Praktikum5
Program di atas adalah program Python yang mengumpulkan data mahasiswa (nama, NIM, nilai tugas, nilai UTS, nilai UAS), menghitung nilai akhir, dan menampilkan hasilnya dalam bentuk tabel. Berikut penjelasan lengkap setiap bagian dari program ini:

# 1. Membuat List data
python
Salin kode
data = []
List data disiapkan untuk menyimpan data mahasiswa, yang akan ditambahkan oleh pengguna.

# 2. Menggunakan Loop while True
while True:
    ...
while True adalah loop yang berjalan terus-menerus sampai pengguna memutuskan untuk berhenti dengan memilih "t" (tidak menambah data lagi).

# 3. Mengambil Input dari Pengguna
Dalam loop, beberapa input diminta dari pengguna:
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))
nama: Nama mahasiswa.
nim: Nomor Induk Mahasiswa, diinput sebagai angka (integer).
nilai_tugas, nilai_uts, nilai_uas: Masing-masing nilai tugas, UTS, dan UAS, juga diinput sebagai angka.

# 4. Menghitung Nilai Akhir
nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
Nilai akhir dihitung berdasarkan bobot masing-masing komponen nilai:
Tugas: 30%
UTS: 35%
UAS: 35%

# 5. Menambahkan Data ke List
data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])
Setiap data mahasiswa disimpan sebagai sebuah list di dalam data dengan format [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir].

# 6. Opsi Menambah Data Lagi
python
Salin kode
add_more = input("Tambah data (y/t)? ")
if add_more.lower() == 't':
    break
Pengguna diberikan opsi untuk menambah data lagi (y untuk ya, t untuk tidak). Jika pengguna memasukkan "t", loop akan berhenti.

# 7. Menampilkan Data dalam Bentuk Tabel
python
Salin kode
print("-" * 50)
print("| No | Nama | NIM | Tugas | UTS | UAS | Akhir |")
print("-" * 50)
for i, row in enumerate(data):
    print(f"| {i+1} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]:.2f} |")
print("-" * 50)
Baris atas dan bawah dari tabel ditampilkan dengan menggunakan "-" * 50 untuk membuat garis horizontal sepanjang 50 karakter.
Loop for dengan enumerate(data) menampilkan setiap data mahasiswa. i+1 digunakan untuk menampilkan nomor urut.
f"{row[5]:.2f}" memastikan nilai akhir ditampilkan dengan dua angka di belakang koma desimal.

Contoh Hasil Program
Jika diinputkan data sebagai berikut:
Nama:Zainal
NIM: 312410215
Nilai Tugas: 80
Nilai UTS: 80
Nilai UAS: 70
Tambah data (y/t)? t

Outputnya:
--------------------------------------------------
| No | Nama |     NIM      | Tugas | UTS | UAS | Akhir |
--------------------------------------------------
| 1  | Zainal  | 312410215 | 80    | 80  | 70  | 76.50 |
--------------------------------------------------

# Kesimpulan
Program ini memudahkan pengguna untuk menginput data nilai mahasiswa, menghitung nilai akhir berdasarkan bobot, dan menampilkannya dalam tabel yang rapi.
