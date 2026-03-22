import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. API ANAHTARI VE YAPILANDIRMA ---
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)

# HATA ÇÖZÜMÜ: Modeli tam yoluyla (models/) tanımlıyoruz
try:
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except:
    # Eğer yukarıdaki olmazsa en garanti eski sürümü deniyoruz
    model = genai.GenerativeModel('gemini-pro')

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

# --- 3. ARAYÜZ ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🪞 MirrorAI")
    st.write("### Sağlık & Yaşam Koçun")
    
    isim = st.text_input("İsim Soyisim")
    yas = st.slider("Yaşınız", 1, 100, 25)
    
    st.info("Kameraya bakın, ayna biyometrik verilerinizi tarayacak.")
    kamera = st.camera_input("Ayna Paneli")

    if st.button("AYNADAN TARAMAYI VE ANALİZİ BAŞLAT"):
        if isim and kamera:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                if percent_complete < 30: status_text.text("Yüz hatları taranıyor...")
                elif percent_complete < 60: status_text.text("Cilt dokusu analiz ediliyor...")
                else: status_text.text("Yağ oranı ve postür ölçülüyor...")
            
            st.toast(f"✅ Biyometrik Veriler Aynadan Başarıyla Çekildi!", icon='🌐')
            
            with st.spinner("Dijital koçun derin raporunu hazırlıyor..."):
                fake_goz_alti = random.choice(["Hafif Morluk", "Belirgin Yorgunluk", "Normal"])
                fake_cilt_nem = random.randint(30, 70)
                fake_yag_orani = random.randint(yas // 2, yas + 10)
                
                prompt = f"""
                Sen bir Dijital Sağlık Koçusun. Kullanıcı ismi: {isim}, Yaş: {yas}.
                Aynadan taranan sanal veriler:
                - Göz Altı: {fake_goz_alti}
                - Cilt Nem: %{fake_cilt_nem}
                - Yağ Oranı: %{fake_yag_orani}
                Bu verilere göre vitamin eksikliği, bölgesel yağlanma ve haftalık spor ihtiyacı önerileri ver.
                Samimi ve uzman bir dille, "Aynadan taranan verilere göre..." diyerek yanıt ver.
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                except Exception as e:
                    # Hata burada yakalanırsa ekrana basıyoruz
                    st.error(f"Bağlantı sorunu: {e}")
        else:
            st.warning("Lütfen isim girin ve kamerayı açın.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun burada belirecek.")
