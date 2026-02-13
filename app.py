import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA ---
# Pega aquí el link que has copiado de GitHub
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"
st.set_page_config(
    page_title="Infiltrado",
    page_icon=URL_LOGO, # Esto pone el logo en la pestaña del navegador
    layout="centered"
)

# --- ICONO PARA EL MÓVIL (PWA) ---
st.markdown(f"""
    <head>
        <link rel="apple-touch-icon" href="{URL_LOGO}">
        <meta name="apple-mobile-web-app-title" content="Infiltrado">
        <meta name="apple-mobile-web-app-capable" content="yes">
    </head>
    """, unsafe_allow_html=True)

# --- CSS V4.0: DISEÑO LUMINOSO Y EFECTO FLIP CARD ---
st.markdown("""
    <style>
    /* Importamos una fuente moderna y limpia */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    /* --- ESTRUCTURA LUMINOSA --- */
    .stApp {
        background-color: #F8FAFC; /* Blanco roto luminoso */
        color: #1E293B; /* Azul oscuro casi negro para el texto */
        font-family: 'Poppins', sans-serif !important;
    }

    h1, h2, h3 {
        color: #334155 !important;
        text-align: center;
    }
    
    h1 {
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(to right, #4F46E5, #7C3AED); /* Degradado Azul-Violeta */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* --- TARJETAS LIMPIAS --- */
    .setup-card, .result-card, .flip-container {
        background-color: #FFFFFF; /* Blanco puro */
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #E2E8F0; /* Borde gris muy suave */
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); /* Sombra sutil y elegante */
        margin-bottom: 20px;
    }

    /* --- BOTONES MODERNOS --- */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #4F46E5; /* Azul vibrante */
        color: white;
        font-weight: 700;
        border: none;
        font-size: 18px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #4338CA;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }

    /* --- 🔥 EFECTO FLIP CARD (LA MAGIA) 🔥 --- */
    .flip-card {
      background-color: transparent;
      width: 100%;
      height: 300px; /* Altura de la carta */
      perspective: 1000px; /* Necesario para el efecto 3D */
      margin-bottom: 20px;
    }

    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.8s; /* Duración del giro */
      transform-style: preserve-3d;
    }

    /* Esta clase se activa con Python para girar la carta */
    .flipped {
      transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden; /* Oculta la cara de atrás */
      backface-visibility: hidden;
      border-radius: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 20px;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
    }

    .flip-card-front {
      background: linear-gradient(135deg, #4F46E5, #7C3AED); /* Frente azul-violeta */
      color: white;
    }

    .flip-card-back {
      background-color: #FFFFFF; /* Reverso blanco */
      color: #1E293B;
      transform: rotateY(180deg); /* El reverso empieza girado */
      border: 2px solid #4F46E5;
    }
    
    /* --- TEXTOS DE RESULTADO --- */
    .winner-text { color: #10B981; font-size: 2rem; font-weight: 800; text-align: center; }
    .loser-text { color: #EF4444; font-size: 2rem; font-weight: 800; text-align: center; }

    </style>
    """, unsafe_allow_html=True)

