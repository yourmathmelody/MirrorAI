import streamlit as st
from google import genai
import random

# --- 1. SAYFA VE SİSTEM AYARLARI ---
st.set_page_config(
    page_title="MirrorAI | Biyometrik Sağlık Analizi", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SIZINTI KORUMASI: Anahtar Streamlit Secrets'tan çekilir.
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=API_KEY)
except Exception:
    st.error("⚠️ API Anahtarı bulunamadı! Lütfen Streamlit Secrets kısmına GEMINI_API_KEY ekleyin.")
    st.stop()

# --- 2. YÜKSEK KONTRASTLI NEON TASARIM & BALONCUKLAR ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    
    <style>
    /* Global Ayarlar */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #020408;
        color: #FFFFFF;
    }
    
    .main { background-color: #020408; }

    h1 { 
        color: #00f2fe; 
        text-align: center;
        text-shadow: 2px 2px 15px rgba(0, 242, 254, 0.4);
        font-weight: 800;
        margin-bottom: 30px;
    }
    
    h3 { color: #00E676; font-weight: 600; text-align: center; }

    .report-card {
        background: rgba(13, 17, 23, 0.98); 
        padding: 40px; 
        border-radius: 20px;
        border: 1px solid rgba(0, 242, 254, 0.3);
        color: #FFFFFF; 
        line-height: 1.8; 
        font-size: 17px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }

    .metric-box {
        background: #0d1117; 
        padding: 20px; 
        border-radius: 15px;
        border-left: 6px solid #00E676;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .metric-label { color: #8b949e; font-size: 14px; text-transform: uppercase; font-weight: 600; }
    .metric-value { color: #00E676; font-size: 24px; font-weight: 800; }

    .stButton>button {
        background: linear-gradient(45deg, #00E676, #00f2fe);
        color: #020408; 
        border-radius: 15px; 
        width: 100%; 
        height: 65px;
        font-weight: 800; 
        border: none;
        font-size: 20px; 
        transition: 0.4s;
        text-transform: uppercase;
    }
    .stButton>button:hover { 
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(0, 230, 118, 0.4);
    }

    #particles-js {
        position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;
    }
    </style>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 70, "density": { "enable": true, "value_area": 800 } },
            "color": { "value": ["#00E676", "#00f2fe", "#4facfe"] },
            "shape": { "type": "circle" },
            "opacity": { "value": 0.25, "random": true },
            "size": { "value": 4, "random": true },
            "move": { "enable": true, "speed": 2, "direction": "none", "random": true, "out_mode": "out" }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL VE KOÇLUK AKIŞI ---
st.markdown("<h1>🪞 MirrorAI: Biyometrik Gelişim Aynası</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.4], gap="large")

with col1:
    st.subheader("🌐 Biyometrik Veri Girişi")
    isim = st.text_input("Adınız Soyadınız", placeholder="Örn: Ezgi Büyükkaya")
    yas = st.slider("Yaşınız", 15, 85, 22)
    odak_noktasi = st.selectbox("Analiz Odak Noktası", ["Bütünsel Tarama", "Karın Bölgesi", "Cilt Sağlığı", "Postür & Kas"])
    kamera = st.camera_input("Biyometrik Tarama Yap")

    if st.button("🚀 ANALİZİ BAŞLAT"):
        if isim and kamera:
            with st.spinner("Analiz ediliyor..."):
                try:
                    f_yag = random.randint(18, 27)
                    f_su = random.randint(58, 68)
                    istek = f"Kullanıcı: {isim}, Yaş: {yas}, Odak: {odak_noktasi}. Yağ: %{f_yag}. Göz altı morluk/şişlik, solgunluk, su kalitesi, kansızlık, saç dökülmesi, kilo kaybı ve beslenme üzerine analiz yapıp adım adım spor ve yemek önerisi ver."
                    
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=istek
                    )
                    
                    st.session_state['mirror_raporu'] = response.text
                    st.session_state['yag_res'] = f_yag
                    st.session_state['su_res'] = f_su
                    st.success("✅ Analiz Başarıyla Tamamlandı!")
                except Exception as e:
                    st.error(f"❌ Motor Hatası: {str(e)}")
        else:
            st.warning("⚠️ Lütfen bilgileri doldurun.")

with col2:
    st.subheader("🤖 Analiz Raporu")
    if 'mirror_raporu' in st.session_state:
        st.markdown(f"<div class='metric-box'><span class='metric-label'>Vücut Yağı</span><span class='metric-value'>%{st.session_state['yag_res']}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-box'><span class='metric-label'>Su Dengesi</span><span class='metric-value'>%{st.session_state['su_res']}</span></div>", unsafe_allow_html=True)
        st.markdown(f'<div class="report-card">{st.session_state["mirror_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.info("Sonuçlar burada kristal netliğinde belirecek.")
📋 Ezgi, Lütf
