import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set judul halaman
st.title("Analysis of Variance (ANOVA)")

# Tambahkan deskripsi atau penjelasan singkat
st.write("Selamat datang di aplikasi Analisis Variansi (ANOVA)!")
st.write("ANOVA adalah metode statistik yang digunakan untuk membandingkan rata-rata dari tiga atau lebih kelompok yang berbeda untuk melihat apakah ada perbedaan yang signifikan di antara mereka.")
st.write("Dengan menggunakan ANOVA, kita dapat menentukan apakah ada perbedaan yang signifikan antara kelompok-kelompok tersebut berdasarkan variabel dependen yang diamati.")
st.write("ANOVA merupakan salah satu teknik penting dalam statistika dan digunakan dalam berbagai bidang, seperti ilmu sosial, ilmu biologi, ilmu ekonomi, dan ilmu kesehatan. Dengan menggunakan ANOVA, kita dapat mendapatkan pemahaman yang lebih baik tentang perbedaan kelompok dan faktor-faktor yang mempengaruhinya.")
st.write("Aplikasi ini memberikan kemudahan untuk melakukan analisis ANOVA secara interaktif. Anda dapat memasukkan data Anda, memilih jenis ANOVA yang sesuai, dan melihat hasil analisis dengan mudah melalui antarmuka aplikasi.")
st.write("Aplikasi ini memiliki dua halaman utama:")
st.subheader("1. One-Way ANOVA")
st.write("One-Way ANOVA digunakan ketika kita ingin membandingkan rata-rata dari tiga atau lebih kelompok yang dihasilkan dari satu faktor atau variabel independen.")
st.write("Pada halaman ini, Anda dapat memasukkan data kelompok, memilih metode pengujian hipotesis, dan melihat hasil analisis yang mencakup rata-rata kelompok, variabilitas dalam kelompok, dan keberartian perbedaan antara kelompok.")
st.subheader("2. Two-Way ANOVA")
st.write("Two-Way ANOVA digunakan ketika kita ingin membandingkan rata-rata dari tiga atau lebih kelompok yang dihasilkan dari dua faktor atau variabel independen.")
st.write("Pada halaman ini, Anda dapat memasukkan data kelompok dan faktor, memilih metode pengujian hipotesis, dan melihat hasil analisis yang mencakup efek masing-masing faktor, interaksi antara faktor-faktor, serta perbedaan kelompok.")
st.write("mohon maaf jika masih ada kekurangan, karena masih dalam proses belajar:))") 
st.write("Terima kasih dan semoga aplikasi ini bermanfaat!")

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

# Halaman Korelasi
def One_Way_ANOVA():
# Judul aplikasi
    st.title('Uji ANOVA')

# Deskripsi aplikasi
    st.markdown('Aplikasi ini melakukan uji ANOVA untuk membandingkan rata-rata antara beberapa kelompok.')

# Memasukkan jumlah kelompok
    num_groups = st.number_input('Jumlah Kelompok', min_value=2, step=1, value=2)

# Menginisialisasi data
    data = []
    for i in range(num_groups):
        data_input = st.text_area(f'Masukkan data kelompok {i+1} (pisahkan dengan koma)', '')
        data_values = [x.strip() for x in data_input.split(',')]
        data.append(data_values)

# Memasukkan taraf signifikansi (alpha)
    alpha = st.number_input('Taraf Signifikansi (alpha)', min_value=0.01, max_value=0.5, step=0.01, value=0.05)

# Tombol untuk memproses data
    if st.button('Proses'):
    # Memeriksa apakah ada data yang dimasukkan
        if all(data):
        # Menginisialisasi DataFrame
            df = pd.DataFrame()

        # Memeriksa validitas data
            valid_data = True
            for i, group_data in enumerate(data):
                group_values = []
                for value in group_data:
                    try:
                        if '.' in value:
                            group_values.append(float(value))
                        else:
                            group_values.append(int(value))
                    except ValueError:
                        valid_data = False
                        st.write(f'Data kelompok {i+1} tidak valid. Pastikan hanya memasukkan angka.')

                df[f'Kelompok {i+1}'] = group_values

            if valid_data:
            # Menampilkan data
                st.subheader('Data')
                st.write(df)

            # Melakukan uji ANOVA jika setidaknya ada 2 kelompok dengan data yang valid
                if len(df.columns) >= 2:
                    result = stats.f_oneway(*[group for _, group in df.iteritems()])
                    st.subheader('Hasil Uji ANOVA')
                    st.write('Nilai p-value:', result.pvalue)

                # Menghitung titik kritis berdasarkan nilai alpha
                    df_between = len(df.columns) - 1
                    df_within = df.size - len(df.columns)
                    critical_value = stats.f.ppf(1 - alpha, df_between, df_within)
                    st.write('Titik Kritis:', critical_value)

                    if result.pvalue < alpha:
                        st.write('Kesimpulan: Terdapat perbedaan signifikan antara kelompok-kelompok')
                    else:
                        st.write('Kesimpulan: Tidak terdapat perbedaan signifikan antara kelompok-kelompok')

                # Menghitung jumlah kuadrat
                    sum_sq_between = sum((df[group].mean() - df.values.mean()) ** 2 for group in df.columns) * len(df)
                    sum_sq_within = sum((df[group] - df[group].mean()).pow(2).sum() for group in df.columns)
                    sum_sq_total = sum_sq_between + sum_sq_within


                # Menghitung derajat kebebasan
                    df_total = df.size - 1

                # Menghitung rata-rata kuadrat
                    mean_sq_between = sum_sq_between / df_between
                    mean_sq_within = sum_sq_within / df_within

                # Menghitung statistik F
                    f_value = mean_sq_between / mean_sq_within

                # Membuat tabel ANOVA
                    anova_table = pd.DataFrame({
                        'Sumber Variasi': ['Antar Kelompok', 'Dalam Kelompok', 'Total'],
                        'Derajat Kebebasan': [df_between, df_within, df_total],
                        'Jumlah Kuadrat': [sum_sq_between, sum_sq_within, sum_sq_total],
                        'Rata-rata Kuadrat': [mean_sq_between, mean_sq_within, None],
                        'F-Value': [f_value, None, None]
                    })
                    st.subheader('Tabel ANOVA')
                    st.write(anova_table)

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
    menu = st.sidebar.radio("Navigasi", ("Home", "One-Way ANOVA", "Regresi"))
    
    if menu == "Home":
        home()
    elif menu == "One-Way ANOVA":
        One_Way_ANOVA()
    elif menu == "Regresi":
        regresi()

if __name__ == "__main__":
    main()