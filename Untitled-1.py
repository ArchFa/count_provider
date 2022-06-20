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

col_multi, col_em = st.columns([1, 3])

selected_sn = col_multi.selectbox(
    "Выберите промокод",
    options=all['state'].unique().tolist(),
    index=0,
)



df_ref_code = all[all['state']== selected_sn].duration.value_counts().to_frame()
st.dataframe(df_ref_code)


