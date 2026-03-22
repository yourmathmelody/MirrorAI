import streamlit as st
import google.generativeai as genai
import time

# --- 1. TAM VE KESİN API ANAHTARI YAPILANDIRMASI ---
# Senin verdiğin tam anahtarı tırnakların arasına, boşluksuz yerleştirdim.
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)

# En akıllı modelimizi seçiyoruz
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. GÖRSEL TASARIM (MAVİ-YEŞİL NEON & BALONCUKLAR) ---
st.set_page_config(page_title="MirrorAI | Dijital Sağlık Koçu", layout="wide")

st.markdown("""
    <style>
    /* Arka Plan ve Neon Renkler */
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2, h3 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; }
    
    /* Şık Neon Buton */
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; font-weight: bold; width: 100%; height: 60px;
        border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 30px #00f2fe; }
    
    /* Analiz Raporu Kartı */
    .report-card {
        background: rgba(16, 21, 31, 0.9); padding: 25px; border-radius: 20px;
        border: 2px solid #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
        font-size: 16px; line-height: 1.6;
    }
    </style>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js" style="position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1; pointer-events: none;"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 100, "density": { "enable": true, "value_area": 800 } },
            "color": { "value": "#00f2fe" },
            "shape": { "type": "circle" },
            "opacity": { "value": 0.4 },
            "size": { "value": 3, "random": true },
            "line_linked": { "enable": true, "distance": 150, "color": "#4facfe", "opacity": 0.3, "width": 1 },
            "move": { "enable": true, "speed": 3, "direction": "none", "random": true, "straight": false, "out_mode": "out" }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ARAYÜZ ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🪞 MirrorAI")
    st.write("### Dijital Sağlık & Yaşam Koçun")
    
    # Giriş: İsim ve Yaş
    isim = st.text_input("İsim Soyisim")
    yas = st.slider("Yaşınız", 1, 100, 25)
    
    st.info("Kameraya bakın, biyometrik verileriniz ayna tarafından işleniyor...")
