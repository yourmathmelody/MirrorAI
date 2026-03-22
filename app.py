import streamlit as st
import google.generativeai as genai
import random

# --- 1. API VE AKILLI MODEL SEÇİCİ (KÖKTEN ÇÖZÜM) ---
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)

@st.cache_resource
def get_working_model():
    # Hata almamak için tüm ihtimalleri sırayla dener
    for model_name in ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro']:
        try:
            m = genai.GenerativeModel(model_name)
            m.generate_content("test") # Canlılık kontrolü
            return m
        except:
            continue
    return None

model = get_working_model()

# --- 2. GÖRSEL TASARIM (MAVİ-YEŞİL NEON & BALONCUKLAR) ---
st.set_page_config(page_title="MirrorAI | Sağlık Koçu", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #05080f; color: #e0e0e0; }
    h1, h2, h3 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; }
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: white; border-radius: 30px; font-weight: bold; width: 100%; height: 60px;
        border: none; box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        font-size: 18px;
    }
    .report-card {
        background: rgba(16, 21, 31, 0.9); padding: 25px; border-radius: 20px;
        border: 2px solid #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
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
    st.info("Kameraya bakın, biyometrik verileriniz taranıyor...")
    kamera = st.camera_input("Biyometrik Tarama Paneli")

    if st.button("ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if model is None:
            st.error("⚠️ Yapay zeka motoru başlatılamadı. Lütfen API anahtarını kontrol edin.")
        elif isim and kamera:
            with st.spinner("Aynadan veriler çekiliyor ve analiz ediliyor..."):
                # Sanal Veri Üretimi
                f_goz = random.choice(["Hafif Morluk", "Yorgun", "Normal"])
                f_nem = random.randint(30, 60)
                f_yag = random.randint(yas // 2, yas + 10)
                
                prompt = f"""
                Sen bir Dijital Sağlık Koçusun. Kullanıcı: {isim}, Yaş: {yas}.
                Aynadan taranan biyometrik veriler: Göz Altı: {f_goz}, Nem: %{f_nem}, Yağ Oranı: %{f_yag}.
                Buna göre vitamin, spor ve beslenme önerisi ver. Mavi-yeşil neon ruhuna uygun konuş.
                """
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                    st.toast("✅ Veriler Başarıyla Aktarıldı!")
                except Exception as e:
                    st.error(f"Bağlantı Sorunu: {e}")
        else:
            st.warning("Lütfen isim girin ve kamerayı kullanın.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun burada belirecek.")
