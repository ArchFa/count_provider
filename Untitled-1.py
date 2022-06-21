# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.set_page_config(layout="wide")


uploaded_file_one = "main.csv"
uploaded_file_who = "asd.csv"
uploaded_file_third = "df_count_zero.csv"

all = pd.read_csv(uploaded_file_one, sep=',')
task = pd.read_csv(uploaded_file_who, sep=',')
zero_count = pd.read_csv(uploaded_file_third, sep=',')

st.title("Аналитика задач за май 2022")
st.subheader("Количество необходимых провайдеров")


col_multi, col_em = st.columns([2, 3])
selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=all['state'].unique().tolist(),
    index=0,
)

st.write(all.query('state == @selected_sn'), width=300)


st.write("""##### Суммарное необходимое количество провайдеров по штатам""")
st.write(task, width=200)



st.subheader("Штаты с 0 задач и провайдеров")
st.write(zero_count)


col_multi, col_em = st.columns([2, 3])
selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=zero_count['state'].unique().tolist(),
    index=0,
)


col_em.write("")
col_em.write("")
col_em.write(
    f"{selected_sn} содержит {df.query('state == @selected_sn').count()[0]} категорий без провайдеров и исполнителей"
)


# %%



