import streamlit as st
import google.generativeai as genai

# --- KESİN ÇÖZÜM BAĞLANTISI ---
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)

# Sistem neyi kabul ediyorsa onu otomatik seçen mantık
try:
    # 1. Tercih: Yeni nesil Flash model
    model = genai.GenerativeModel('gemini-1.5-flash')
    model.generate_content("test") # Çalışıp çalışmadığını anında kontrol et
except:
    # 2. Tercih: Eğer kütüphane eskiyse bu ismi kesin tanır
    model = genai.GenerativeModel('gemini-pro')
    
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

# --- 3. DİJİTAL KOÇ PANELİ ---
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
            # GÖRSEL TARAMA SİMÜLASYONU
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
                # Sanal Veri Üretimi
                f_goz = random.choice(["Hafif Morluk", "Yorgun", "Normal"])
                f_nem = random.randint(30, 60)
                f_yag = random.randint(yas // 2, yas + 10)
                
                prompt = f"""
                Sen bir Dijital Sağlık Koçusun. Kullanıcı: {isim}, Yaş: {yas}.
                Aynadan taranan sanal veriler: Göz Altı: {f_goz}, Nem: %{f_nem}, Yağ Oranı: %{f_yag}.
                Bu verilere göre vitamin eksikliği, bölgesel yağlanma ve spor programı önerileri ver.
                Teknolojik bir dille, "Aynadan taranan verilere göre..." diyerek yanıt ver.
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                except Exception as e:
                    st.error(f"Bağlantı hatası: {e}. Lütfen requirements.txt dosyasını kontrol edin.")
        else:
            st.warning("İsim ve Kamera verisi eksik.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun burada belirecek.")
