import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA ---
# Pega aquí tu URL de la imagen si la tienes
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"

st.set_page_config(page_title="Infiltrado", page_icon=URL_LOGO, layout="centered")

# --- CSS V6.0: ESTILO PREMIUM + MEJORAS VISUALES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;900&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif !important; }
    .stApp { background-color: #F3F4F6; color: #1F2937; }

    h1 {
        font-weight: 900 !important; text-transform: uppercase; letter-spacing: -1px;
        background: linear-gradient(90deg, #4F46E5, #9333EA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 2px 10px rgba(147, 51, 234, 0.3); padding-bottom: 10px;
    }
    h2, h3 { font-weight: 700 !important; color: #374151 !important; }

    .card-style {
        background-color: white; padding: 25px; border-radius: 24px;
        box-shadow: 0 10px 40px -10px rgba(0,0,0,0.08); border: 1px solid #E5E7EB;
        margin-bottom: 20px; text-align: center;
    }

    .stButton>button {
        width: 100%; border-radius: 50px !important; height: 3.8em;
        background: linear-gradient(90deg, #4F46E5, #7C3AED); color: white;
        font-weight: 700; border: none; font-size: 18px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4); transition: 0.2s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(124, 58, 237, 0.6); }
    
    /* Botón de votar a alguien específico (más suave) */
    .vote-btn > button {
        background: white !important; color: #4F46E5 !important;
        border: 2px solid #4F46E5 !important;
        box-shadow: none !important;
    }
    .vote-btn > button:hover { background: #EEF2FF !important; }

    /* ESTILOS CARTA (Flip) */
    .flip-card { background-color: transparent; width: 100%; height: 320px; perspective: 1000px; margin-bottom: 20px; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }
    .flipped { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back {
      position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden;
      border-radius: 24px; display: flex; flex-direction: column; justify-content: center; align-items: center;
      padding: 20px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.15);
    }
    .flip-card-front { background: linear-gradient(135deg, #4F46E5, #7C3AED); color: white; }
    .flip-card-back { background-color: white; color: #1F2937; transform: rotateY(180deg); border: 4px solid #F3F4F6; }
    
    .status-eliminated { color: #EF4444; font-weight: bold; text-decoration: line-through; }
    </style>
    """, unsafe_allow_html=True)

# --- TUS DATOS ---
DATOS = {
    "⚽ Fútbol": [
        # TUS DATOS ORIGINALES
        "Real Madrid", "FC Barcelona", "Champions League", "Copa del Mundo",
        "Leo Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Balón de Oro",
        "El Clásico", "Boca Juniors", "Manchester City", "La Liga",
        "Estadio Santiago Bernabéu", "Camp Nou", "Tarjeta Roja", "VAR",
        "Fuera de Juego", "Bota de Oro", "Erling Haaland", "Vinícius Jr",
        "Selección Española", "Inter Miami", "Luis de la Fuente", "Mundial 2030",
        "Árbitro", "Jabulani", "Maradona", "Zidane", "Barça de Guardiola",
        "La chilena de Cristiano", "Iker Casillas", "Xavi e Iniesta", "El Chiringuito",
        "Kings League", "Un Linier", "Tirar un penalti", 
        # NUEVOS AÑADIDOS
        "Atlético de Madrid", "Cholo Simeone", "Florentino Pérez", "Joan Laporta",
        "Neymar Jr", "Pelé", "Johan Cruyff", "Mundial de Sudáfrica 2010",
        "Gol de Iniesta", "Sergio Ramos", "Lamine Yamal", "Copa América",
        "Eurocopa", "Anfield", "River Plate", "La Libertadores",
        "Saque de esquina", "Gol en propia puerta", "Tanda de penaltis", "El Bicho",
        "Hala Madrid", "Visca el Barça", "Luis Rubiales", "Fútbol Femenino",
        "Alexia Putellas", "Aitana Bonmatí", "Balón de Oro", "Ley del Ex",
        "Hacer una rabona", "Tirar a lo Panenka", "Un espontáneo", "El césped",
        "Vestuario", "Rueda de prensa", "Fichaje millonario", "Cláusula de rescisión",
        "Mourinho", "Pep Guardiola", "La Masía", "La Fábrica"
    ],
    "🏀 Deportes": [
        # TUS DATOS ORIGINALES
        "Baloncesto", "Tenis", "Fórmula 1", "MotoGP", "Pádel", "NBA",
        "Boxeo", "Natación", "Ciclismo", "Golf", "Rugby", "Carlos Alcaraz",
        "Fernando Alonso", "Rafa Nadal", "Marc Márquez", "Juegos Olímpicos",
        "Gimnasio", "Crossfit", "Maratón", "Surf", "Lamine Yamal", "Pau Gasol",
        "Tour de Francia", "Wimbledon", "Super Bowl", "Esquí", "Escalada",
        "Ajedrez", "Yoga", "La 33 de Alonso", "Lanzamiento de jabalina",
        # NUEVOS AÑADIDOS
        "Michael Jordan", "LeBron James", "Kobe Bryant", "Usain Bolt",
        "Simone Biles", "Serena Williams", "Roland Garros", "Copa Davis",
        "Lewis Hamilton", "Max Verstappen", "Valentino Rossi", "Dakar",
        "UFC", "Ilia Topuria", "Conor McGregor", "Mike Tyson",
        "Karate", "Judo", "Ping Pong", "Bádminton", "Voleibol",
        "Waterpolo", "Halterofilia", "Triatlón", "Ironman",
        "Senderismo", "Skateboarding", "Snowboard", "Curling", "Petanca",
        "Dardos", "Billar", "Bolos", "Hoyo en uno", "Triple",
        "Mate", "Touchdown", "Pit Stop", "Bandera a cuadros", "Medalla de Oro"
    ],
    "📜 Historia": [
        # TUS DATOS ORIGINALES
        "Pirámides de Egipto", "Imperio Romano", "Cristóbal Colón", "Guerra Fría",
        "Revolución Francesa", "El Muro de Berlín", "Napoleón Bonaparte",
        "Segunda Guerra Mundial", "Los Mayas", "Vikingos", "Edad Media",
        "Renacimiento", "Juana de Arco", "Mahatma Gandhi", "Leonardo da Vinci",
        "El Titanic", "Los Reyes Católicos", "La Peste Negra", "Julio César",
        "La llegada a la Luna", "Antigua Grecia", "Samuráis", "Caballeros Templarios",
        "La Revolución Industrial", "Cleopatra", "Atila el Huno", "El Lejano Oeste",
        # NUEVOS AÑADIDOS
        "Guerra Civil Española", "Franquismo", "La Transición", "Constitución de 1812",
        "Albert Einstein", "Marie Curie", "Isaac Newton", "Charles Darwin",
        "Mozart", "Beethoven", "Elvis Presley", "Marilyn Monroe",
        "Adolf Hitler", "Winston Churchill", "Nelson Mandela", "Martin Luther King",
        "La URSS", "Chernóbil", "Las Cruzadas", "Inquisición Española",
        "Descubrimiento de América", "Revolución Rusa", "Caída de Roma",
        "Los Aztecas", "Los Incas", "Machu Picchu", "Coliseo Romano",
        "Torre Eiffel", "Estatua de la Libertad", "11-S", "Pandemia COVID-19",
        "La Pinta, la Niña y la Santa María", "Gladiadores", "Faraones", "La Biblia",
        "Imprenta", "Internet", "Teléfono", "Máquina de vapor"
    ],
    "🌟 Famosos": [
        # TUS DATOS ORIGINALES
        "Ibai Llanos", "Rosalía", "Shakira", "Mr Beast", "Bad Bunny",
        "Taylor Swift", "Georgina Rodríguez", "Auronplay", "TheGrefg",
        "Zendaya", "Tom Holland", "Rauw Alejandro", "Donald Trump",
        "Elon Musk", "Kim Kardashian", "Quevedo", "Bizarrap", "Will Smith",
        "C. Tangana", "Belén Esteban", "David Broncano", "IlloJuan", "Kanye West",
        "Justin Bieber", "Lady Gaga", "Marta Díaz", "Plex", "Mariano Rajoy",
        # NUEVOS AÑADIDOS
        "El Rubius", "DjMaRiiO", "Rivers", "Kings League", "Gerard Piqué",
        "Aitana", "Lola Índigo", "Omar Montes", "Melendi", "Estopa",
        "Duki", "Karol G", "Feid", "Peso Pluma", "Harry Styles",
        "Dua Lipa", "Beyoncé", "Rihanna", "Cristiano Ronaldo", "Messi",
        "Pedro Sánchez", "Rey Felipe VI", "Reina Letizia", "Princesa Leonor",
        "Pablo Motos", "El Hormiguero", "Ana Obregón", "Tamara Falcó",
        "Kiko Rivera", "Paquirrín", "Torrente", "Santiago Segura",
        "Antonio Banderas", "Penélope Cruz", "Javier Bardem", "Úrsula Corberó",
        "Ester Expósito", "Mario Casas", "Blanca Suárez", "Steve Jobs",
        "Mark Zuckerberg", "Jeff Bezos", "Bill Gates", "Papa Francisco"
    ],
    "🎬 Series y Cine": [
        # TUS DATOS ORIGINALES
        "La Casa de Papel", "Juego de Tronos", "Harry Potter", "Star Wars",
        "Stranger Things", "Titanic", "Marvel", "El Rey León", "Avatar",
        "Batman", "Spiderman", "Élite", "The Last of Us", "Disney World",
        "Netflix", "Piratas del Caribe", "Shrek", "Sherlock Holmes",
        "Los Juegos del Hambre", "Toy Story", "Parásitos", "Barbie (película)",
        "Oppenheimer", "Breaking Bad", "The Office", "Los Simpson", "Jurassic Park",
        # NUEVOS AÑADIDOS
        "El Padrino", "Pulp Fiction", "Matrix", "El Señor de los Anillos",
        "Indiana Jones", "Regreso al Futuro", "Forrest Gump", "Gladiator",
        "Interstellar", "Inception", "Joker", "Vengadores: Endgame",
        "Frozen", "Coco", "Encanto", "Buscando a Nemo", "Gru, mi villano favorito",
        "Minions", "Dragon Ball", "One Piece", "Naruto", "Pokémon",
        "El Juego del Calamar", "Black Mirror", "Peaky Blinders", "Vikingos",
        "Friends", "Aquí no hay quien viva", "La que se avecina", "Los Serrano",
        "Cuéntame cómo pasó", "Paquita Salas", "Vis a Vis", "Merlí",
        "Hermanos", "Telenovela turca", "Sálvame", "La Isla de las Tentaciones",
        "Operación Triunfo", "Supervivientes", "Masterchef", "First Dates"
    ],
    "🥘 Comida": [
        # TUS DATOS ORIGINALES
        "Pizza", "Hamburguesa", "Sushi", "Paella", "Tortilla de patatas",
        "Croquetas", "Tacos", "Kebab", "Pasta Carbonara", "Ramen",
        "Salmorejo", "Chuletón", "Tarta de Queso", "Donuts", "Bravas",
        "Jamón Ibérico", "Palomitas", "Nutella", "Cerveza", "Filipinos",
        "Brócoli", "Aguacate", "Huevo frito", "Arroz con cosas", "Tiramisú",
        "Air Fryer", "Comida de la abuela", "Un buffet libre", "Macarrones",
        # NUEVOS AÑADIDOS
        "Gazpacho", "Fabada Asturiana", "Cocido Madrileño", "Pulpo a la gallega",
        "Calamares a la romana", "Ensaladilla Rusa", "Bocadillo de calamares",
        "Churros con chocolate", "Torrijas", "Roscón de Reyes", "Turrón",
        "Polvorones", "Pan con tomate", "Aceite de Oliva", "Vino Tinto",
        "Sangría", "Tinto de Verano", "Clara con limón", "Café con leche",
        "Cola Cao", "Nesquik", "Kinder Bueno", "KitKat", "Oreo",
        "Helado de chocolate", "Crep", "Gofre", "Nachos con queso",
        "Burrito", "Quesadilla", "Fajitas", "Hot Dog", "Nuggets",
        "Patatas fritas", "Ketchup", "Mayonesa", "Alioli",
        "Mercadona", "Hacendado", "Glovo", "Uber Eats", "Telepizza"
    ],
    "✈️ Lugares y Viajes": [
        # TUS DATOS ORIGINALES
        "Madrid", "Barcelona", "París", "Nueva York", "Londres", "Roma",
        "Tokio", "Ibiza", "La Playa", "Egipto", "Route 66", "Un Gimnasio",
        "Una Discoteca", "El Supermercado", "Un Aeropuerto", "La Universidad",
        "El Cine", "Un Hospital", "Un Parque de Atracciones", "Costa Rica",
        "La Luna", "Benidorm", "Islandia", "Machu Picchu", "La Gran Muralla China",
        "Un crucero", "Un hostal de mochileros", "Camping en la montaña", "Jordania",
        "Canada", "Oslo", "Puerto Rico",
        # NUEVOS AÑADIDOS
        "Venecia", "Ámsterdam", "Berlín", "Dubái", "Las Vegas",
        "Los Ángeles", "Miami", "Caribe", "Cancún", "Punta Cana",
        "Maldivas", "Bali", "Tailandia", "Japón", "Australia",
        "Antártida", "Desierto del Sahara", "Selva Amazónica", "Niágara",
        "El Vaticano", "Museo del Louvre", "Museo del Prado", "Sagrada Familia",
        "Ikea", "Zara", "Primark", "Apple Store", "Gasolinera",
        "Estación de tren", "Metro de Madrid", "Un autobús", "Un taxi",
        "La casa de tus padres", "Un hotel de 5 estrellas", "Una casa rural",
        "La feria del pueblo", "Un concierto", "Un estadio de fútbol", "La cárcel",
        "El baño de una discoteca", "La cola del paro", "Hacienda"
    ],
    "📱 Tecnología y Redes": [
        # TUS DATOS ORIGINALES
        "TikTok", "Instagram", "WhatsApp", "Twitter / X", "ChatGPT",
        "iPhone", "PlayStation 5", "YouTube", "Influencer", "Hacker",
        "Google", "Amazon", "Wifi", "Batería baja", "Selfie", "Inteligencia Artificial",
        "Realidad Virtual", "Un podcast", "Notificaciones", "Modo Avión",
        "El algoritmo", "Bizum", "Spotify Wrapped", "Vinted", "Bluetooth",
        # NUEVOS AÑADIDOS
        "Tinder", "Bumble", "Grindr", "OnlyFans", "Twitch",
        "Discord", "Telegram", "Facebook", "LinkedIn", "Pinterest",
        "BeReal", "Snapchat", "Filtro de Instagram", "Trending Topic",
        "Hacerse viral", "Un meme", "Sticker de WhatsApp", "Audio de 5 minutos",
        "Visto azul", "Bloquear a alguien", "Stalkear", "Ghosting",
        "Match", "Swipe", "Crush", "Hater", "Troll",
        "Bot", "Spam", "Phishing", "Virus informático", "Pantallazo azul",
        "Reiniciar el router", "Cable HDMI", "Cargador del móvil", "Auriculares",
        "AirPods", "Nintendo Switch", "Xbox", "PC Gamer", "Teclado mecánico",
        "Ratón", "Monitor 4K", "Fibra óptica", "5G", "Modo Incógnito",
        "Historial de búsqueda", "Contraseña olvidada", "Verificación en dos pasos"
    ],
    "🛋️ Cosas de la Vida": [
        # TUS DATOS ORIGINALES
        "Llegar tarde", "La resaca", "Quedarse sin papel en el baño",
        "Hacerse un selfie", "El grupo de WhatsApp de la familia",
        "Ligar en una discoteca", "El primer día de gimnasio",
        "Un examen sin haber estudiado", "Ir al dentista",
        "Hacer un Bizum", "El olor a coche nuevo",
        "Un grupo de turistas perdidos", "La cuenta de la cena",
        "Stalkear a tu ex", "Dormir la siesta", "El mando a distancia",
        "Ese amigo que nunca tiene batería", "Pedir un Glovo",
        "Intentar no reírse en un sitio serio", "El lunes por la mañana",
        "Hacer la compra con hambre", "Perder las llaves", "Hacer la maleta",
        # NUEVOS AÑADIDOS
        "Pisar una pieza de Lego", "Darse con el dedo meñique del pie",
        "Se cae el internet", "Spoiler de tu serie favorita",
        "La declaración de la Renta", "Pasar la ITV", "Buscar aparcamiento",
        "El vecino ruidoso", "Llamada de spam a la siesta", "Olvidar el PIN de la tarjeta",
        "Encontrarse a un ex", "Mancharse de tomate la camisa blanca",
        "Perder el autobús por un segundo", "Que te toque la lotería",
        "Domingo de lluvia", "Hacer dieta", "Dejar de fumar",
        "Ir a Ikea el sábado", "Montar un mueble y que sobren piezas",
        "Que se te queme la comida", "Pedir la cuenta y que no te miren",
        "Quedarse sin batería en el momento clave", "Romper la pantalla del móvil",
        "Perder un calcetín en la lavadora", "Sacar la basura",
        "Reunión de vecinos", "Cena de empresa", "Amigo invisible",
        "Boda, bautizo y comunión", "Operación bikini", "La cuesta de enero"
    ]
}

# --- LÓGICA DE ESTADOS ---
if 'game_state' not in st.session_state: st.session_state.game_state = "setup"
if 'eliminados' not in st.session_state: st.session_state.eliminados = []

# Cabecera
st.markdown(f"""
    <div style="text-align: center; padding-bottom: 10px;">
        <img src="{URL_LOGO}" style="width: 80px; border-radius: 20px; margin-bottom: 10px;">
        <h1>INFILTRADO</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# PANTALLA 1: SETUP
# =========================================
if st.session_state.game_state == "setup":
    st.markdown('<div class="card-style">', unsafe_allow_html=True)
    tema = st.selectbox("📚 SELECCIONA TEMÁTICA", list(DATOS.keys()))
    st.write("")
    c1, c2 = st.columns(2)
    with c1: jug = st.number_input("👥 JUGADORES", 3, 20, 4)
    with c2: imp = st.number_input("🕵️ IMPOSTORES", 1, max(1, jug-2), 1)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 COMENZAR PARTIDA"):
        st.session_state.roles_bool = [False] * jug
        indices_imp = random.sample(range(jug), imp)
        for idx in indices_imp: st.session_state.roles_bool[idx] = True
        
        st.session_state.palabra = random.choice(DATOS[tema])
        st.session_state.turno = 0
        st.session_state.total = jug
        st.session_state.eliminados = [] # Reseteamos eliminados
        st.session_state.game_state = "playing"
        st.session_state.card_flipped = False
        st.rerun()

# =========================================
# PANTALLA 2: JUEGO (CARTAS)
# =========================================
elif st.session_state.game_state == "playing":
    turno = st.session_state.turno
    
    st.markdown(f'<h3 style="text-align: center;">Turno del Jugador {turno + 1}</h3>', unsafe_allow_html=True)

    # Contenido reverso (HTML limpio)
    if st.session_state.roles_bool[turno]:
        contenido = """<div style="text-align: center;">
            <span style="font-size: 50px;">🤫</span><br>
            <h2 style="color: #EF4444;">ERES EL INFILTRADO</h2>
            <p>No sabes la palabra. ¡Disimula!</p></div>"""
    else:
        contenido = f"""<div style="text-align: center;">
            <p style="color: #6B7280;">La palabra clave es:</p>
            <h1>{st.session_state.palabra.upper()}</h1></div>"""

    flip_cls = "flipped" if st.session_state.get('card_flipped', False) else ""
    
    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner {flip_cls}">
        <div class="flip-card-front">
            <span style="font-size: 50px;">🃏</span>
            <h2>TU ROL</h2><p>Toca para revelar</p>
        </div>
        <div class="flip-card-back">{contenido}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.get('card_flipped'):
        if st.button("👁️ VER MI ROL"):
            st.session_state.card_flipped = True
            st.rerun()
    else:
        es_ultimo = turno >= st.session_state.total - 1
        txt = "🗳️ IR A VOTACIÓN" if es_ultimo else "🔒 OCULTAR Y SIGUIENTE"
        if st.button(txt):
            if es_ultimo: st.session_state.game_state = "voting_round"
            else: 
                st.session_state.turno += 1
                st.session_state.card_flipped = False
            st.rerun()

# =========================================
# PANTALLA 3: VOTACIÓN (BUCLE)
# =========================================
elif st.session_state.game_state == "voting_round":
    st.markdown('<div class="card-style"><h3>🗣️ R O N D A &nbsp; D E &nbsp; V O T A C I Ó N</h3><p>Debatid y expulsad a un jugador.</p></div>', unsafe_allow_html=True)
    
    # Mostramos botones solo para los vivos
    for i in range(st.session_state.total):
        if i not in st.session_state.eliminados:
            # Usamos un truco de CSS para botones secundarios
            st.markdown('<div class="vote-btn">', unsafe_allow_html=True)
            if st.button(f"👉 Expulsar al Jugador {i+1}", key=f"vote_{i}"):
                st.session_state.ultimo_expulsado = i
                st.session_state.eliminados.append(i)
                st.session_state.game_state = "round_result"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
             st.markdown(f'<div style="text-align:center; padding: 10px; color: #9CA3AF;">💀 Jugador {i+1} (Eliminado)</div>', unsafe_allow_html=True)

# =========================================
# PANTALLA 4: RESULTADO DE LA RONDA
# =========================================
elif st.session_state.game_state == "round_result":
    expulsado = st.session_state.ultimo_expulsado
    es_impostor = st.session_state.roles_bool[expulsado]
    
    # LÓGICA DE VICTORIA
    total_impostores = sum(st.session_state.roles_bool)
    impostores_vivos = sum(1 for i in range(st.session_state.total) if st.session_state.roles_bool[i] and i not in st.session_state.eliminados)
    inocentes_vivos = sum(1 for i in range(st.session_state.total) if not st.session_state.roles_bool[i] and i not in st.session_state.eliminados)