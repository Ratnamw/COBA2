import streamlit as st

st.header("Kalkulator Sederhana")

# Input bilangan pertama
num1 = st.number_input("Masukkan bilangan pertama:")

# Input operasi matematika
operation = st.selectbox("Pilih operasi:", ["+", "-", "*", "/"])

# Input bilangan kedua
num2 = st.number_input("Masukkan bilangan kedua:")

# Tombol untuk melakukan perhitungan
calculate = st.button("Hitung")

# Logika perhitungan berdasarkan operasi yang dipilih
if calculate:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    
    # Menampilkan hasil perhitungan
    st.success(f"Hasil: {result}")
