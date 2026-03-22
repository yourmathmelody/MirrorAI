import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. SİSTEM AYARLARI VE BAĞLANTI ---
st.set_page_config(page_title="MirrorAI | Sağlık Koçu", layout="wide")

# Senin yeni anahtarını buraya zırhlı bir şekilde ekledim
API_KEY = "AIzaSyA1jrF344zDTDLdcF3TkqMNarYwtXQIXIE"

try:
    genai.configure(api_key=API_KEY)
    # Hata veren kısmı 'models/' ekleyerek tamir ettim:
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    # Bağlantı testi
    model.generate_content("test")
except Exception as e:
    st.error(f"Bağlantı Kurulamadı: {e}")
    model = None

# --- 2. TASARIM (MAVİ-YEŞİL NEON) ---
st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; text-align: center; }
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 25px; width: 100%; height: 55px;
        font-weight: bold; border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
    }
    .report-box {
        background: rgba(16, 21, 31, 0.9); padding: 20px; border-radius: 15px;
        border: 1px solid #00f2fe; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. UYGULAMA PANELİ ---
st.title("🪞 MirrorAI: Dijital Sağlık Aynası")

col1, col2 = st.columns([1, 1])

with col1:
    isim = st.text_input("İsim Soyisim")
    kamera = st.camera_input("Biyometrik Tarama")

    if st.button("ANALİZİ BAŞLAT"):
        if model and isim and kamera:
            with st.spinner("Yapay zeka verileri işliyor..."):
                try:
                    # Raporu hazırlayan kısım
                    prompt = f"Sen profesyonel bir sağlık koçusun. Kullanıcı ismi: {isim}. Bu kişi için 3 tane çok kısa vitamin ve yaşam önerisi ver."
                    response = model.generate_content(prompt)
                    st.session_state['sonuc'] = response.text
                except Exception as e:
                    st.error(f"Rapor hazırlanırken hata oluştu: {e}")
        else:
            st.warning("Lütfen isim girin ve kamerayı kullanın.")

with col2:
    st.subheader("🤖 Analiz Raporu")
    if 'sonuc' in st.session_state:
        st.markdown(f'<div class="report-box">{st.session_state["sonuc"]}</div>', unsafe_allow_html=True)
    else:
        st.info("Sonuçlar burada belirecek.")
