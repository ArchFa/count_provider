# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.title("Необходимое число провайдеров")

uploaded_file_one = "main.csv"
uploaded_file_who = "asd.csv"


all = pd.read_csv(uploaded_file_one, sep='|')
task = pd.read_csv(uploaded_file_who, sep='|')

option = st.selectbox(
    "Выберите промокод",
    options=all['state'].unique().tolist(),
    index=0,
)




