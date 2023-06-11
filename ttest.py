import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.subheader("Menghitung Waktu Gerak Jatuh Bebas")

h = st.number_input ("Masukkan Nilai Ketinggan Benda dijatuhkan ")
hitung = st.button ("Hitung Estimasi waktu")

if hitung :
    waktu = (h * 2 / 10) ** 0.5
    st.write ("Waktu yang dibutuhkan benda untuk menyentuh permukaan adalah=",waktu)