import streamlit as st
import google.generativeai as genai

# --- 1. YAPAY ZEKA AYARI ---
genai.configure(api_key="AIzaSyBzDTPzJmUovHk-DBxenQfDJ4i5nHlRUgM")
model = genai.GenerativeModel('models/gemini-1.5-flash-')

# --- 2. GÖRSEL TASARIM ---
st.set_page_config(page_title="MirrorAI | Güvenli Sağlık Analizi", layout="wide")

st.markdown("""
<style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { background: linear-gradient(45deg, #ff4b4b, #b22222); color: white; border-radius: 15px; width: 100%; height: 50px; font-weight: bold; border: none; }
</style>
""", unsafe_allow_html=True)

st.title("🪞 MirrorAI: Akıllı Biyometrik Tarama")

# Test için basit bir buton
if st.button("ANALİZİ BAŞLAT"):
    try:
        response = model.generate_content("Merhaba, analiz yapmaya hazır mısın?")
        st.write(response.text)
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
