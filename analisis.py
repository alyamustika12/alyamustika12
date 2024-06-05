import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
df = pd.read_csv('data_produksi.csv')

# Konversi kolom 'Tanggal Produksi' menjadi tipe data datetime
df['Tanggal Produksi'] = pd.to_datetime(df['Tanggal Produksi'])

# Menampilkan data frame
print("Data Produksi:")
print(df)

# Analisis sederhana: Total produksi per produk
total_produksi_per_produk = df.groupby('Nama Produk')['Jumlah Produksi'].sum()
print("\nTotal Produksi per Produk:")
print(total_produksi_per_produk)

# Visualisasi sederhana: Grafik jumlah produksi per tanggal
plt.figure(figsize=(10, 6))
for produk in df['Nama Produk'].unique():
    plt.plot(df[df['Nama Produk'] == produk]['Tanggal Produksi'], df[df['Nama Produk'] == produk]['Jumlah Produksi'], label=produk)

plt.title('Jumlah Produksi per Tanggal')
plt.xlabel('Tanggal Produksi')
plt.ylabel('Jumlah Produksi')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
