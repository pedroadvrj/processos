import pandas as pd
import openpyxl
import streamlit as st

df = pd.read_excel("cadastroprocessos.xlsx")


def quantidade_autor():   #retornar a quantidade de autores de forma unica, para ter a contagem correta
    return len(df["autor"].unique())


def quantidade_processos():
    return len(df["numero_processo"].unique())

def busca_por_nome(nome):
    # Filtra o DataFrame com base no nome informado
    
    processos = df[df["autor"].str.contains(nome, case=False, na=False)]

    if not processos.empty:
        numeros_processos = processos["numero_processo"].tolist()
        numeros_reu = processos["vara"].tolist()
        st.write(f"Processos encontrados de {nome}:")
        for numero in numeros_processos:
            st.write(f"• Processo nº {numero}")
    else:
        st.write("Nenhum processo encontrado para este autor.")



with st.container():
    st.subheader("subheader")
    st.title("Busca processual")
    st.divider()
name_input = st.text_input(" digite o primeiro nome do cliente")

if name_input:
     busca_por_nome(name_input)


st.divider()

st.write(f"Números de processos cadastrados: {quantidade_processos()}")

st.divider()

st.write(f"quantida de clientes: {quantidade_autor()}")












