import streamlit as st
from google import genai
import random

# --- 1. SAYFA VE SİSTEM AYARLARI ---
st.set_page_config(page_title="MirrorAI | Profesyonel Sağlık Koçu", layout="wide")

# Yeni Nesil SDK Yapılandırması (2026)
API_KEY = "AIzaSyA1jrF344zDTDLdcF3TkqMNarYwtXQIXIE"
client = genai.Client(api_key=API_KEY)

# --- 2. PREMIUM NEON ARAYÜZ TASARIMI ---
st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2 { color: #00f2fe; text-align: center; text-shadow: 0 0 15px #00f2fe; }
    
    /* Neon Buton */
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; width: 100%; height: 60px;
        font-weight: bold; border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 35px #00f2fe; }
    
    /* Rapor Kartı */
    .report-card {
        background: rgba(16, 21, 31, 0.95); padding: 30px; border-radius: 25px;
        border: 2px solid #00f2fe; box-shadow: 0 0 25px rgba(0, 242, 254, 0.2);
        color: #ffffff; line-height: 1.8; font-size: 16px;
    }
    .metric-box {
        background: #10151f; padding: 15px; border-radius: 15px;
        border-left: 5px solid #00f2fe; margin-bottom: 15px;
        font-weight: bold; color: #00f2fe;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL VE GİRİŞLER ---
st.title("🪞 MirrorAI: Dijital Sağlık ve Postür Aynası")
st.write("---")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("🌐 Biyometrik Veri Girişi")
    isim = st.text_input("Adınız Soyadınız", placeholder="Örn: Ezgi Büyükkaya")
    yas = st.slider("Yaşınız", 15, 85, 22)
    
    # Senin istediğin o alternatif başlıklar
    odak_noktasi = st.selectbox(
        "Analiz Odak Noktası", 
        ["Karın Bölgesi & Yağ Yakımı", "Cilt Sağlığı & Parlaklık", "Postür Düzeltme & Esneklik", "Kas Kütlesi & Şekillenme"]
    )
    
    kamera = st.camera_input("Biyometrik Tarama (Yüz ve Gövde)")

    if st.button("🚀 ANALİZİ VE ADIM ADIM KOÇLUĞU BAŞLAT"):
        if isim and kamera:
            with st.spinner("Gemini 3 Flash verileri işliyor..."):
                try:
                    # Rastgele simüle edilen veriler
                    f_yag = random.randint(18, 27)
                    f_su = random.randint(58, 66)
                    
                    # YAPAY ZEKAYA VERİLEN AYRINTILI TALİMAT (PROMPT)
                    istek = f"""
                    Sen profesyonel bir fitness koçu ve beslenme uzmanısın. 
                    Kullanıcı: {isim}, Yaş: {yas}, Odak Noktası: {odak_noktasi}.
                    Tahmini Yağ Oranı: %{f_yag}.
                    
                    Lütfen şu başlıklarda ADIM ADIM ve ÇÖZÜM odaklı bir rapor hazırla:
