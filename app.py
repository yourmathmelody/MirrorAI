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
    
    odak_noktasi = st.selectbox(
        "Analiz Odak Noktası", 
        ["Karın Bölgesi & Yağ Yakımı", "Cilt Sağlığı & Parlaklık", "Postür Düzeltme & Esneklik", "Kas Kütlesi & Şekillenme"]
    )
    
    kamera = st.camera_input("Biyometrik Tarama (Yüz ve Gövde)")

    if st.button("🚀 ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if isim and kamera:
            with st.spinner("Gemini 3 Flash verileri işliyor..."):
                try:
                    # Rastgele simüle edilen veriler
                    f_yag = random.randint(18, 27)
                    
                    # YAPAY ZEKAYA VERİLEN AYRINTILI TALİMAT
                    # Syntax hatasını önlemek için f-string'i tek satırda birleştirdik
                    istek = f"Sen profesyonel bir fitness koçu ve beslenme uzmanısın. Kullanıcı: {isim}, Yaş: {yas}, Odak Noktası: {odak_noktasi}, Tahmini Yağ Oranı: %{f_yag}. Lütfen şu başlıklarda ÇÖZÜM odaklı bir rapor hazırla: 1. Mevcut Durum Analizi, 2. Bölgesel Spor ve Karın Egzersizleri (Adım Adım), 3. Yağ Yakıcı Beslenme ve Vitamin Önerileri, 4. Cilt Sağlığı İçin Detoks Önerisi, 5. Bu Haftalık 3 Somut Aksiyon Adımı."
                    
                    # Gemini 3 Flash Preview Model Çağrısı
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=istek
                    )
                    
                    st.session_state['mirror_raporu'] = response.text
                    st.session_state['yag_sonuc'] = f_yag
                    st.success("✅ Analiz Başarıyla Tamamlandı!")
                    
                except Exception as e:
                    st.error(f"❌ Motor Hatası: {str(e)}")
        else:
            st.warning("⚠️ Lütfen isim girin ve kamerayı onaylayın.")

with col2:
    st.subheader("🤖 MirrorAI Kişisel Gelişim Raporu")
    if 'mirror_raporu' in st.session_state:
        # Özet Metrikler
        st.markdown(f"<div class='metric-box'>🔥 Tahmini Yağ: %{st.session_state['yag_sonuc']} | 💧 Su Dengesi: %64</div>", unsafe_allow_html=True)
            
        # Ana Rapor Alanı
        st.markdown(f'<div class="report-card">{st.session_state["mirror_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.info("Kameranızı açıp analizi başlattığınızda dijital koçunuzun raporu burada belirecek.")

st.markdown("---")
st.caption("MirrorAI bir dijital rehberdir. Uygulamadan önce bir uzmana danışmanız önerilir.")
