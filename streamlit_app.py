import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="💰 Pengeplanen 2.0", layout="wide")

st.title("💰 Pengeplanen 2.0")
st.write("Dette er din oppdaterte versjon av pengeplanen basert på **basisplan 400M – 8 %/2 %**.")

# Grunnverdier
startformue = 400_000_000
avkastning = 0.08
uttak = 0.02
kapitalskatt = 0.22
formuesskatt = 0.0085
eiendomskostnader = 1_000_000
år = 30

# Beregning
data = []
formue = startformue
for i in range(1, år + 1):
    bruttoavkastning = formue * avkastning
    skatt = bruttoavkastning * kapitalskatt + formue * formuesskatt
    uttak_år = formue * uttak
    netto_endring = bruttoavkastning - skatt - uttak_år - eiendomskostnader
    formue += netto_endring
    data.append({
        "År": i,
        "Startformue": round(formue / ((1 + (netto_endring / formue))), 0),
        "Avkastning": round(bruttoavkastning, 0),
        "Skatt": round(skatt, 0),
        "Uttak": round(uttak_år, 0),
        "Eiendomskostnader": eiendomskostnader,
        "Netto endring": round(netto_endring, 0),
        "Sluttformue": round(formue, 0)
    })

df = pd.DataFrame(data)

# Vis tabell
st.subheader("📊 Årlig oversikt")
st.dataframe(df, use_container_width=True)

# Vis graf
st.subheader("📈 Formuesutvikling")
plt.figure(figsize=(10, 5))
plt.plot(df["År"], df["Sluttformue"], linewidth=2)
plt.xlabel("År")
plt.ylabel("Formue (NOK)")
plt.title("Utvikling i netto formue over tid")
st.pyplot(plt)

st.success("✅ Pengeplanen 2.0 er klar – full beregning med skatt, uttak og vekst.")
