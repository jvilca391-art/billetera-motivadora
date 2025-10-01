import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(
    page_title="Quiz de IA y Programación",
    page_icon="🤖",
    layout="centered"
)

# Título principal
st.title("🤖 Quiz de IA y Programación")
st.markdown("Pon a prueba tus conocimientos básicos de programación e inteligencia artificial")
st.markdown("---")

# Inicializar estado del quiz
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'puntuacion' not in st.session_state:
    st.session_state.puntuacion = 0
if 'quiz_completado' not in st.session_state:
    st.session_state.quiz_completado = False
if 'respuesta_seleccionada' not in st.session_state:
    st.session_state.respuesta_seleccionada = None

# Base de datos de preguntas de IA y programación
preguntas = [
    {
        "pregunta": "¿Qué significa 'IA'?",
        "opciones": ["Inteligencia Artificial", "Interfaz Automatizada", "Internet Avanzado", "Información Asistida"],
        "respuesta_correcta": "Inteligencia Artificial",
        "explicacion": "IA significa Inteligencia Artificial, que se refiere a máquinas que pueden realizar tareas que normalmente requieren inteligencia humana."
    },
    {
        "pregunta": "¿Qué lenguaje se usa comúnmente para ciencia de datos y IA?",
        "opciones": ["Java", "Python", "C++", "HTML"],
        "respuesta_correcta": "Python",
        "explicacion": "Python es muy popular en ciencia de datos e IA por sus librerías como TensorFlow, PyTorch y scikit-learn."
    },
    {
        "pregunta": "¿Qué es un 'chatbot'?",
        "opciones": [
            "Un programa que chatea con personas",
            "Un tipo de virus informático", 
            "Un dispositivo hardware",
            "Un lenguaje de programación"
        ],
        "respuesta_correcta": "Un programa que chatea con personas",
        "explicacion": "Un chatbot es un programa diseñado para simular conversaciones con usuarios humanos."
    },
    {
        "pregunta": "¿Qué hace la función 'print()' en Python?",
        "opciones": [
            "Imprime texto en la pantalla",
            "Toma una foto",
            "Calcula números",
            "Detiene el programa"
        ],
        "respuesta_correcta": "Imprime texto en la pantalla",
        "explicacion": "print() muestra texto o variables en la consola o salida del programa."
    },
    {
        "pregunta": "¿Qué es el 'machine learning'?",
        "opciones": [
            "Máquinas que aprenden por sí mismas",
            "Reparar computadoras",
            "Aprender a programar rápido",
            "Un tipo de red social"
        ],
        "respuesta_correcta": "Máquinas que aprenden por sí mismas",
        "explicacion": "Machine Learning es un tipo de IA donde las máquinas aprenden de datos sin ser programadas explícitamente."
    },
    {
        "pregunta": "¿Qué comando se usa para instalar librerías en Python?",
        "opciones": ["pip install", "python get", "download lib", "get package"],
        "respuesta_correcta": "pip install",
        "explicacion": "pip install es el comando para instalar paquetes de Python desde PyPI (Python Package Index)."
    },
    {
        "pregunta": "¿Qué es GitHub?",
        "opciones": [
            "Plataforma para guardar y compartir código",
            "Un juego de programación",
            "Un tipo de computadora",
            "Un lenguaje de programación"
        ],
        "respuesta_correcta": "Plataforma para guardar y compartir código",
        "explicacion": "GitHub es una plataforma donde los desarrolladores almacenan, comparten y colaboran en proyectos de código."
    },
    {
        "pregunta": "¿Qué significa 'HTML'?",
        "opciones": [
            "HyperText Markup Language",
            "HighTech Modern Language", 
            "Hyper Transfer Model Link",
            "Home Tool Markup Language"
        ],
        "respuesta_correcta": "HyperText Markup Language",
        "explicacion": "HTML es el lenguaje estándar para crear páginas web."
    }
]

def reiniciar_quiz():
    st.session_state.pregunta_actual = 0
    st.session_state.puntuacion = 0
    st.session_state.quiz_completado = False
    st.session_state.respuesta_seleccionada = None

# Mostrar progreso
if not st.session_state.quiz_completado:
    progreso = st.session_state.pregunta_actual / len(preguntas)
    st.progress(progreso)
    st.write(f"**Progreso:** {st.session_state.pregunta_actual + 1} de {len(preguntas)} preguntas")

if not st.session_state.quiz_completado:
    # Obtener pregunta actual
    pregunta_actual = preguntas[st.session_state.pregunta_actual]
    
    # Mostrar pregunta
    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1}")
    st.markdown(f"### {pregunta_actual['pregunta']}")
    
    # Mostrar opciones
    for i, opcion in enumerate(pregunta_actual['opciones']):
        if st.button(opcion, key=f"opcion_{i}", use_container_width=True):
            st.session_state.respuesta_seleccionada = opcion
    
    # Verificar respuesta
    if st.session_state.respuesta_seleccionada:
        es_correcta = st.session_state.respuesta_seleccionada == pregunta_actual['respuesta_correcta']
        
        if es_correcta:
            st.success("✅ ¡Correcto!")
            st.session_state.puntuacion += 1
        else:
            st.error(f"❌ Incorrecto")
        
        # Mostrar explicación
        st.info(f"💡 **Explicación:** {pregunta_actual['explicacion']}")
        
        # Botón para continuar
        if st.button("➡️ Siguiente pregunta", type="primary"):
            if st.session_state.pregunta_actual < len(preguntas) - 1:
                st.session_state.pregunta_actual += 1
                st.session_state.respuesta_seleccionada = None
                st.rerun()
            else:
                st.session_state.quiz_completado = True
                st.rerun()

else:
    # Mostrar resultados finales
    st.balloons()
    st.success("🎉 ¡Quiz Completado!")
    
    st.subheader("🏆 Resultados Finales")
    st.write(f"**Puntuación:** {st.session_state.puntuacion} / {len(preguntas)}")
    
    porcentaje = (st.session_state.puntuacion / len(preguntas)) * 100
    st.write(f"**Porcentaje de aciertos:** {porcentaje:.1f}%")
    
    # Mostrar mensaje según puntuación
    col1, col2, col3 = st.columns(3)
    
    with col2:
        if porcentaje == 100:
            st.success("🏆 ¡Perfecto! Eres un crack de la programación")
        elif porcentaje >= 75:
            st.info("👍 ¡Excelente! Tienes buenos conocimientos")
        elif porcentaje >= 50:
            st.warning("😊 Bien, vas por buen camino")
        else:
            st.error("📚 Sigue aprendiendo, ¡la práctica hace al maestro!")
    
    # Botón para reiniciar
    if st.button("🔄 Intentar de nuevo", use_container_width=True, type="primary"):
        reiniciar_quiz()
        st.rerun()

# Sidebar con información
with st.sidebar:
    st.header("📊 Estadísticas")
    st.write(f"**Puntuación actual:** {st.session_state.puntuacion}")
    if not st.session_state.quiz_completado:
        st.write(f"**Preguntas restantes:** {len(preguntas) - st.session_state.pregunta_actual}")
    
    st.markdown("---")
    st.header("🎯 Temas del Quiz")
    st.write("• Inteligencia Artificial")
    st.write("• Programación básica")
    st.write("• Herramientas de desarrollo")
    st.write("• Conceptos tecnológicos")
    
    st.markdown("---")
    if st.button("Reiniciar Quiz", use_container_width=True):
        reiniciar_quiz()
        st.rerun()

# Footer
st.markdown("---")
st.caption("🤖 Quiz de IA y Programación | Creado con Streamlit 🎈")