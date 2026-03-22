import streamlit as st
import google.generativeai as genai
import time
import random # Sanal veri üretmek için

# --- 1. API ANAHTARI VE YAPILANDIRMA ---
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

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
        font-size: 18px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 30px #00f2fe; }
    
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
    # Kamera inputunu hala tutuyoruz ama veriyi "fake" analiz için kullanmıyoruz, sadece kullanıcı baksın diye.
    kamera = st.camera_input("Ayna Paneli")

    if st.button("AYNADAN TARAMAYI VE ANALİZİ BAŞLAT"):
        if isim and kamera:
            # SİMÜLASYON ADIMLARI
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # 1. Tarama Animasyonu (Simüle ediliyor)
            for percent_complete in range(100):
                time.sleep(0.02) # Tarama hızı
                progress_bar.progress(percent_complete + 1)
                if percent_complete < 30: status_text.text("Yüz hatları taranıyor...")
                elif percent_complete < 60: status_text.text("Cilt dokusu analiz ediliyor...")
                else: status_text.text("Yağ oranı ve postür ölçülüyor...")
            
            # 2. Başarı Bildirimi (Toast)
            st.toast(f"✅ Biyometrik Veriler Aynadan Başarıyla Çekildi!", icon='🌐')
            
            with st.spinner("Dijital koçun derin raporunu hazırlıyor..."):
                # 3. SANAL BİYOMETRİK VERİ OLUŞTURMA (FAKE IT)
                # Burası sihirli kısım! Rastgele ama mantıklı veriler üretiyoruz.
                fake_goz_alti = random.choice(["Hafif Morluk", "Belirgin Yorgunluk", "Normal"])
                fake_cilt_nem = random.randint(30, 70) # % Nem
                fake_yag_orani = random.randint(yas // 2, yas + 10) # Yaşa göre rastgele yağ oranı
                
                # ÖZEL KOÇLUK KOMUTU (Sanal verileri Gemini'a veriyoruz)
                prompt = f"""
                Sen bir Dijital Sağlık Koçusun. Kullanıcı ismi: {isim}, Yaş: {yas}.
                Aynadan (biyometrik taramadan) gelen gerçek zamanlı veriler şunlar (şu an simüle ediliyor):
                - Göz Altı Durumu: {fake_goz_alti}
                - Cilt Nem Oranı: %{fake_cilt_nem}
                - Vücut Yağ Oranı Tahmini: %{fake_yag_orani}

                Bu verilere dayanarak kullanıcıya şok edici derecede isabetli bir koçluk raporu yaz. 
                Raporun şunları içermeli:
                1. Bu verilerin (göz altı morluğu vs.) ne anlama geldiği ve hangi vitaminlerin (Demir, B, D) eksik olabileceği.
                2. Bu yağ oranına göre bölgesel yağlanma analizi ve hangi sporların (Haftada kaç gün, kaç dakika) yapılması gerektiği.
                3. Yaşam tarzı ve beslenme önerileri.
                
                Teknolojik, samimi ve uzman bir dille, "Aynadan taranan verilere göre..." diyerek yanıt ver. 
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
            st.warning("Lütfen tarama için kamerayı açın.")

with col2:
    st.subheader("🤖 MirrorAI Koçluk Raporu")
    if 'koç_raporu' in st.session_state:
        st.markdown(f'<div class="report-card">{st.session_state["koç_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.write("Analiz raporun ve sağlık yol haritan burada belirecek. Hazırsan başlayalım!")
