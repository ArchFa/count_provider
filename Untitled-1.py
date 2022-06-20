# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.title("Необходимое число провайдеров")


all = pd.read_csv('/Users/arturfattahov/Desktop/main.csv', sep='|')
task = pd.read_csv('/Users/arturfattahov/Desktop/asd.csv', sep='|')

option = st.selectbox.selectbox(
    "Выберите промокод",
    options=all['state'].unique().tolist(),
    index=0,
)



