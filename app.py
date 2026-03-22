import streamlit as st
import google.generativeai as genai

# 1. API ANAHTARI AYARI
genai.configure(api_key="AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc")

# 2. DOĞRU MODELİ OTOMATİK BULMA
try:
    # Google'dan senin için çalışan modellerin listesini istiyoruz
    modeller = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Eğer liste boş değilse ilk sıradakini (en güncelini) al, yoksa varsayılan gemini-pro'yu kullan
    secilen_model = modeller[0] if modeller else "models/gemini-pro"
    model = genai.GenerativeModel(secilen_model)
except Exception as e:
    st.error(f"Modellere erişilemedi: {e}")
    secilen_model = "models/gemini-pro"
    model = genai.GenerativeModel(secilen_model)

# 3. GÖRSEL TASARIM
st.set_page_config(page_title="MirrorAI | Analiz", layout="wide")
st.title("🪞 MirrorAI: Akıllı Tarama")

if st.button("ANALİZİ BAŞLAT"):
    try:
        response = model.generate_content("Merhaba, sistem testi başarılı mı?")
        st.success(f"✅ Başarılı! Kullanılan Model: {secilen_model}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Hala bir sorun var: {e}")
