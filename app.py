import streamlit as st
import google.generativeai as genai

# --- 1. YAPAY ZEKA AYARI ---
# Anahtarını buraya doğrudan tırnak içine yapıştırıyoruz
genai.configure(api_key="AIzaSyBzDTPzJmUovHk-DBxenQfDJ4i5nHlRUgM")
model = genai.GenerativeModel('gemini-pro')

# --- 2. GÖRSEL TASARIM ---
st.set_page_config(page_title="MirrorAI | Güvenli Sağlık Analizi", layout="wide")

st.markdown("""
<style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { background: linear-gradient(45deg, #ff4b4b, #b22222); color: white; border-radius: 10px; font-weight: bold; border: none; height: 3em; width: 100%; }
    .mirror-result { background-color: #111; border: 1px solid #333; padding: 25px; border-radius: 15px; border-left: 5px solid #ff4b4b; }
</style>
""", unsafe_allow_html=True)

st.title("🪞 MirrorAI: Akıllı Biyometrik Tarama")
st.write("SKA 3: Sağlıklı Yaşam | Vitamin & Alerji Analizi")

# --- 3. GİRİŞ PANELİ ---
with st.sidebar:
    st.header("🧬 Biyometrik Giriş")
    bulgu = st.multiselect("Ayna Taraması Bulguları:", 
                            ["Solgun Cilt", "Göz Altı Morlukları", "Dudak Çatlakları", "Tırnak Lekeleri", "Saç Dökülmesi"])
    
    st.header("⚠️ Hassasiyetler")
    alerji = st.multiselect("Bilinen Alerjiler:", 
                             ["Gluten", "Laktoz", "Kuruyemiş", "Polen"])
    
    st.header("📅 Yaşam Tarzı")
    gunes = st.select_slider("Güneş Maruziyeti:", options=["Hiç", "Çok Az", "Yeterli"])

    analiz_et = st.button("ANALİZİ BAŞLAT")

# --- 4. AI ANALİZ VE PAZARLAMA ---
if analiz_et:
    with st.spinner("DNA ve Alerjen verileri işleniyor..."):
        prompt = f"""
        Sen MirrorAI isimli bir sağlık koçusun. 
        Veriler: Bulgular: {bulgu}, Alerjiler: {alerji}, Güneş: {gunes}.
        1. Vitamin eksikliği (Demir, B12, D) riskini sarsıcı bir pazarlama diliyle anlat.
        2. Alerji uyarısı yap.
        3. Kullanıcıya özel 1 takviye ve 1 alet öner.
        """
        try:
            res = model.generate_content(prompt)
            st.markdown(f"<div class='mirror-result'>{res.text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("API Key eksik veya hatalı!")
