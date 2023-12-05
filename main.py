import streamlit as st #para fazer todo o servidor e gerar as dashboards
import pandas as pd
import numpy as np
st.header('Dashboards com Streamlit')
st.text('Fazendo varios testes para saber se é bom.')
st.sidebar.header('Configurações')
excel = pd.read_excel('dados.xlsx', sheet_name='Planilha1')
df = pd.DataFrame(
    excel
    )
print(excel)
opselec = st.sidebar.selectbox(
    'Escolha o formato do grafico',
    ('Linhas', 'Barras')
)
if opselec == 'Linhas':
    st.line_chart(df)
else:
    st.bar_chart(df)