import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Infiltrado", page_icon="🕵️", layout="centered")

# --- CSS V3.0: DISEÑO MODERNO Y LIMPIO ---
st.markdown("""
    <style>
    /* Importamos la fuente 'Inter' para un look profesional y moderno */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* --- ESTRUCTURA BASE --- */
    .stApp {
        background-color: #0E1117; /* Fondo oscuro premium (no negro puro) */
        color: #E6EDF3; /* Texto blanco roto para no cansar la vista */
        font-family: 'Inter', sans-serif !important;
    }

    /* --- TIPOGRAFÍA --- */
    h1 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 1rem !important;
        text-shadow: none !important; /* Eliminamos sombras cutres */
    }
    
    h2, h3 {
        font-weight: 600 !important;
        color: #E6EDF3 !important;
    }

    /* --- TARJETAS Y CONTENEDORES --- */
    .setup-card, .role-card, .result-card {
        background-color: #161B22; /* Un tono más claro que el fondo */
        padding: 30px;
        border-radius: 16px;
        border: 1px solid #30363D; /* Borde sutil */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .role-card {
        text-align: center;
        font-size: 26px;
        font-weight: 600;
    }

    /* --- BOTONES --- */
    /* Botón Principal (Acción) */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #7C3AED; /* Violeta eléctrico moderno */
        color: white;
        font-weight: 700;
        border: none;
        font-size: 18px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #6D28D9; /* Un poco más oscuro al pasar el ratón */
        transform: translateY(-2px);
    }
    
    /* Botones secundarios (Votación) - Usaremos un truco en el código de Python para diferenciarlos */

    /* --- INPUTS Y LABELS --- */
    .stSelectbox label, .stNumberInput label {
        color: #E6EDF3 !important;
        font-weight: 600;
        font-size: 16px;
    }
    
    /* --- RESULTADOS --- */
    .winner-text { color: #2ea043; font-size: 2rem; font-weight: 800; text-align: center; } /* Verde moderno */
    .loser-text { color: #da3633; font-size: 2rem; font-weight: 800; text-align: center; } /* Rojo moderno */
    .word-reveal { margin-top: 20px; padding: 15px; background: #30363D; border-radius: 8px; text-align: center; }

    </style>
    """, unsafe_allow_html=True)

