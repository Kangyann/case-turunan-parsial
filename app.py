import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set judul halaman
st.set_page_config(page_title="Simulasi Produksi Gasket & Reinf", layout="centered")
st.title("📦 Simulasi Biaya Produksi Harian (Gasket & Reinf)")
st.title("Kelompok 6" )

# Konstanta produksi
lot_gasket = 3600
lot_reinf = 880
harga_gasket = 50000.0     # harga per pcs (dalam float)
harga_reinf = 200000.0     # harga per pcs (dalam float)
hari_kerja = 22

# Produksi dasar
produksi_gasket_awal = 72000
produksi_reinf_awal = 2640

# Simulasi tambahan harian (acak)
np.random.seed(42)
tambahan_gasket = np.random.randint(0, lot_gasket + 1, hari_kerja)
tambahan_reinf = np.random.randint(0, 808 + 1, hari_kerja)

# Total produksi per hari
produksi_gasket_harian = produksi_gasket_awal + tambahan_gasket
produksi_reinf_harian = produksi_reinf_awal + tambahan_reinf

# Hitung biaya harian (float untuk menghindari overflow)
biaya_gasket = produksi_gasket_harian.astype(float) * harga_gasket
biaya_reinf = produksi_reinf_harian.astype(float) * harga_reinf
total_biaya = biaya_gasket + biaya_reinf

# Biaya dasar
biaya_awal = produksi_gasket_awal * harga_gasket + produksi_reinf_awal * harga_reinf
tambahan_biaya = total_biaya - biaya_awal

# Buat DataFrame hasil simulasi
df = pd.DataFrame({
    "Hari": np.arange(1, hari_kerja + 1),
    "Tambahan Gasket": tambahan_gasket,
    "Tambahan Reinf": tambahan_reinf,
    "Total Gasket": produksi_gasket_harian,
    "Total Reinf": produksi_reinf_harian,
    "Biaya Gasket": biaya_gasket,
    "Biaya Reinf": biaya_reinf,
    "Total Biaya": total_biaya,
    "Tambahan Biaya": tambahan_biaya
})

# Tampilkan DataFrame
st.subheader("📊 Tabel Data Simulasi Produksi")
st.dataframe(df.style.format({
    "Biaya Gasket": "Rp {:,.0f}",
    "Biaya Reinf": "Rp {:,.0f}",
    "Total Biaya": "Rp {:,.0f}",
    "Tambahan Biaya": "Rp {:,.0f}"
}))

# Line chart
st.subheader("📈 Grafik Line Chart: Total Biaya Produksi")
st.line_chart(df.set_index("Hari")[["Total Biaya"]])

# Pyplot chart
st.subheader("📉 Grafik Pyplot: Total Biaya Produksi")
fig, ax = plt.subplots()
ax.plot(df["Hari"], df["Total Biaya"], marker="o", linestyle='-', color='green')
ax.set_title("Total Biaya Produksi Harian")
ax.set_xlabel("Hari ke-")
ax.set_ylabel("Total Biaya (Rp)")
ax.grid(True)
st.pyplot(fig)
