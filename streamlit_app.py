import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pengeplanen 2.0", layout="wide")

st.title("💰 Pengeplanen 2.0")

st.write("""
Dette er din oppdaterte versjon av pengeplanen.
Her kan du laste inn data, se utvikling og gjøre justeringer.
""")

uploaded_file = st.file_uploader("Last opp Excel- eller CSV-fil med planen din:", type=["xlsx", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.line_chart(df.select_dtypes(include=['float', 'int']))
else:
    st.info("Ingen fil lastet opp ennå.")