# --- TUS DATOS (¡IMPORTANTE! SUSTITUYE ESTO POR TU LISTA GIGANTE) ---
DATOS = {
    "⚽ Fútbol": [
        "Real Madrid", "FC Barcelona", "Champions League", "Copa del Mundo",
        "Leo Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Balón de Oro",
        "El Clásico", "Boca Juniors", "Manchester City", "La Liga",
        "Estadio Santiago Bernabéu", "Camp Nou", "Tarjeta Roja", "VAR",
        "Fuera de Juego", "Bota de Oro", "Erling Haaland", "Vinícius Jr",
        "Selección Española", "Inter Miami", "Luis de la Fuente", "Mundial 2030",
        "Árbitro", "Jabulani", "Maradona", "Zidane", "Barça de Guardiola", 
        "La chilena de Cristiano", "Iker Casillas", "Xavi e Iniesta", "El Chiringuito",
        "Kings League", "Un Linier", "Tirar un penalti"
    ],
    "🏀 Deportes": [
        "Baloncesto", "Tenis", "Fórmula 1", "MotoGP", "Pádel", "NBA",
        "Boxeo", "Natación", "Ciclismo", "Golf", "Rugby", "Carlos Alcaraz",
        "Fernando Alonso", "Rafa Nadal", "Marc Márquez", "Juegos Olímpicos",
        "Gimnasio", "Crossfit", "Maratón", "Surf", "Lamine Yamal", "Pau Gasol",
        "Tour de Francia", "Wimbledon", "Super Bowl", "Esquí", "Escalada",
        "Ajedrez", "Yoga", "La 33 de Alonso", "Lanzamiento de jabalina"
    ],
    "📜 Historia": [
        "Pirámides de Egipto", "Imperio Romano", "Cristóbal Colón", "Guerra Fría", 
        "Revolución Francesa", "El Muro de Berlín", "Napoleón Bonaparte", 
        "Segunda Guerra Mundial", "Los Mayas", "Vikingos", "Edad Media", 
        "Renacimiento", "Juana de Arco", "Mahatma Gandhi", "Leonardo da Vinci", 
        "El Titanic", "Los Reyes Católicos", "La Peste Negra", "Julio César", 
        "La llegada a la Luna", "Antigua Grecia", "Samuráis", "Caballeros Templarios",
        "La Revolución Industrial", "Cleopatra", "Atila el Huno", "El Lejano Oeste"
    ],
    "🌟 Famosos": [
        "Ibai Llanos", "Rosalía", "Shakira", "Mr Beast", "Bad Bunny",
        "Taylor Swift", "Georgina Rodríguez", "Auronplay", "TheGrefg",
        "Zendaya", "Tom Holland", "Rauw Alejandro", "Donald Trump",
        "Elon Musk", "Kim Kardashian", "Quevedo", "Bizarrap", "Will Smith",
        "C. Tangana", "Belén Esteban", "David Broncano", "IlloJuan", "Kanye West",
        "Justin Bieber", "Lady Gaga", "Marta Díaz", "Plex", "Mariano Rajoy"
    ],
    "🎬 Series y Cine": [
        "La Casa de Papel", "Juego de Tronos", "Harry Potter", "Star Wars",
        "Stranger Things", "Titanic", "Marvel", "El Rey León", "Avatar",
        "Batman", "Spiderman", "Élite", "The Last of Us", "Disney World",
        "Netflix", "Piratas del Caribe", "Shrek", "Sherlock Holmes", 
        "Los Juegos del Hambre", "Toy Story", "Parásitos", "Barbie (película)",
        "Oppenheimer", "Breaking Bad", "The Office", "Los Simpson", "Jurassic Park"
    ],
    "🥘 Comida": [
        "Pizza", "Hamburguesa", "Sushi", "Paella", "Tortilla de patatas",
        "Croquetas", "Tacos", "Kebab", "Pasta Carbonara", "Ramen",
        "Salmorejo", "Chuletón", "Tarta de Queso", "Donuts", "Bravas",
        "Jamón Ibérico", "Palomitas", "Nutella", "Cerveza", "Filipinos",
        "Brócoli", "Aguacate", "Huevo frito", "Arroz con cosas", "Tiramisú",
        "Air Fryer", "Comida de la abuela", "Un buffet libre", "Macarrones"
    ],
    "✈️ Lugares y Viajes": [
        "Madrid", "Barcelona", "París", "Nueva York", "Londres", "Roma",
        "Tokio", "Ibiza", "La Playa", "Egipto", "Route 66", "Un Gimnasio", 
        "Una Discoteca", "El Supermercado", "Un Aeropuerto", "La Universidad", 
        "El Cine", "Un Hospital", "Un Parque de Atracciones", "El Infierno", 
        "La Luna", "Benidorm", "Islandia", "Machu Picchu", "La Gran Muralla China",
        "Un crucero", "Un hostal de mochileros", "Camping en la montaña"
    ],
    "📱 Tecnología y Redes": [
        "TikTok", "Instagram", "WhatsApp", "Twitter / X", "ChatGPT",
        "iPhone", "PlayStation 5", "YouTube", "Influencer", "Hacker",
        "Google", "Amazon", "Wifi", "Batería baja", "Selfie", "Inteligencia Artificial",
        "Realidad Virtual", "Un podcast", "Notificaciones", "Modo Avión", 
        "El algoritmo", "Bizum", "Spotify Wrapped", "Vinted"
    ],
    "🛋️ Cosas de la Vida": [
        "Llegar tarde", "La resaca", "Quedarse sin papel en el baño",
        "Hacerse un selfie", "El grupo de WhatsApp de la familia",
        "Ligar en una discoteca", "El primer día de gimnasio",
        "Un examen sin haber estudiado", "Ir al dentista",
        "Hacer un Bizum", "El olor a coche nuevo",
        "Un grupo de turistas perdidos", "La cuenta de la cena",
        "Stalkear a tu ex", "Dormir la siesta", "El mando a distancia",
        "Ese amigo que nunca tiene batería", "Pedir un Glovo",
        "Intentar no reírse en un sitio serio", "El lunes por la mañana",
        "Hacer la compra con hambre", "Perder las llaves", "Hacer la maleta"
    ]
}
# ------------------------------------------------------------------


# --- LÓGICA DE ESTADOS DEL JUEGO ---
if 'game_state' not in st.session_state:
    st.session_state.game_state = "setup"

st.title("INFILTRADO")

# =========================================
# PANTALLA 1: CONFIGURACIÓN (SETUP)
# =========================================
if st.session_state.game_state == "setup":
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    tema = st.selectbox("📚 SELECCIONA TEMÁTICA", list(DATOS.keys()))
    
    st.write("") # Espaciador
    
    c1, c2 = st.columns(2)
    with c1:
        jugadores = st.number_input("👥 JUGADORES", min_value=3, max_value=20, value=4)
    with c2:
        max_impostores = max(1, jugadores - 2)
        impostores = st.number_input("🕵️ IMPOSTORES", min_value=1, max_value=max_impostores, value=1)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 COMENZAR PARTIDA"):
        if not DATOS[tema]: # Protección si la categoría está vacía
            st.error("¡Esa categoría no tiene palabras!")
            st.stop()
            
        palabra = random.choice(DATOS[tema])
        # Crear lista de True (impostor) y False (inocente)
        lista_roles_bool = [False] * jugadores
        indices_impostores = random.sample(range(jugadores), impostores)
        for idx in indices_impostores:
            lista_roles_bool[idx] = True
            
        # Guardar todo en la memoria del juego
        st.session_state.roles_bool = lista_roles_bool
        st.session_state.palabra_secreta = palabra
        st.session_state.turno_actual = 0
        st.session_state.total_jugadores = jugadores
        st.session_state.game_state = "playing_hidden"
        st.rerun()

