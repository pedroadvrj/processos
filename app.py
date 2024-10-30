import pandas as pd
import streamlit as st

df = pd.read_csv("cadastroprocessos.csv", header=None, encoding="ISO-8859-1", names=["index_acao", "nomecliente", "outra_parte","numero_processo", "comarca", "vara", "tipo_de_acao"])


def quantidade_processos():
    return len(df["numero_processo"].unique())

def busca_por_nome(nome):
    # Filtra o DataFrame com base no nome informado
    
    processos = df[df["nomecliente"].str.contains(nome, case=False, na=False)]

    if not processos.empty:
        numeros_processos = processos["numero_processo"].tolist()
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

st.divider()













