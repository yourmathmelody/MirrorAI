import streamlit as st
import google.generativeai as genai
import time

# --- 1. TAM VE DOĞRU API ANAHTARI YAPILANDIRMASI ---
# Başına eksik olan 'A' harfini ekledik!
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
    h1, h2, h3 { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; font-family: 'Orbitron', sans-serif; }
    
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
    <div id="particles-js" style="position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 90 },
            "color": { "value": "#00f2fe" },
            "shape": { "type": "circle" },
            "opacity": { "value": 0.4 },
            "size": { "value": 3 },
            "line_linked": { "enable": true, "color": "#4facfe", "distance": 150, "opacity": 0.3 },
            "move": { "enable": true, "speed": 2 }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ARAYÜZ ---
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🪞 MirrorAI")
    st.write("### Dijital Sağlık Koçun")
    
    # Sade Giriş: İsim ve Yaş
    isim = st.text_input("İsim Soyisim")
    yas = st.slider("Yaşınız", 1, 100, 25)
    
    st.info("Kameraya bakın, biyometrik verileriniz ayna tarafından işleniyor...")
    kamera = st.camera_input("Biyometrik Tarama Paneli")

    if st.button("ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if isim and kamera:
            with st.spinner("Yapay zeka koçun verileri tarıyor..."):
                # ÖZEL KOÇLUK KOMUTU
                prompt = f"""
                Sen profesyonel bir Dijital Sağlık Koçusun. Kullanıcı ismi: {isim}, Yaş: {yas}.
                Aynadan (kamera görüntüsünden) gelen verileri şu başlıklarda analiz et:
                1. Yüzdeki yorgunluk, göz altı morluğu, cilt ve dudak kuruluğu durumu.
                2. Olası Demir, B ve D vitamini eksikliği uyarıları.
                3. Vücut yağ oranı tahmini ve bölgesel yağlanma analizi.
                4. Kişiye özel spor ihtiyacı (Hangi spor, haftada kaç gün, kaç dakika?).
                5. Beslenme önerileri ve yaşam tarzı dokunuşları.
                Mavi-yeşil neon teknolojik bir dille, samimi ama uzman bir koç gibi yanıt ver. 
                (Not: Tıbbi tavsiye değildir uyarısını en sona ekle.)
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.session_state['koç_raporu'] = response.text
                except Exception as e:
                    st.error(f"Sistemsel bir sorun oluştu: {e}")
        elif not isim:
            st.warning("Lütfen isminizi girin.")
        else:
            st.warning("Lütfen analiz için kamerayı kullanın.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.
