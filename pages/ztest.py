import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest
from scipy.stats import shapiro

st.title('ZTest')

with st.expander('view data'):
    df = pd.read_csv('https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv')
    st.dataframe(df.transpose())

with st.expander('Input data'):
    data = st.text_input("Enter data (comma-separated)")

    input_button = st.button("Submit")

if input_button:
    # Convert the user input into a DataFrame
    data_list = data.split(',')
    df = pd.DataFrame(data_list)

    # Transpose the DataFrame
    df_transposed = df.transpose()

    # Display the transposed DataFrame
    st.dataframe(df_transposed)

with st.expander('view statistics'):
    st.dataframe(df.describe().transpose())

st.write('## Constructing')
import streamlit as st

st.latex('H_{0} : \mu = \mu_{0}')
st.latex('H_{1} : \mu \\neq \mu_{1}') #\neq stands for not eq

alpha = st.number_input('Masukkan Nilai α', step = 0.001, min_value = 0., max_value = 1.0)
null_mean = st.number_input('Masukkan Nilai $\\mu_{0}$', step = 0.001)

clicked = st.button('Do The Z Test !!')

if clicked:
    print(alpha)
    alpha_z = NormalDist().inv_cdf(p=1-alpha/2)
    z_score, p_value = ztest(df['grades'], value=null_mean, alternative='two-sided')
    if abs(z_score) > alpha_z :
        st.latex('REJECT H_{0}')
    else:
        st.latex('CAN NOT REJECT H_{0}')
    st.write('TITIK KRITIS = {alpha_z}, hitung z = {z_score}, p_value = {p_value}')

st.write('CHECK NORMALITY')
clikced_2 = st.button('Do The Shapiro Test !!')

if clikced_2:
    result = shapiro(df['grades'])
    st.write(result)
    st.bar_chart(df['grades'])