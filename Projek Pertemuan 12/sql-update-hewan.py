#KONEKSI DB
import sqlite3
koneksi = sqlite3.connect('hewan1.db')
kursor = koneksi.cursor()

#menampilkan semua data dalam database
id_Hewan = 5
jml_skrg = 9000

kursor.execute(f"UPDATE HEWAN SET asal = {id_Hewan} WHERE id_Hewan = {jml_skrg}")
baris_tabel = kursor.fetchall()

if kursor.rowcount > 0:
    print(f"Data hewan dengan id_Hewan {id_Hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan id_Hewan {id_Hewan}.")

#buat tabel pegawai
print("DATA HEWAN 2023")
print("="*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan","nama_hewan","jenis","asal","jml_skrg","thn_ditemukan"))
print("-"*80)

for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0] ,baris[1], baris[2], baris[3], baris[4], baris[5]))

print("-"*80)
koneksi.close()