# =========================================
# PANTALLA 2: TURNO OCULTO (Pasar el móvil)
# =========================================
elif st.session_state.game_state == "playing_hidden":
    turno = st.session_state.turno_actual
    st.markdown(f"""
    <div class="setup-card" style="text-align: center;">
        <h2>➡️ Turno del Jugador {turno + 1}</h2>
        <p style="color: #8b949e;">Pasad el dispositivo. Asegúrate de que nadie más mire.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("👁️ MOSTRAR MI ROL"):
        st.session_state.game_state = "playing_revealed"
        st.rerun()

# =========================================
# PANTALLA 3: ROL REVELADO
# =========================================
elif st.session_state.game_state == "playing_revealed":
    turno = st.session_state.turno_actual
    es_impostor = st.session_state.roles_bool[turno]
    
    if es_impostor:
        contenido = """
        <span style="font-size: 40px;">🕵️</span><br>
        <span style="color: #f85149; font-weight: 800;">ERES EL INFILTRADO</span><br>
        <span style="font-size: 18px; color: #8b949e;">No sabes la palabra. ¡Miente!</span>
        """
    else:
        contenido = f"""
        <span style="font-size: 18px; color: #8b949e;">La palabra clave es:</span><br>
        <span style="font-size: 36px; color: #7C3AED; font-weight: 800;">{st.session_state.palabra_secreta.upper()}</span>
        """
        
    st.markdown(f'<div class="role-card">{contenido}</div>', unsafe_allow_html=True)
    st.warning("Memorízalo rápido. Pulsa el botón para ocultarlo antes de pasar el móvil.")
    
    # Lógica del botón siguiente
    es_ultimo_jugador = turno >= st.session_state.total_jugadores - 1
    texto_boton = "🗳️ IR A LA VOTACIÓN FINAL" if es_ultimo_jugador else "🔒 OCULTAR Y SIGUIENTE JUGADOR"
    
    if st.button(texto_boton):
        if es_ultimo_jugador:
            st.session_state.game_state = "voting"
        else:
            st.session_state.turno_actual += 1
            st.session_state.game_state = "playing_hidden"
        st.rerun()

# =========================================
# PANTALLA 4: VOTACIÓN
# =========================================
elif st.session_state.game_state == "voting":
    st.title("🗣️ DEBATE Y VOTACIÓN")
    st.markdown('<div class="setup-card"><p>Debatid y pulsad sobre el jugador que creéis que es el infiltrado para comprobarlo.</p></div>', unsafe_allow_html=True)
    
    # Generamos un botón por cada jugador
    for i in range(st.session_state.total_jugadores):
        # Usamos un estilo diferente (outline) para los botones de votación
        if st.button(f"👉 Acusar al Jugador {i + 1}", key=f"voto_{i}"):
            st.session_state.jugador_acusado = i
            st.session_state.game_state = "result"
            st.rerun()

# =========================================
# PANTALLA 5: RESULTADO FINAL
# =========================================
elif st.session_state.game_state == "result":
    acusado_idx = st.session_state.jugador_acusado
    era_impostor = st.session_state.roles_bool[acusado_idx]
    
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    
    if era_impostor:
        st.markdown('<div class="winner-text">🎉 ¡INOCENTES GANAN! 🎉</div>', unsafe_allow_html=True)
        st.write(f"¡Correcto! El Jugador {acusado_idx + 1} era un infiltrado.")
        st.balloons()
    else:
        st.markdown('<div class="loser-text">💀 ¡INFILTRADOS GANAN! 💀</div>', unsafe_allow_html=True)
        st.write(f"¡Habéis fallado! El Jugador {acusado_idx + 1} era inocente.")
        st.write("Los infiltrados se han salido con la suya.")
    
    # Mostrar la palabra secreta y quiénes eran los impostores
    st.markdown(f"""
    <div class="word-reveal">
        La palabra secreta era: <b>{st.session_state.palabra_secreta}</b>
    </div>
    """, unsafe_allow_html=True)
    
    lista_impostores_txt = []
    for idx, es_imp in enumerate(st.session_state.roles_bool):
        if es_imp:
            lista_impostores_txt.append(f"Jugador {idx+1}")
            
    st.write(f"\nLos infiltrados eran: {', '.join(lista_impostores_txt)}")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 JUGAR OTRA VEZ"):
        # Reseteamos variables clave
        for key in ['roles_bool', 'palabra_secreta', 'turno_actual', 'jugador_acusado']:
            del st.session_state[key]
        st.session_state.game_state = "setup"
        st.rerun()