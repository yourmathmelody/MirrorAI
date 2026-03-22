import streamlit as st
import google.generativeai as genai
import time
import random
# --- 1. ÖNCE KÜTÜPHANEYİ VE ANAHTARI KUR ---
import google.generativeai as genai
import streamlit as st

# Anahtarını direkt buraya, en tepeye yazıyoruz
API_KEY = "AIzaSyA1jrF344zDTDLdcF3TkqMNarYwtXQIXIE"

try:
    # ADIM A: Önce kapıyı aç (Konfigüre et)
    genai.configure(api_key=API_KEY)
    
    # ADIM B: Sonra içeri gir (Modeli tanımla)
    # Başına 'models/' ekleyerek en garanti yolu seçiyoruz
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    # ADIM C: Bağlantıyı test et
    model.generate_content("test")
    st.session_state['motor_calisiyor'] = True
except Exception as e:
    st.session_state['motor_calisiyor'] = False
    st.session_state['hata_mesaji'] = str(e)
# --- 1. SİSTEM VE API YAPILANDIRMASI ---
st.set_page_config(page_title="MirrorAI | Dijital Sağlık Koçu", layout="wide")

# Senin en güncel anahtarın (AIzaSyA1jr...)
API_KEY = "AIzaSyA1jrF344zDTDLdcF3TkqMNarYwtXQIXIE"

@st.cache_resource
def load_ai_engine():
    try:
        genai.configure(api_key=API_KEY)
        # 404 hatasını bitiren "Akıllı Model Seçici"
        # Hangi isim varyasyonu çalışırsa onu kilitler
        for model_name in ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro']:
            try:
                m = genai.GenerativeModel(model_name)
                m.generate_content("test") # Isınma turu
                return m
            except:
                continue
        return None
    except:
        return None

model_engine = load_ai_engine()

# --- 2. PREMIUM NEON TASARIM & BALONCUKLAR ---
st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; text-align: center; }
    
    /* Neon Buton Tasarımı */
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; width: 100%; height: 60px;
        font-weight: bold; border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 30px #00f2fe; }
    
    /* Rapor Kartı Tasarımı */
    .report-card {
        background: rgba(16, 21, 31, 0.9); padding: 25px; border-radius: 20px;
        border: 2px solid #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
        font-size: 16px; line-height: 1.6;
    }
    </style>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js" style="position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 80 }, "color": { "value": "#00f2fe" },
            "shape": { "type": "circle" }, "opacity": { "value": 0.5 },
            "size": { "value": 3 }, "line_linked": { "enable": true, "distance": 150, "color": "#4facfe", "opacity": 0.4, "width": 1 },
            "move": { "enable": true, "speed": 2 }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL VE KOÇLUK AKIŞI ---
st.title("🪞 MirrorAI: Geleceğin Sağlık Aynası")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🌐 Veri Girişi")
    isim = st.text_input("Adınız Soyadınız", placeholder="Örn: Ezgi Büyükkaya")
    yas = st.slider("Yaşınız", 1, 100, 22)
    kamera = st.camera_input("Biyometrik Yüz Taraması")

if st.button("ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if model_engine is None:
            st.error("⚠️ Yapay Zeka Motoru Çalıştırılamadı.")
        elif isim and kamera:
            with st.spinner("Dijital koçun raporunu hazırlıyor..."):
                try:
                    # Rapor hazırlama süreci
                    f_yag = random.randint(18, 28)
                    f_enerji = random.randint(70, 95)
                    
                    text_istegi = f"Kullanıcı: {isim}. Yaş: {yas}. Yağ: %{f_yag}. Bana 3 kısa sağlık önerisi ver."
                    
                    response = model_engine.generate_content(text_istegi)
                    st.session_state['mirror_raporu'] = response.text
                except Exception as e:
                    st.error(f"Bağlantı Hatası: {e}")
        else:
            st.warning("Lütfen isim girin ve kamerayı onaylayın.")
   
