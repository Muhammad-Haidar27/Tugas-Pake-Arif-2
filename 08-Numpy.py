import numpy as np
import pandas as pd

df = pd.read_csv("dataset_penjualan_kantin.csv")

# 1. Konversi data ke numerik lebih awal
df["jumlah_terjual"] = (
    pd.to_numeric(df["jumlah_terjual"], errors="coerce").fillna(0).astype(int)
)
df["harga_satuan"] = pd.to_numeric(df["harga_satuan"], errors="coerce")

# 2. Hapus baris jika harga_satuan atau nama_kasir bernilai NaN
df = df.dropna(subset=["harga_satuan", "nama_kasir"])

# 3. Hapus duplikat
df = df.drop_duplicates().reset_index(drop=True)

# 4. Hitung kolom turunan (sudah bebas dari NaN)
df["total_pendapat"] = df["harga_satuan"] * df["jumlah_terjual"]
print("Total Pendapatan:")
print(df["total_pendapat"])

# 5. Mencari Menu Mahal (> 10000)
mahal = df[df["harga_satuan"] > 10000]
print("\nMenu Mahal:")
print(mahal)

# 6. Membuat Ringkasan (Groupby)
ringkasan = df.groupby("nama_produk")["total_pendapat"].sum()
print("\nRingkasan Pendapatan per Produk:")
print(ringkasan)

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