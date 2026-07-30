import streamlit as st
import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Hae API-avain joko ympäristömuuttujasta tai Streamlit secretsistä
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key) if api_key else None

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
        st.error("❌ OpenAI API-avain puuttuu! Lisää se .env-tiedostoon tai Streamlit Secretsiin.")
    elif uploaded_file is not None and prompt:
        with st.spinner("🤖 Tekoäly analysoi kuvaasi ja loihtii viraali-idean TikTokiin..."):
            try:
                image_bytes = uploaded_file.getvalue()
                base64_image = base64.b64encode(image_bytes).decode('utf-8')

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": "Olet huippuluokan TikTok-sisällöntuottaja ja viraalivideoiden asiantuntija. Analysoi käyttäjän kuva ja idea, ja luo sen pohjalta äärimmäisen hauska ja mukaansatempaava TikTok-videon käsikirjoitus, vinkit toteutukseen sekä nokkela kuvateksti hashtagien kera suomeksi."
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": f"Luo tällä idealla hassu TikTok-videokonsepti: {prompt}"
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{base64_image}"
                                    }
                                }
                            ]
                        }
                    ],
                    max_tokens=800,
                    temperature=0.8
                )

                result = response.choices[0].message.content
                st.success("✨ Hassu TikTok-konsepti luotu onnistuneesti!")
                st.markdown("### 📋 TikTok-käsikirjoitus & Konsepti")
                st.write(result)

            except Exception as e:
                st.error(f"Virhe tekoälypyynnössä: {e}")
    else:
        st.warning("⚠️ Ole hyvä ja lataa kuva sekä kirjoita millaisen videon haluat.")
