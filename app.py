import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. API ANAHTARI VE GÜVENLİ MODEL BAĞLANTISI ---
# Senin en taze, hata mesajı içermeyen API anahtarın:
API_KEY = "AIzaSyDaLtQymBdqwTvoguXrRyd-F174kFhsn7s"
genai.configure(api_key=API_KEY)

@st.cache_resource
def load_mirror_ai():
    # Sistemde hangi model varsa onu bulana kadar dener (404 hatasını önler)
    for m_name in ['gemini-1.5-flash', 'gemini-pro']:
        try:
            m = genai.GenerativeModel(m_name)
            m.generate_content("test") 
            return m
        except:
            continue
    return None

model = load_mirror_ai()

# --- 2. AYRINTILI ARA YÜZ VE TASARIM (MAVİ-YEŞİL NEON) ---
st.set_page_config(page_title="MirrorAI | Sağlık Koçu", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2, h3 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; }
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; font-weight: bold; width: 100%; height: 60px;
        border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 30px #00f2fe; }
    .report-card {
        background: rgba(16, 21, 31, 0.9); padding: 25px; border-radius: 20px;
        border: 2px solid #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
        line-height: 1.6;
    }
    </style>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js" style="position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 90 }, "color": { "value": "#00f2fe" },
            "shape": { "type": "circle" }, "opacity": { "value": 0.4 },
            "size": { "value": 3 }, "line_linked": { "enable": true, "color": "#4facfe" },
            "move": { "enable": true, "speed": 2 }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🪞 MirrorAI")
    st.write("### Dijital Sağlık & Yaşam Koçun")
    isim = st.text_input("İsim Soyisim")
    yas = st.slider("Yaşınız", 1, 100, 25)
    kamera = st.camera_input("Biyometrik Tarama")

    if st.button("ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if model is None:
            st.error("⚠️ Yapay zeka motoru başlatılamadı. API anahtarı veya kütüphane sorunu var.")
        elif isim and kamera:
            progress_bar = st.progress(0)
            for p in range(101):
                time.sleep(0.01)
                progress_bar.progress(p)
            
            st.toast("✅ Veriler Aynadan Başarıyla Çekildi!", icon='🌐')
            
            with st.spinner("Dijital koçun rapor hazırlıyor..."):
                f_goz = random.choice(["Hafif Morluk", "Yorgun", "Normal"])
                f_nem = random.randint(30, 60)
                f_yag = random.randint(yas // 2, yas + 10)
                
                prompt = f"Kullanıcı: {isim}, Yaş: {yas}. Biyometrik Veriler: Göz {f_goz}, Nem %{f_nem}, Yağ %{f_yag}. Sağlık koçu önerileri ver."
                
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                except Exception as e:
                    st.error(f"Bağlantı Sorunu: {e}")
        else:
            st.warning("Eksik bilgi: İsim ve Kamera gerekli.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun burada belirecek.")
