import streamlit as st
import google.generativeai as genai
import random

# --- 1. HATA AYIKLAMA MODU ---
st.set_page_config(page_title="MirrorAI | Hata Ayıklama", layout="wide")

# API Anahtarı Tanımlama
API_KEY = "AIzaSyDaLtQymBdqwTvoguXrRyd-F174kFhsn7s"

def test_connection():
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('models/gemini-pro')
        # Bu satır gerçek testi yapar
        response = model.generate_content("Merhaba")
        return model, "✅ Bağlantı Başarılı!"
    except Exception as e:
        return None, f"❌ Hata Detayı: {str(e)}"

model, status_msg = test_connection()

# --- 2. TASARIM VE PANEL ---
st.title("🪞 MirrorAI | Sistem Durumu")
st.write(f"### {status_msg}")

if model is None:
    st.error("⚠️ Yapay zeka motoru kapalı. Lütfen aşağıdaki hata detayını oku.")
    st.info("Eğer 'API_KEY_INVALID' yazıyorsa, Google AI Studio'dan yeni bir anahtar almalıyız.")
    st.info("Eğer '429' yazıyorsa, kota dolmuş demektir.")

# --- 3. ANA UYGULAMA PANELİ ---
col1, col2 = st.columns(2)
with col1:
    isim = st.text_input("İsim")
    kamera = st.camera_input("Biyometrik Tarama")
    
    if st.button("ANALİZ ET"):
        if model and isim and kamera:
            with st.spinner("Analiz ediliyor..."):
                try:
                    res = model.generate_content(f"{isim} için sağlık önerisi ver.")
                    st.session_state['sonuc'] = res.text
                except Exception as e:
                    st.error(f"İçerik üretim hatası: {e}")
        else:
            st.warning("Bilgileri eksiksiz girin.")

with col2:
    if 'sonuc' in st.session_state:
        st.success("🤖 Rapor Hazır:")
        st.write(st.session_state['sonuc'])
