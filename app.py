import streamlit as st
import google.generativeai as genai
import time
import random

# --- 1. API ANAHTARI VE YAPILANDIRMA ---
API_KEY = "AIzaSyD6XOsY27_LflguRU2SEcjYQk27e3s8FKc"
genai.configure(api_key=API_KEY)

# HATA VERMEYEN MODEL TANIMLAMA
try:
    # En garanti model ismi budur (KÜÇÜK HARFLE!)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    model = genai.GenerativeModel('gemini-pro')
