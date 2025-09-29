import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Para mi amor 💖", page_icon="💌")
st.title("💖 Página Especial para Loreley 💖")

# 🎵 Música primero
st.subheader("🎶 Nuestras canciones 💕")
st.audio("baby.mp3", format="audio/mp3")
st.audio("pesao.mp3", format="audio/mp3")
st.audio("tocame.mp3", format="audio/mp3")

# Mensaje bonito
st.write("""
Te amo Loreley 😘,  
Quiero que sepas que eres la persona más increíble del mundo.  
Cada día me haces sonreír y estoy muy agradecido por tenerte en mi vida. 💕✨
""")

# Imagen
imagen = Image.open("amor.jpg")
st.image(imagen, caption="Mi amor 💖", use_container_width=True)

# Mensaje adicional
st.write("""
🌹 Eres mi sol en los días nublados.  
🌟 Cada momento contigo es un tesoro.  
💌 Esta página es solo un pequeño recordatorio de cuánto te quiero.
""")

# Mensaje final
st.write("Espero que te guste esta sorpresa 💖😘")
