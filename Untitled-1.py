# %%
import pandas as pd
import numpy as np
import streamlit as st

# %%
st.set_page_config(layout="wide")


uploaded_file_one = "main.csv"
uploaded_file_who = "asd.csv"
uploaded_file_third = "df_count_zero.csv"
uploaded_file_five = "df5_prov.csv"



all = pd.read_csv(uploaded_file_one, sep=',')
task = pd.read_csv(uploaded_file_who, sep=',')
zero_count = pd.read_csv(uploaded_file_third, sep=',')
need_task = pd.read_csv(uploaded_file_five, sep=',')


all = all[['state','category_id' , 'offers_may', 'offers_no_responds_may', 
'count_active_may', 'count_active_may_with_responds', 'need', 'need_']]

all.columns = ['Штат', 'id категории', 'Количество задач', 
                'Количество задач без отклика', 'Количество активных провайдеров',
                'Количество активных провайдеров с откликом', 'Необходимое число провайдеров', 'Необходимое число провайдеров для поиска']


task = task[['state', 'need', 'need_']]
task.columns = ['Штат', 'Необходимое число провайдеров', 'Необходимое число провайдеров для поиска']


zero_count = zero_count[['state', 'category_id']]

zero_count.columns = ['Штат', 'id_категории']



st.title("Аналитика задач за май 2022")
st.subheader("Количество необходимых провайдеров")

####################

col_multi, col_em = st.columns([2, 3])
selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=all['Штат'].unique().tolist(),
    index=0,
)

st.write(all.query('Штат == @selected_sn'), width=300)


st.write("""##### Суммарное необходимое количество провайдеров по штатам""")
st.write(task, width=200)

####################

st.subheader("Штаты с 0 задач и провайдеров")

col_multi, col_em = st.columns([2, 3])
selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=zero_count['Штат'].unique().tolist(),
    index=0,
)

col_em.write("")
col_em.write("")
col_em.write(
    f"{selected_sn} содержит {zero_count.query('Штат == @selected_sn').count()[0]} категорий без провайдеров и исполнителей"
)
st.write(zero_count.query('Штат == @selected_sn'), width=300)

####################



st.header("Штаты с маленьким количеством задач")

col_multi, col_em = st.columns([2, 3])
selected_sn = col_multi.selectbox(
    "Выберите штат",
    options=need_task['Штат'].unique().tolist(),
    index=0,
)

col_em.write("")
col_em.write("")
col_em.write(
    f"В штат {selected_sn} необходимо привлечь {zero_count.query('Штат == @selected_sn').sum()[7]} закзачиков"
)
st.write(need_task.query('Штат == @selected_sn'), width=300)

# %%



