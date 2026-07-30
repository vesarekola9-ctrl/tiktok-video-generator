import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TikTok Hassu Video Generaattori", page_icon="??", layout="centered")

st.title("?? TikTok Hassu Video Generaattori")
st.write("Lataa oma kuvasi, kirjoita millaisen hassun videon haluat, ja luo viraalisisältöä TikTokiin!")

# Tiedoston lataus käyttäjälle
uploaded_file = st.file_uploader("Valitse oma kasvokuvasi", type=["png", "jpg", "jpeg"])

# Tekstikenttä videon idealle
prompt = st.text_input(
    "Millaisen hassun videon haluat?", 
    placeholder="esim. 'tanssii ysäridiskossa neonvaloissa, hauska animaatiotyyli'"
)

if st.button("?? Luo hassu video"):
    if uploaded_file is not None and prompt:
        st.info("?? Tekoäly käsittelee kuvaasi ja luo videota... Odota hetki.")
        
        # Tähän kohtaan lisätään varsinainen videogeneraattorin API-kutsu (esim. Runway, Luma tai vastaava)
        
        st.success("? Video luotu onnistuneesti! Valmis ladattavaksi TikTokiin.")
    else:
        st.warning("?? Ole hyvä ja lataa kuva sekä kirjoita millaisen videon haluat.")
