#KONEKSI DB
import sqlite3
koneksi = sqlite3.connect('hewan1.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM(jml_skrg) FROM HEWAN")
#MENGAMBILL SATU BARIS jml skrg SAJA FETCHONE() DIMULAI DARI INDEKS 0
jml_skrg = kursor.fetchone()[0]

print(f"Total jml_skrg: {jml_skrg}")
kursor.close()