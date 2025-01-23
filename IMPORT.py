import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Aplikasi Streamlit Sederhana")

# Deskripsi
st.write("Ini adalah aplikasi pertama saya menggunakan Streamlit!")

# Input data dari pengguna
st.header("Input Data")
name = st.text_input("Masukkan nama kamu:")
age = st.number_input("Masukkan usia kamu:", min_value=1, max_value=100, value=20)
mood = st.selectbox("Bagaimana perasaanmu hari ini?", ["Bahagia", "Biasa saja", "Sedih"])

# Menampilkan data yang dimasukkan
st.write("Nama kamu:", name)
st.write("Usia kamu:", age)
st.write("Kamu merasa:", mood)

# Tabel data acak
st.header("Tabel Data Acak")
data = pd.DataFrame(np.random.randn(10, 3), columns=["Kolom A", "Kolom B", "Kolom C"])
st.dataframe(data)

# Grafik
st.header("Grafik")
st.line_chart(data)

# Penutup
st.write("Terima kasih telah mencoba aplikasi ini!")
