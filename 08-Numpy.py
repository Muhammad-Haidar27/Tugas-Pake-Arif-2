import numpy as np
import pandas as pd

df = pd.read_csv("dataset_penjualan_kantin.csv")

# 1. Data Loading Dan Inspection
print("\n--- 5 Baris Pertama")
print(df.head())

print("\n Info Dataset")
df.info()

# 2. Konversi data ke numerik lebih awal
df["jumlah_terjual"] = (
    pd.to_numeric(df["jumlah_terjual"], errors="coerce").fillna(0).astype(int)
)
df["harga_satuan"] = pd.to_numeric(df["harga_satuan"], errors="coerce")

# 3. Hapus baris jika harga_satuan atau nama_kasir bernilai NaN
df = df.dropna(subset=["harga_satuan", "nama_kasir"])

# 4. Hapus duplikat
df = df.drop_duplicates().reset_index(drop=True)

# 5. Hitung kolom turunan (sudah bebas dari NaN)
df["total_pendapat"] = df["harga_satuan"] * df["jumlah_terjual"]
print("Total Pendapatan:")
print(df["total_pendapat"])

# 6. Mencari Menu Mahal (> 10000)
mahal = df[df["harga_satuan"] > 10000]
print("\nMenu Mahal:")
print(mahal)

# 7. Membuat Ringkasan (Groupby)
ringkasan = df.groupby("nama_produk")["total_pendapat"].sum()
print("\nRingkasan Pendapatan per Produk:")
print(ringkasan)

# 8. Menyesuaikan semua tanggal agar formatnya sama
bulan_indo = {
    "Januari": "January",
    "Februari": "February",
    "Maret": "March",
    "April": "April",
    "Mei": "May",
    "Juni": "June",
    "Juli": "July",
    "Agustus": "August",
    "September": "September",
    "Oktober": "October",
    "November": "November",
    "Desember": "December",
}

tanggal_clean = df["tanggal"].astype(str)
for indo, eng in bulan_indo.items():
  tanggal_clean = tanggal_clean.str.replace(indo, eng, regex=False)

df["tanggal"] = pd.to_datetime(
    tanggal_clean, format="mixed", dayfirst=True, errors="coerce"
).dt.strftime("%Y-%m-%d")

# 9. Menampilkan Dataset Bersih
# Simpan DataFrame yang sudah bersih ke file CSV baru
df.to_csv("dataset_kantin_bersih.csv", index=False)
print("File 'dataset_kantin_bersih.csv' berhasil dibuat!")

# ==============================================================================
# HASIL PENGISIAN FORMULIR PERENCANAAN PROYEK ANALISIS DATA KANTIN
# (Silakan copy-paste seluruh teks komentar ini langsung ke file Python kamu)
# ==============================================================================

# Nama Anggota Kelompok: 
# Erfano Alfarrezal Raditya & Muhammad Haidar Kurnia Akbar

# Dataset yang Dipilih: 
# [X] dataset_penjualan_kantin.csv

# Pertanyaan Analisis Awal:
# 1. Menu makanan/minuman apa yang menghasilkan total pendapatan tertinggi?
# 2. Menu apa saja yang paling laris berdasarkan jumlah porsi yang terjual?
# 3. Berapa total pendapatan kantin berdasarkan kategori produk?

# Dugaan Masalah Kualitas Data:
# - Missing value pada kolom: jumlah_terjual, harga_satuan, nama_kasir
# - Duplikat data: Terdapat baris data duplikat dalam dataset
# - Tipe data tidak sesuai pada kolom: jumlah_terjual dan harga_satuan (terbaca sebagai object/string)

# Rencana Teknik Pembersihan:
# - Mengisi nilai NaN pada kolom jumlah_terjual dengan angka 0 menggunakan fillna(0)
# - Menghapus baris bernilai NaN pada kolom harga_satuan dan nama_kasir menggunakan dropna(subset=[...])
# - Menghapus baris duplikat menggunakan drop_duplicates()
# - Mengonversi tipe data jumlah_terjual dan harga_satuan ke numerik menggunakan pd.to_numeric()

# Rencana Manipulasi Data:
# - Filter: Menyaring produk mahal (harga_satuan > 10000) atau produk laris (jumlah_terjual > 20)
# - Sort: Mengurutkan transaksi berdasarkan penjualan terbanyak (sort_values(by='jumlah_terjual', ascending=False))
# - Kolom turunan: Membuat kolom total_pendapat (harga_satuan * jumlah_terjual)
# - Groupby/agregasi: Mengelompokkan data berdasarkan nama_produk untuk menghitung total pendapatan (df.groupby('nama_produk')['total_pendapat'].sum())

# Jadwal Kerja:
# P3 (Loading & Inspection): Selesai | P4 (Cleaning): Selesai | P5 (Manipulation): Selesai | P6 (Uji & Presentasi): -