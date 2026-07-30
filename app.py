import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key and "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]

if api_key:
    genai.configure(api_key=api_key)

st.set_page_config(page_title="TikTok Hassu Video Generaattori", page_icon="🎬", layout="centered")

st.title("🎬 TikTok Hassu Video Generaattori")
st.write("Lataa oma kuvasi, kirjoita millaisen hassun videon haluat, ja luo viraalisisältöä TikTokiin!")

uploaded_file = st.file_uploader("Valitse oma kasvokuvasi", type=["png", "jpg", "jpeg"])

prompt = st.text_input(
    "Millaisen hassun videon haluat?", 
    placeholder="esim. 'tanssii ysäridiskossa neonvaloissa, hauska animaatiotyyli'"
)

if st.button("🚀 Luo hassu video"):
    if not api_key:
        st.error("❌ GEMINI_API_KEY puuttuu! Lisää se Streamlit Secretsiin.")
    elif uploaded_file is not None and prompt:
        with st.spinner("🤖 Tekoäly analysoi kuvaasi ja loihtii viraali-idean TikTokiin..."):
            try:
                image = Image.open(uploaded_file)
                
                # Päivitetty mallinimi
                model = genai.GenerativeModel('gemini-2.0-flash')
                
                full_prompt = (
                    "Olet huippuluokan TikTok-sisällöntuottaja ja viraalivideoiden asiantuntija. "
                    "Analysoi käyttäjän kuva ja idea, ja luo sen pohjalta äärimmäisen hauska ja mukaansatempaava "
                    "TikTok-videon käsikirjoitus, vinkit toteutukseen sekä nokkela kuvateksti hashtagien kera suomeksi.\n\n"
                    f"Ideana on: {prompt}"
                )

                response = model.generate_content([full_prompt, image])
                
                st.success("✨ Hassu TikTok-konsepti luotu onnistuneesti!")
                st.markdown("### 📋 TikTok-käsikirjoitus & Konsepti")
                st.write(response.text)

            except Exception as e:
                st.error(f"Virhe tekoälypyynnössä: {e}")
    else:
        st.warning("⚠️ Ole hyvä ja lataa kuva sekä kirjoita millaisen videon haluat.")