# --- TUS DATOS (¡IMPORTANTE! PEGA TU LISTA GIGANTE AQUÍ) ---
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
        "El Cine", "Un Hospital", "Un Parque de Atracciones", "Costa Rica",
        "La Luna", "Benidorm", "Islandia", "Machu Picchu", "La Gran Muralla China",
        "Un crucero", "Un hostal de mochileros", "Camping en la montaña", "Jordania",
        "Canada", "Oslo", "Puerto Rico"

    ],
    "📱 Tecnología y Redes": [
        "TikTok", "Instagram", "WhatsApp", "Twitter / X", "ChatGPT",
        "iPhone", "PlayStation 5", "YouTube", "Influencer", "Hacker",
        "Google", "Amazon", "Wifi", "Batería baja", "Selfie", "Inteligencia Artificial",
        "Realidad Virtual", "Un podcast", "Notificaciones", "Modo Avión",
        "El algoritmo", "Bizum", "Spotify Wrapped", "Vinted", "Bluetooth",
        ""
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

# --- LÓGICA DEL JUEGO ---
if 'game_state' not in st.session_state:
    st.session_state.game_state = "setup"
if 'card_flipped' not in st.session_state:
    st.session_state.card_flipped = False

st.markdown("<h1>INFILTRADO</h1>", unsafe_allow_html=True)

# =========================================
# PANTALLA 1: CONFIGURACIÓN (SETUP)
# =========================================
if st.session_state.game_state == "setup":
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    st.subheader("Configura la Partida")
    tema = st.selectbox("📚 SELECCIONA TEMÁTICA", list(DATOS.keys()))
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        jugadores = st.number_input("👥 JUGADORES", min_value=3, max_value=20, value=4)
    with c2:
        max_impostores = max(1, jugadores - 2)
        impostores = st.number_input("🕵️ IMPOSTORES", min_value=1, max_value=max_impostores, value=1)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 COMENZAR PARTIDA"):
        if not DATOS[tema]:
            st.error("¡Categoría vacía!")
            st.stop()
        palabra = random.choice(DATOS[tema])
        lista_roles_bool = [False] * jugadores
        indices_impostores = random.sample(range(jugadores), impostores)
        for idx in indices_impostores: lista_roles_bool[idx] = True
            
        st.session_state.roles_bool = lista_roles_bool
        st.session_state.palabra_secreta = palabra
        st.session_state.turno_actual = 0
        st.session_state.total_jugadores = jugadores
        st.session_state.game_state = "playing"
        st.session_state.card_flipped = False
        st.rerun()

# =========================================
# PANTALLA 2: TURNO Y CARTA (EL NÚCLEO)
# =========================================
elif st.session_state.game_state == "playing":
    turno = st.session_state.turno_actual
    es_impostor = st.session_state.roles_bool[turno]
    
    st.markdown(f'<h2 style="margin-bottom: 20px;">Turno del Jugador {turno + 1}</h2>', unsafe_allow_html=True)

    # --- CONTENIDO DEL REVERSO DE LA CARTA ---
    if es_impostor:
        contenido_reverso = """
        <span style="font-size: 60px;">🤫</span><br>
        <h2 style="color: #EF4444; margin: 10px 0;">ERES EL INFILTRADO</h2>
        <p>No sabes la palabra. ¡Miente!</p>
        """
    else:
        contenido_reverso = f"""
        <p style="font-size: 18px; color: #64748B;">La palabra clave es:</p>
        <h1 style="font-size: 40px; margin: 10px 0;">{st.session_state.palabra_secreta.upper()}</h1>
        <span style="font-size: 40px;">🧐</span>
        """

    # --- LÓGICA DE LA CARTA GIRATORIA ---
    # Si card_flipped es True, añadimos la clase "flipped" para que rote
    flip_class = "flipped" if st.session_state.card_flipped else ""

    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner {flip_class}">
        <div class="flip-card-front">
          <span style="font-size: 60px;">🃏</span>
          <h2 style="color: white;">TU CARTA DE ROL</h2>
          <p>Pulsa el botón para revelarla</p>
        </div>
        <div class="flip-card-back">
          {contenido_reverso}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- BOTÓN DE ACCIÓN ---
    es_ultimo_jugador = turno >= st.session_state.total_jugadores - 1
    
    if not st.session_state.card_flipped:
        # Botón para girar la carta
        if st.button("👁️ VER MI ROL (GIRAR CARTA)"):
            st.session_state.card_flipped = True
            st.rerun()
    else:
        # Botón para pasar al siguiente turno/votación
        texto_boton = "🗳️ IR A LA VOTACIÓN FINAL" if es_ultimo_jugador else "🔒 OCULTAR Y SIGUIENTE JUGADOR"
        if st.button(texto_boton):
            if es_ultimo_jugador:
                st.session_state.game_state = "voting"
            else:
                st.session_state.turno_actual += 1
                st.session_state.card_flipped = False # Reseteamos la carta para el siguiente
            st.rerun()

# =========================================
# PANTALLA 3: VOTACIÓN (Estilo Luminoso)
# =========================================
elif st.session_state.game_state == "voting":
    st.markdown("<h2>🗣️ DEBATE Y VOTACIÓN</h2>", unsafe_allow_html=True)
    st.markdown('<div class="setup-card"><p style="text-align: center;">Debatid y pulsad sobre el jugador que creéis que es el infiltrado.</p></div>', unsafe_allow_html=True)
    
    for i in range(st.session_state.total_jugadores):
        if st.button(f"👉 Acusar al Jugador {i + 1}", key=f"voto_{i}"):
            st.session_state.jugador_acusado = i
            st.session_state.game_state = "result"
            st.rerun()

# =========================================
# PANTALLA 4: RESULTADO FINAL (Estilo Luminoso)
# =========================================
elif st.session_state.game_state == "result":
    acusado_idx = st.session_state.jugador_acusado
    era_impostor = st.session_state.roles_bool[acusado_idx]
    
    st.markdown('<div class="result-card" style="text-align: center;">', unsafe_allow_html=True)
    if era_impostor:
        st.markdown('<div class="winner-text">🎉 ¡INOCENTES GANAN! 🎉</div>', unsafe_allow_html=True)
        st.write(f"¡Correcto! El Jugador {acusado_idx + 1} era un infiltrado.")
        st.balloons()
    else:
        st.markdown('<div class="loser-text">💀 ¡INFILTRADOS GANAN! 💀</div>', unsafe_allow_html=True)
        st.write(f"¡Habéis fallado! El Jugador {acusado_idx + 1} era inocente.")
    
    st.write("---")
    st.subheader(f"Palabra: {st.session_state.palabra_secreta}")
    lista_imps = [f"J.{i+1}" for i, es in enumerate(st.session_state.roles_bool) if es]
    st.write(f"Infiltrados: {', '.join(lista_imps)}")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 JUGAR OTRA VEZ"):
        for key in ['roles_bool', 'palabra_secreta', 'turno_actual', 'jugador_acusado', 'card_flipped']:
            del st.session_state[key]
        st.session_state.game_state = "setup"
        st.rerun()