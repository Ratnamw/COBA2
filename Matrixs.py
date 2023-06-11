import streamlit as st
import numpy as np

st.header("Kalkulator Matriks")

# Input ukuran matriks
rows1 = st.number_input("Masukkan jumlah baris matriks pertama:")
cols1 = st.number_input("Masukkan jumlah kolom matriks pertama:")
rows2 = st.number_input("Masukkan jumlah baris matriks kedua:")
cols2 = st.number_input("Masukkan jumlah kolom matriks kedua:")

# Input elemen-elemen matriks pertama
st.subheader("Masukkan elemen-elemen matriks pertama:")
matrix1 = []
for i in range(int(rows1)):
    row = []
    for j in range(int(cols1)):
        value = st.number_input(f"Elemen ({i+1}, {j+1}):")
        row.append(value)
    matrix1.append(row)

# Input elemen-elemen matriks kedua
st.subheader("Masukkan elemen-elemen matriks kedua:")
matrix2 = []
for i in range(int(rows2)):
    row = []
    for j in range(int(cols2)):
        value = st.number_input(f"Elemen ({i+1}, {j+1}):")
        row.append(value)
    matrix2.append(row)

# Tombol untuk melakukan perhitungan
calculate = st.button("Hitung")

# Logika perhitungan berdasarkan tombol "Hitung"
if calculate:
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    
    # Penjumlahan matriks
    if rows1 == rows2 and cols1 == cols2:
        addition_result = matrix1 + matrix2
        st.subheader("Hasil Penjumlahan Matriks:")
        st.write(addition_result)
    
    # Pengurangan matriks
    if rows1 == rows2 and cols1 == cols2:
        subtraction_result = matrix1 - matrix2
        st.subheader("Hasil Pengurangan Matriks:")
        st.write(subtraction_result)
    
    # Perkalian matriks
    if cols1 == rows2:
        multiplication_result = np.dot(matrix1, matrix2)
        st.subheader("Hasil Perkalian Matriks:")
        st.write(multiplication_result)