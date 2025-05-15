import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # untuk 3D plot

st.title("Aplikasi Biaya Produksi Linear (Tanpa Koefisien Kuadrat)")

# Input biaya per pcs
a = st.number_input("Biaya per pcs gasket (a)", value=3.0)
b = st.number_input("Biaya per pcs reinf (b)", value=2.0)

# Input jumlah produk x dan y
x_input = st.number_input("Jumlah gasket (x)", value=72000)
y_input = st.number_input("Jumlah reinf (y)", value=2640)

# Hitung total biaya
total_biaya = a * x_input + b * y_input
st.write(f"Total biaya produksi: {total_biaya}")

# Membuat grid untuk plot
x = np.linspace(0, x_input*1.5, 50)
y = np.linspace(0, y_input*1.5, 50)
X, Y = np.meshgrid(x, y)

# Fungsi biaya linear
Z = a * X + b * Y

# Plot grafik 3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_xlabel('Jumlah Gasket (x)')
ax.set_ylabel('Jumlah Reinf (y)')
ax.set_zlabel('Biaya Produksi')
ax.set_title('Permukaan Biaya Produksi Linear')

st.pyplot(fig)
