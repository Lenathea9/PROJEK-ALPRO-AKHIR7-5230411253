#KONEKSI DB
import sqlite3
koneksi = sqlite3.connect('hewan1.db')

#Buat Database dan Table Pegawai
koneksi.execute('''
                CREATE TABLE HEWAN(
                 id_Hewan : PRIMARY KEY,INTEGER,AUTOINCREMENT,
                 nama_hewan VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jml_skrg INTEGER(10),
                 thn_ditemukan INTEGER(10)
                )
                ''')
koneksi.close()