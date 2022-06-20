# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.set_page_config(layout="wide")

st.title("Необходимое число провайдеров")

uploaded_file_one = "main.csv"
uploaded_file_who = "asd.csv"


all = pd.read_csv(uploaded_file_one, sep=',')
task = pd.read_csv(uploaded_file_who, sep=',')



col_multi, col_em = st.columns([2, 3])

selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=all['state'].unique().tolist(),
    index=0,
)

st.write(all.query('state == @selected_sn'))


st.write("Суммарное еобходимое число провайдеров по штатам")

# %%



