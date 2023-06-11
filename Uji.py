import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Judul halaman web
st.title("Penjelasan Uji ANOVA dengan Streamlit")

# Data contoh
data = pd.DataFrame({
    'Group': ['A'] * 10 + ['B'] * 10 + ['C'] * 10,
    'Score': np.random.randint(50, 100, 30)
})

# Tampilkan data contoh
st.subheader("Data Contoh")
st.dataframe(data)

# Memilih variabel dependen
dependent_var = st.selectbox("Pilih variabel dependen", data.columns)

# Memilih variabel independen
independent_var = st.multiselect("Pilih variabel independen", data.columns)

# Menjalankan analisis ANOVA
formula = f"{dependent_var} ~ {' + '.join(independent_var)}"
model = ols(formula, data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Menampilkan hasil ANOVA
st.subheader("Hasil Uji ANOVA")
st.dataframe(anova_table)
