import pandas as pd

print("Data inspection")
# Data inspection
df = pd.read_csv("data_kantin.csv")
print(df.head())
print(df.info())
print(df.describe())

print("Missing value")
# Menangani mssing value
print(df.isnull().sum())
df['terjual'] = df['terjual'].fillna(0)
df = df.dropna(subset=['menu'])
# Checking if thre still any null value
print(df.isnull().sum())

print("Duplicate Data")
# Menangani duplikat data
print(df.duplicated().sum())
# Cek duplikat hanya berdasarkan kolom 'id_transaksi'
duplikat_id = df[df.duplicated(subset=['tanggal'], keep=False)].sort_values(by='tanggal')
print(duplikat_id)
df = df.drop_duplicates()
# Checking if thre still any duplicates
print(df.duplicated().sum())
print(df.shape)

# Data manipulation 
laris = df[df["terjual"] > 20]
print("Laris")
print(laris)

# Mengurutkan files
urut = df.sort_values(by='terjual', ascending=False)
print("Urut")
print(urut)

# mengurutkan total pendapat
df['total_pendapat'] = df['harga'] * df['terjual']
print('Total pendaptan')
print(df['total_pendapat'])

# membuat ringkasan
ringkasan = df.groupby('menu')['total_pendapat'].sum()
print('Ringkasan')
print(ringkasan)


# Latihan 3
# # Kolom yang non-null lebih sedikit adalah terjual dan itu menandakan bahwa banyak data kosong atau null

# Latihan 4
# terjual di-fillna karena nilainya masih bisa diestimasi secara logis (0) tanpa merusak data lainnya.
# menu di-dropna karena identitas utamanya hilang, sehingga seluruh baris data tidak lagi relevan untuk dianalisis.

# Latihan 5
# Sebelumnya ada 107 baris dan sekarang ada 102 Baris
# kita perlu menghapus duplicate untuk menghapus hasil perhitungan ganda

# Latihan 6
# dari data yang dilihat menu yang paling banyak menghasilkan uang adalah Nasi goreng, dan kita perlu data ini
# misalnya untuk contoh manajmen stok bahan baku karena nasi goreng paling menghasilkan uang jadi kita perlu memprioritaskan