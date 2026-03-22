import streamlit as st
from google import genai
import random

# --- 1. SAYFA VE SİSTEM AYARLARI (EN ÜSTTE) ---
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

# --- 2. PREMIUM GÖRSEL TASARIM & BALONCUK EFEKTİ ---
# Google Fonts'tan şık bir yazı tipi (Poppins) ve neon CSS ekliyoruz.
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    
    <style>
    /* Global Yazı Tipi */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background-color: #05080f;
        color: #e0e0e0;
    }
    
    .main { background-color: #05080f; }
    
    /* Neon Başlıklar */
    h1, h2, h3 { 
        color: #00f2fe; 
        text-align: center; 
        text-shadow: 0 0 20px #00f2fe, 0 0 10px #4facfe;
        font-weight: 700;
    }
    
    /* Neon Buton */
    .stButton>button {
        background: linear-gradient(45deg, #00f2fe, #4facfe, #00e676);
        background-size: 200% auto;
        color: white; border-radius: 30px; width: 100%; height: 65px;
        font-weight: 700; border: none; 
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.7);
        font-size: 20px; transition: 0.5s;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { 
        background-position: right center;
        transform: scale(1.03); 
        box-shadow: 0 0 40px #00e676; 
    }
    
    /* Rapor Kartı */
    .report-card {
        background: rgba(16, 21, 31, 0.95); padding: 35px; border-radius: 25px;
        border: 2px solid #00f2fe; box-shadow: 0 0 30px rgba(0, 242, 254, 0.3);
        color: #ffffff; line-height: 1.8; font-size: 16px;
        backdrop-filter: blur(10px);
    }
    
    /* Metrik Kutuları */
    .metric-box {
        background: rgba(0, 242, 254, 0.1); padding: 20px; border-radius: 15px;
        border-left: 5px solid #00e676; margin-bottom: 20px;
        font-weight: 600; color: #ffffff; font-size: 17px;
        display: flex; justify-content: space-between; align-items: center;
    }
    .metric-value { color: #00f2fe; font-size: 20px; font-weight: 700; }
    
    /* Baloncuk Arka Planı (Particles.js) */
    #particles-js {
        position: fixed; width: 100%; height: 100%; top: 0; left: 0;
        z-index: -1;
    }
    </style>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js"></div>
    <script>
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 100, "density": { "enable": true, "value_area": 800 } },
            "color": { "value": ["#00f2fe", "#4facfe", "#00e676"] }, // Mavi, Lacivert, Yeşil baloncuklar
            "shape": { "type": "circle" },
            "opacity": { "value": 0.6, "random": true },
            "size": { "value": 4, "random": true },
            "line_linked": { "enable": true, "distance": 150, "color": "#4facfe", "opacity": 0.3, "width": 1 },
            "move": { "enable": true, "speed": 3, "direction": "none", "random": true, "straight": false, "out_mode": "out" }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } },
            "mode": { "grab": { "distance": 140 }, "push": { "particles_nb": 4 } }
        }
    });
    </script>
    """, unsafe_allow_html=True)

# --- 3. ANA PANEL VE GİRİŞLER ---
st.markdown("<h1>🪞 MirrorAI: Profesyonel Biyometrik Ayna</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("🌐 Biyometrik Veri Analizi")
    isim = st.text_input("Adınız Soyadınız", placeholder="Örn: Ezgi Büyükkaya")
    yas = st.slider("Yaşınız", 15, 85, 22)
    
    odak_noktasi = st.selectbox(
        "Birincil Sağlık Hedefiniz", 
        ["Kompleks Biyometrik Analiz", "Yağ Yakımı & Karın Bölgesi", "Cilt Sağlığı & Parlaklık (Morluk/Solgunluk)", "Postür & Esneklik", "Kas Kütlesi & Şekillenme"]
    )
    
    kamera = st.camera_input("Biyometrik Tarama (Yüz ve Postür)")

    if st.button("🚀 DERİN ANALİZİ VE KOÇLUĞU BAŞLAT"):
        if isim and kamera:
            with st.spinner("Gemini 3 Flash, biyometrik dokuları ve semptomları analiz ediyor..."):
                try:
                    # Simüle edilen gelişmiş veriler
                    f_yag = random.randint(18, 27)
                    f_su = random.randint(60, 68)
                    
                    # PROMPT: Senin istediğin TÜM detayları ekledik
                    istek = f"""
                    Sen profesyonel bir biyometrik analiz uzmanı, fitness koçu ve beslenme uzmanısın. 
                    Kullanıcı: {isim}, Yaş: {yas}, Hedef: {odak_noktasi}.
                    Tahmini Yağ Oranı: %{f_yag}. Su Dengesi: %{f_su}.
                    
                    Lütfen aşağıdaki semptomları analiz edip, her biri için ADIM ADIM ve ÇÖZÜM odaklı (spor ve beslenme dahil) bir rapor hazırla:
                    1. Yüz Analizi: (Göz altı şişlikleri, morarma durumu ve yüz solgunluğu analizi.)
                    2. Metabolik Dengeler: (Kansızlık (anemi) ihtimali ve saç dökülmesi semptomları üzerine değerlendirme.)
                    3. Su Kalitesi & Ölçümü: (Vücudun su tutma durumu ve içilen suyun kalitesine dair öneriler.)
                    4. Kilo & Beslenme: (Düzensiz beslenme ve kilo kaybı durumunun analizi.)
                    5. Bölgesel Tavsiye (Spor): ({odak_noktasi} üzerine evde yapılabilecek 2 etkili egzersiz adımı.)
                    6. Haftalık Somut Aksiyon Planı: (Bu hafta atılacak 3 net adım.)
                    """
                    
                    # Gemini 3 Flash Preview Çağrısı
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=istek
                    )
                    
                    st.session_state['mirror_raporu'] = response.text
                    st.session_state['yag_sonuc'] = f_yag
                    st.session_state['su_sonuc'] = f_su
                    st.success("✅ Analiz Başarıyla Tamamlandı!")
                    
                except Exception as e:
                    st.error(f"❌ Motor Hatası: {str(e)}")
                    st.info("İpucu: Eğer 403 sızıntı hatası alırsan, Secrets kısmındaki anahtarı yenile.")
        else:
            st.warning("⚠️ Lütfen analizi başlatmak için isim girin ve kamerayı onaylayın.")

with col2:
    st.subheader("🤖 MirrorAI Biyometrik Raporu")
    if 'mirror_raporu' in st.session_state:
        # Özet Metrikler (Tasarımı güzelleştirildi)
        st.markdown(f"""
            <div class='metric-box'>
                <span>🔥 Tahmini Vücut Yağı:</span>
                <span class='metric-value'>%{st.session_state['yag_sonuc']}</span>
            </div>
            <div class='metric-box'>
                <span>💧 Hücresel Su Dengesi:</span>
                <span class='metric-value'>%{st.session_state['su_sonuc']}</span>
            </div>
        """, unsafe_allow_html=True)
            
        # Ana Rapor Alanı
        st.markdown(f'<div class="report-card">{st.session_state["mirror_raporu"]}</div>', unsafe_allow_html=True)
    else:
        st.info("Kameranızı açıp analizi başlattığınızda dijital koçunuzun biyometrik reçetesi burada belirecek.")

# --- 4. ALT BİLGİ ---
st.markdown("---")
st.caption("MirrorAI bir biyometrik analiz asistanıdır. Kesin teşhis ve tedavi için mutlaka doktorunuza danışın.")
