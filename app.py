import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set judul halaman
st.title("Aplikasi Web Statistik")

# Tambahkan deskripsi atau penjelasan singkat
st.write("Ini adalah aplikasi web sederhana untuk menampilkan statistik dasar.")

# Muat data dari file CSV
data = pd.read_csv("data.csv")

# Tampilkan tabel data
st.subheader("Tabel Data")
st.dataframe(data)

# Tampilkan deskripsi statistik
st.subheader("Deskripsi Statistik")
st.write(data.describe())

# Tampilkan histogram
st.subheader("Histogram")
selected_column = st.selectbox("Pilih kolom:", data.columns)
plt.hist(data[selected_column].dropna())
st.pyplot(plt)

# Tampilkan scatter plot
st.subheader("Scatter Plot")
x_column = st.selectbox("Pilih kolom x:", data.columns)
y_column = st.selectbox("Pilih kolom y:", data.columns)
plt.scatter(data[x_column], data[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
st.pyplot(plt)


st.title('Thank uuu :v')

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Menghitung nilai korelasi
def calculate_correlation(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sqrt(np.sum((X - mean_X)**2) * np.sum((Y - mean_Y)**2))
    correlation = numerator / denominator
    return correlation

# Menghitung koefisien regresi beta 0 dan beta 1
def calculate_regression_coefficients(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X)**2)
    beta_1 = numerator / denominator
    beta_0 = mean_Y - beta_1 * mean_X
    return beta_0, beta_1

# Menghitung R-Squared
def calculate_r_squared(X, Y, beta_0, beta_1):
    mean_Y = np.mean(Y)
    predicted_Y = beta_0 + beta_1 * X
    numerator = np.sum((Y - predicted_Y)**2)
    denominator = np.sum((Y - mean_Y)**2)
    r_squared = 1 - (numerator / denominator)
    return r_squared

# Halaman Home
def home():
    st.title("Regresi Linier Sederhana")
    st.write("Selamat datang di aplikasi Regresi Linier Sederhana!")
    st.write("Regresi linier sederhana adalah metode statistik yang digunakan untuk memodelkan hubungan antara sebuah variabel dependen (Y) dengan sebuah variabel independen (X).")
    st.write("Dengan menggunakan regresi linier sederhana, kita dapat memprediksi nilai variabel dependen berdasarkan nilai variabel independen.")
    st.write("Aplikasi ini memiliki dua halaman utama: Korelasi dan Regresi. Silakan pilih halaman yang ingin diakses pada sidebar di sebelah kiri. ")
    st.write("Saya menyadari bahwa web ini masih belum sempurna dan banyak kurangnya, oleh karena itu mohon maaf dan kasih nilai excelent yaa hehehe. Thank you~~ ")

# Halaman Korelasi
def korelasi():
    st.title("Menghitung Nilai Korelasi")
    st.write("Halaman ini digunakan untuk melakukan analisis korelasi antara dua variabel.")
    
    option = st.radio("Pilih Opsi", ("Data Manual", "Upload File"))
    
    if option == "Data Manual":
        num_data = st.number_input("Jumlah Data", min_value=2, value=10, step=1)
        data = []
        for i in range(num_data):
            x = st.number_input(f"Nilai X{i+1}", key=f"X{i+1}")
            y = st.number_input(f"Nilai Y{i+1}", key=f"Y{i+1}")
            data.append((x, y))
        
        if st.button("Hitung Korelasi"):
            X = np.array([d[0] for d in data])
            Y = np.array([d[1] for d in data])
            
            correlation = calculate_correlation(X, Y)
            st.write(f"Nilai Korelasi: {correlation:.4f}")
            
            # Plot grafik korelasi
            plt.scatter(X, Y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Grafik Korelasi")
            st.pyplot(plt)
            
            # Analisis hasil korelasi
            if correlation > 0:
                st.write("Terdapat hubungan positif antara X dan Y.")
            elif correlation < 0:
                st.write("Terdapat hubungan negatif antara X dan Y.")
            else:
                st.write("Tidak terdapat hubungan linier antara X dan Y.")
    
    else:
        uploaded_file = st.file_uploader("Upload File", type=["csv", "xlsx"])

# Halaman Regresi
def regresi():
    st.title("Analisis Regresi")
    st.write("Halaman ini digunakan untuk melakukan analisis regresi linier sederhana.")
    
    option = st.radio("Pilih Opsi", ("Data Manual", "Upload File"))
    
    if option == "Data Manual":
        num_data = st.number_input("Jumlah Data", min_value=2, value=10, step=1)
        data = []
        for i in range(num_data):
            x = st.number_input(f"Nilai X{i+1}", key=f"X{i+1}")
            y = st.number_input(f"Nilai Y{i+1}", key=f"Y{i+1}")
            data.append((x, y))
        
        if st.button("Hitung Regresi"):
            X = np.array([d[0] for d in data])
            Y = np.array([d[1] for d in data])
            
            beta_0, beta_1 = calculate_regression_coefficients(X, Y)
            r_squared = calculate_r_squared(X, Y, beta_0, beta_1)
            
            st.write(f"Nilai Beta 0: {beta_0:.4f}")
            st.write(f"Nilai Beta 1: {beta_1:.4f}")
            st.write(f"Nilai R-Squared: {r_squared:.4f}")
            st.write(f"Y = {beta_0:.4f} + {beta_1:.4f}X")
            
            # Model regresi
            plt.scatter(X, Y)
            plt.plot(X, beta_0 + beta_1 * X, color='red')
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Model Regresi")
            st.pyplot(plt)
            
    else:
        uploaded_file = st.file_uploader("Upload File", type=["csv", "xlsx"])

# Main Program
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Navigasi", ("Home", "Korelasi", "Regresi"))
    
    if menu == "Home":
        home()
    elif menu == "Korelasi":
        korelasi()
    elif menu == "Regresi":
        regresi()

if __name__ == "__main__":
    main()