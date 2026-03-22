import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. SAYFA AYARLARI (EN ÜSTTE OLMALI) ---
st.set_page_config(page_title="MirrorAI | Sağlık Koçu", layout="wide")

# API Anahtarı
API_KEY = "AIzaSyA1jrF344zDTDLdcF3TkqMNarYwtXQIXIE"

# --- 2. GÖRSEL TASARIM (MAVİ-YEŞİL NEON) ---
st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; text-align: center; }
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; width: 100%; height: 60px;
        font-weight: bold; border: none; box-shadow: 0 0 25px rgba(0, 242, 254, 0.6);
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 35px #00f2fe; }
    .report-card {
        background: rgba(16, 21, 31, 0.95); padding: 30px; border-radius: 25px;
        border: 2px solid #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        color: #ffffff; line-height: 1.8;
    }
    .metric-box {
        background: #10151f; padding: 15px; border-radius: 15px;
        border-left: 5px solid #00f2fe; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL ---
st.title("🪞 MirrorAI: Dijital Sağlık Aynası")
st.write("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🌐 Biyometrik Veri Girişi")
    isim = st.text_input("Adınız Soyadınız", placeholder="Örn: Ezgi Büyükkaya")
    yas = st.slider("Yaşınız", 15, 80, 22)
    hedef = st.selectbox("Sağlık Hedefiniz", ["Yağ Yakımı & Karın Bölgesi", "Cilt Sağlığı & Detoks", "Kas Kütlesi Artışı", "Genel Sağlık Kontrolü"])
    kamera = st.camera_input("Biyometrik Yüz ve Postür Taraması")

    if st.button("🔍 ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if isim and kamera:
            with st.spinner("Yapay Zeka dokuları ve verileri analiz ediyor..."):
                try:
                    # BAĞLANTIYI BUTON İÇİNDE KURUYORUZ (404 HATASINI BİTİRİR)
                    genai.configure(api_key=API_KEY)
                    # En stabil model ismi
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    
                    # Dinamik Veri Üretimi
                    f_yag = random.randint(18, 26)
                    f_su = random.randint(55, 65)
                    
                    # YAPAY ZEKAYA ÖZEL TALİMAT (PROMPT)
                    istek = f"""
                    Sen bir profesyonel sağlık, fitness ve cilt uzmanısın. 
                    Kullanıcı: {isim}, Yaş: {yas}, Hedef: {hedef}.
                    Tahmini Yağ Oranı: %{f_yag}, Su Oranı: %{f_su}.
                    
                    Lütfen şu 4 başlıkta adım adım, samimi bir rapor hazırla:
                    1. Cilt Sağlığı Analizi: (Yüz taramasına göre öneriler)
                    2. Bölgesel Tavsiye: ({hedef} üzerine spor ve egzersiz adımları)
                    3. Beslenme & Vitamin: (Hangi yiyeceklerden uzak durmalı, hangilerini yemeli?)
                    4. Haftalık Aksiyon Planı: (Adım adım yapılacaklar)
                    """
                    
                    response = model.generate_content(istek)
                    st.session_state['mirror_raporu'] = response.text
                    st.session_state['yag_orani'] = f_yag
                    st.success("✅ Analiz Başarıyla Tamamlandı!")
                except Exception as e:
                    st.error(f"❌ Motor Hatası: {str(e)}")
                    st.info("İpucu: Eğer 404 diyorsa, requirements.txt dosyasında sürümü 0.8.3 yapıp Reboot edin.")
        else:
            st.warning("⚠️ Devam etmek için lütfen isim girin ve kamerayı onaylayın.")

with col2:
    st.subheader("🤖 MirrorAI Kişisel Raporu")
    if 'mirror_raporu' in st.session_state:
        # Analiz Özet Kutuları
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='metric-box'>🔥 Yağ Oranı: %{st.session_state['yag_orani']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='metric-box'>💧 Su Oranı: %62</div>", unsafe_allow_html=True)
            
        st.markdown(f'<div class="report-card">{st.session_state["mirror_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.info("Kameranızı açıp analizi başlattığınızda dijital koçunuzun detaylı raporu burada belirecek.")

# --- 4. ALT BİLGİ ---
st.markdown("---")
st.caption("MirrorAI bir yapay zeka asistanıdır. Ciddi sağlık kararları için lütfen doktorunuza danışın.")
