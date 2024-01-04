#KONEKSI DB
import sqlite3
koneksi = sqlite3.connect('hewan1.db')
kursor = koneksi.cursor()

#menampilkan semua data dalam database
nama_hewan = 'O%' 
kursor.execute(f"SELECT * FROM HEWAN WHERE nama_hewan LIKE ?", (nama_hewan,))
baris_tabel = kursor.fetchall()
#buat tabel HEWAN
print("DATA HEWAN 2023")
print("="*80)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan","nama_hewan","jenis","asal","jml_skrg","thn_ditemukan"))
print("-"*80)

for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0] ,baris[1], baris[2], baris[3], baris[4], baris[5]))

print("-"*80)
koneksi.close()