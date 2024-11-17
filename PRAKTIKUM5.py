data = []

while True:
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
    data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])

    add_more = input("Tambah data (y/t)? ")
    if add_more.lower() == 't':
        break

print("-" * 50)
print("| No | Nama | NIM | Tugas | UTS | UAS | Akhir |")
print("-" * 50)
for i, row in enumerate(data):
    print(f"| {i+1} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]:.2f} |")
print("-" * 50)
