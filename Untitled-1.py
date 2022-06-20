# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.title("Необходимое число провайдеров")

uploaded_file_one = "main.csv"
uploaded_file_who = "asd.csv"


all = pd.read_csv(uploaded_file_one, sep=',')
task = pd.read_csv(uploaded_file_who, sep=',')


st.write(all.head(5))
st.write(task.head(5))

col_multi, col_em = st.columns([2, 3])

selected_sn = col_multi.selectbox(
    "Выберите промокод",
    options=all['state'].unique().tolist(),
    index=0,
)

st.write(all.query('state == @options'))




# %%



