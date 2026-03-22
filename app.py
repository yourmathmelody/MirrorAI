import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. GÜNCEL API ANAHTARI VE MODEL BAĞLANTISI ---
# Senin verdiğin tam anahtarı buraya hatasız yerleştirdim.
API_KEY = "AIzaSyDaLtQymBdqwTvoguXrRyd-F174kFhsn7s"
genai.configure(api_key=API_KEY)

# Hata vermeyen, her sürümde çalışan model seçici
@st.cache_resource
def load_model():
    for m_name in ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro']:
        try:
            m = genai.GenerativeModel(m_name)
            m.generate_content("test") # Bağlantı testi
            return m
        except:
            continue
    return None

model = load_model()

# --- 2. GÖRSEL TASARIM (MAVİ-YEŞİL NEON & BALONCUKLAR) ---
st.set_page_config(page_title="MirrorAI | Dijital Sağlık Koçu", layout="wide")

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

# --- 3. DİJİTAL KOÇ PANELİ ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🪞 MirrorAI")
    st.write("### Dijital Sağlık & Yaşam Koçun")
    
    isim = st.text_input("İsim Soyisim")
    yas = st.slider("Yaşınız", 1, 100, 25)
    
    st.info("Kameraya bakın, biyometrik verileriniz ayna tarafından işleniyor...")
    kamera = st.camera_input("Biyometrik Tarama Paneli")

    if st.button("ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if model is None:
            st.error("⚠️ Yapay zeka motoru şu an başlatılamadı. Lütfen API anahtarını kontrol edin.")
        elif isim and kamera:
            # GÖRSEL TARAMA SİMÜLASYONU
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for percent_complete in range(101):
                time.sleep(0.01)
                progress_bar.progress(percent_complete)
                if percent_complete < 30: status_text.text("Yüz hatları taranıyor...")
                elif percent_complete < 70: status_text.text("Cilt dokusu analiz ediliyor...")
                else: status_text.text("Yağ oranı ve postür ölçülüyor...")
            
            # Bildirim: Veriler Çekildi
            st.toast(f"✅ Biyometrik Veriler Aynadan Başarıyla Çekildi!", icon='🌐')
            
            with st.spinner("Dijital koçun derin raporunu hazırlıyor..."):
                # Sanal Veri Üretimi (Fake it 'til you make it!)
                f_goz = random.choice(["Hafif Morluk", "Belirgin Yorgunluk", "Normal"])
                f_nem = random.randint(30, 65)
                f_yag = random.randint(yas // 2, yas + 12)
                
                prompt = f"""
                Sen profesyonel bir Dijital Sağlık Koçusun. Kullanıcı: {isim}, Yaş: {yas}.
                Aynadan taranan sanal veriler: Göz Altı: {f_goz}, Cilt Nem: %{f_nem}, Tahmini Yağ Oranı: %{f_yag}.
                Buna göre; vitamin eksikliği, bölgesel yağlanma analizi, haftalık spor programı ve beslenme önerileri ver.
                Mavi-yeşil neon teknolojik bir dille, "Aynadan taranan verilere göre..." diyerek samimi bir rapor yaz.
                (Not: Tıbbi tavsiye değildir uyarısını ekle.)
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                except Exception as e:
                    st.error(f"Bağlantı sorunu oluştu: {e}")
        else:
            st.warning("Lütfen isim girin ve kamerayı kullanın.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state['koç_raporu']}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun burada belirecek. Aynaya bakmaya hazır mısın?")
