import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA ---
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"
st.set_page_config(page_title="Infiltrado", page_icon=URL_LOGO, layout="centered")

# --- CSS SUPER-PREMIUM (V8.0) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;900&display=swap');
    
    /* FUENTES Y COLORES GENERALES */
    html, body, [class*="css"] {{ font-family: 'Montserrat', sans-serif !important; }}
    .stApp {{ 
        background-color: #F3F4F6; 
        background-image: radial-gradient(#E5E7EB 1px, transparent 1px);
        background-size: 20px 20px;
        color: #1F2937; 
    }}

    /* HEADER GIGANTE */
    .hero-container {{
        text-align: center;
        padding: 40px 20px;
        background: white;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-top: -60px; /* Sube para pegar al borde */
        margin-bottom: 30px;
        border-bottom: 3px solid #4F46E5;
    }}
    
    .hero-title {{
        font-weight: 900 !important; 
        text-transform: uppercase; 
        letter-spacing: -2px;
        font-size: 3.5rem !important;
        background: linear-gradient(90deg, #4F46E5, #9333EA);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin: 0;
    }}
    
    .hero-subtitle {{
        color: #6B7280;
        font-weight: 600;
        font-size: 1.1rem;
        margin-top: 10px;
    }}

    /* TARJETAS FLOTANTES */
    .setup-card {{
        background-color: white; 
        padding: 30px; 
        border-radius: 24px;
        box-shadow: 0 20px 40px -10px rgba(79, 70, 229, 0.1); 
        border: 1px solid #E5E7EB;
        margin-bottom: 20px;
    }}

    /* BOTONES */
    .stButton>button {{
        width: 100%; border-radius: 50px !important; height: 3.8em;
        background: linear-gradient(90deg, #4F46E5, #7C3AED); color: white;
        font-weight: 700; border: none; font-size: 18px;
        box-shadow: 0 10px 20px rgba(79, 70, 229, 0.3); 
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{ 
        transform: translateY(-3px) scale(1.02); 
        box-shadow: 0 15px 30px rgba(79, 70, 229, 0.5); 
    }}
    
    /* BOTÓN DE VOTO */
    .vote-btn > button {{
        background: white !important; color: #4F46E5 !important;
        border: 2px solid #4F46E5 !important; box-shadow: none !important; margin-bottom: 10px;
    }}
    .vote-btn > button:hover {{ background: #EEF2FF !important; transform: translateY(-2px); }}

    /* ESTILOS CARTA (Flip) */
    .flip-card {{ background-color: transparent; width: 100%; height: 340px; perspective: 1000px; margin-bottom: 20px; }}
    .flip-card-inner {{ position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }}
    .flipped {{ transform: rotateY(180deg); }}
    .flip-card-front, .flip-card-back {{
      position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden;
      border-radius: 24px; display: flex; flex-direction: column; justify-content: center; align-items: center;
      padding: 20px; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.15);
    }}
    .flip-card-front {{ background: linear-gradient(135deg, #4F46E5, #7C3AED); color: white; }}
    .flip-card-back {{ background-color: white; color: #1F2937; transform: rotateY(180deg); border: 4px solid #F3F4F6; }}
    
    /* PANTALLA DE STOP */
    .stop-card {{
        background-color: #111827; color: white; padding: 40px; border-radius: 24px;
        text-align: center; margin-bottom: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.4);
        border: 2px solid #374151;
    }}
    
    /* FOOTER */
    .footer {{
        text-align: center; color: #9CA3AF; font-size: 0.8rem; margin-top: 40px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- TU LISTA GIGANTE DE DATOS ---
DATOS = {
    "⚽ Fútbol": [
        "Real Madrid", "FC Barcelona", "Champions League", "Copa del Mundo",
        "Leo Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Balón de Oro",
        "El Clásico", "Boca Juniors", "Manchester City", "La Liga",
        "Estadio Santiago Bernabéu", "Camp Nou", "Tarjeta Roja", "VAR",
        "Fuera de Juego", "Bota de Oro", "Erling Haaland", "Vinícius Jr",
        "Selección Española", "Inter Miami", "Luis de la Fuente", "Mundial 2030",
        "Árbitro", "Jabulani", "Maradona", "Zidane", "Barça de Guardiola",
        "La chilena de Cristiano", "Iker Casillas", "Xavi", "Iniesta", "El Chiringuito",
        "Kings League", "Bajar de división", "Tirar un penalti", "Atlético de Madrid", 
        "Cholo Simeone", "Florentino Pérez", "Joan Laporta", "Neymar Jr", "Pelé", 
        "Johan Cruyff", "Mundial de Sudáfrica 2010", "Gol de Iniesta", "Sergio Ramos", 
        "Lamine Yamal", "Copa América", "Eurocopa", "Anfield", "River Plate", 
        "La Libertadores", "Saque de esquina", "Gol en propia puerta", "Tanda de penaltis", 
        "Julian Alvarez", "MLS", "Gareth Bale", "Luis Rubiales", "Fútbol Femenino", 
        "Alexia Putellas", "Aitana Bonmatí", "Balón de Oro", "Ley del Ex", 
        "Henry", "Tirar a lo Panenka", "Paolo Maldini", "Roberto Baggio", 
        "Vestuario", "Rueda de prensa", "Fichaje millonario", "Cláusula de rescisión", 
        "Mourinho", "Pep Guardiola", "La Masía", "Cole Palmer", "Bruno Fernandes", "Ruud Gullit",
        "Marco Van Basten", "Kubala", "Mundial 2002", "Mundial 2018", "Eurocopa", "Transfermarkt",
        "Radamel Falcao", "Ryan Cherki", "Marcos Llorente"
    ],
    "🏀 Deportes": [
        "Baloncesto", "Tenis", "Fórmula 1", "MotoGP", "Pádel", "NBA",
        "Boxeo", "Natación", "Ciclismo", "Golf", "Rugby", "Carlos Alcaraz",
        "Fernando Alonso", "Rafa Nadal", "Marc Márquez", "Juegos Olímpicos",
        "Gimnasio", "Crossfit", "Maratón", "Surf", "Lamine Yamal", "Pau Gasol",
        "Tour de Francia", "Wimbledon", "Super Bowl", "Esquí", "Escalada",
        "Ajedrez", "Yoga", "La 33 de Alonso", "Lanzamiento de jabalina",
        "Michael Jordan", "LeBron James", "Kobe Bryant", "Usain Bolt",
        "Simone Biles", "Serena Williams", "Roland Garros", "Copa Davis",
        "Lewis Hamilton", "Max Verstappen", "Valentino Rossi", "Dakar",
        "UFC", "Ilia Topuria", "Conor McGregor", "Mike Tyson", "Karate", 
        "Judo", "Ping Pong", "Bádminton", "Voleibol", "Waterpolo", "Halterofilia", 
        "Triatlón", "Ironman", "Senderismo", "Skateboarding", "Snowboard", 
        "Curling", "Petanca", "Dardos", "Billar", "Bolos", "Hoyo en uno", 
        "Triple", "Mate", "Touchdown", "Pit Stop", "Bandera a cuadros", "Medalla de Oro"
    ],
    "📜 Historia": [
        "Pirámides de Egipto", "Imperio Romano", "Cristóbal Colón", "Guerra Fría",
        "Revolución Francesa", "El Muro de Berlín", "Napoleón Bonaparte",
        "Segunda Guerra Mundial", "Los Mayas", "Vikingos", "Edad Media",
        "Renacimiento", "Juana de Arco", "Mahatma Gandhi", "Leonardo da Vinci",
        "El Titanic", "Los Reyes Católicos", "La Peste Negra", "Julio César",
        "La llegada a la Luna", "Antigua Grecia", "Samuráis", "Caballeros Templarios",
        "La Revolución Industrial", "Cleopatra", "Atila el Huno", "El Lejano Oeste",
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
        "Ibai Llanos", "Rosalía", "Shakira", "Mr Beast", "Bad Bunny",
        "Taylor Swift", "Georgina Rodríguez", "Auronplay", "TheGrefg",
        "Zendaya", "Tom Holland", "Rauw Alejandro", "Donald Trump",
        "Elon Musk", "Kim Kardashian", "Quevedo", "Bizarrap", "Will Smith",
        "C. Tangana", "Belén Esteban", "David Broncano", "IlloJuan", "Kanye West",
        "Justin Bieber", "Lady Gaga", "Marta Díaz", "Plex", "Mariano Rajoy",
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
        "La Casa de Papel", "Juego de Tronos", "Harry Potter", "Star Wars",
        "Stranger Things", "Titanic", "Marvel", "El Rey León", "Avatar",
        "Batman", "Spiderman", "Élite", "The Last of Us", "Disney World",
        "Netflix", "Piratas del Caribe", "Shrek", "Sherlock Holmes",
        "Los Juegos del Hambre", "Toy Story", "Parásitos", "Barbie (película)",
        "Oppenheimer", "Breaking Bad", "The Office", "Los Simpson", "Jurassic Park",
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
        "Pizza", "Hamburguesa", "Sushi", "Paella", "Tortilla de patatas",
        "Croquetas", "Tacos", "Kebab", "Pasta Carbonara", "Ramen",
        "Salmorejo", "Chuletón", "Tarta de Queso", "Donuts", "Bravas",
        "Jamón Ibérico", "Palomitas", "Nutella", "Cerveza", "Filipinos",
        "Brócoli", "Aguacate", "Huevo frito", "Arroz con cosas", "Tiramisú",
        "Air Fryer", "Comida de la abuela", "Un buffet libre", "Macarrones",
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
        "Madrid", "Barcelona", "París", "Nueva York", "Londres", "Roma",
        "Tokio", "Ibiza", "La Playa", "Egipto", "Route 66", "Un Gimnasio",
        "Una Discoteca", "El Supermercado", "Un Aeropuerto", "La Universidad",
        "El Cine", "Un Hospital", "Un Parque de Atracciones", "Costa Rica",
        "La Luna", "Benidorm", "Islandia", "Machu Picchu", "La Gran Muralla China",
        "Un crucero", "Un hostal de mochileros", "Camping en la montaña", "Jordania",
        "Canada", "Oslo", "Puerto Rico",
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
        "TikTok", "Instagram", "WhatsApp", "Twitter / X", "ChatGPT",
        "iPhone", "PlayStation 5", "YouTube", "Influencer", "Hacker",
        "Google", "Amazon", "Wifi", "Batería baja", "Selfie", "Inteligencia Artificial",
        "Realidad Virtual", "Un podcast", "Notificaciones", "Modo Avión",
        "El algoritmo", "Bizum", "Spotify Wrapped", "Vinted", "Bluetooth",
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

# --- INICIALIZACIÓN DE MEMORIA SEGURA ---
if 'game_state' not in st.session_state: st.session_state.game_state = "setup"
if 'eliminados' not in st.session_state: st.session_state.eliminados = []
if 'roles_bool' not in st.session_state: st.session_state.roles_bool = []
if 'total' not in st.session_state: st.session_state.total = 4
if 'palabra' not in st.session_state: st.session_state.palabra = ""

# =========================================
# PANTALLA 1: SETUP (DISEÑO MEJORADO)
# =========================================
if st.session_state.game_state == "setup":
    # 1. HEADER TIPO APP
    st.markdown(f"""
        <div class="hero-container">
            <img src="{URL_LOGO}" style="width: 100px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 15px;">
            <h1 class="hero-title">INFILTRADO</h1>
            <div class="hero-subtitle">Descubre al mentiroso antes de que sea tarde</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 2. INSTRUCCIONES DESPLEGABLES (LIMPIEZA)
    with st.expander("📜 ¿Cómo se juega? (Leer reglas)"):
        st.write("""
        1. **Pasad el móvil:** Cada jugador mira su rol en secreto.
        2. **La Palabra:** Todos ven la misma palabra menos el **Infiltrado**.
        3. **Debate:** Haced preguntas por turnos. El infiltrado debe disimular.
        4. **Votación:** Expulsad al sospechoso. Si echáis al Infiltrado, ¡Ganan los inocentes!
        """)

    # 3. TARJETA DE CONFIGURACIÓN
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: left; margin-bottom: 20px;">⚙️ Configuración</h3>', unsafe_allow_html=True)
    
    tema = st.selectbox("📚 Elige un mazo de palabras", list(DATOS.keys()))
    
    st.write("") # Espacio
    c1, c2 = st.columns(2)
    with c1: jug = st.number_input("👥 Jugadores", 3, 20, 4)
    with c2: imp = st.number_input("🕵️ Infiltrados", 1, max(1, jug-2), 1)
    
    st.write("") # Espacio
    if st.button("🔥 GENERAR NUEVA PARTIDA"):
        st.session_state.roles_bool = [False] * jug
        indices_imp = random.sample(range(jug), imp)
        for idx in indices_imp: st.session_state.roles_bool[idx] = True
        
        st.session_state.palabra = random.choice(DATOS[tema])
        st.session_state.turno = 0
        st.session_state.total = jug
        st.session_state.eliminados = []
        st.session_state.game_state = "playing" 
        st.session_state.card_flipped = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. FOOTER
    st.markdown('<div class="footer">v1.0 • Made with ❤️</div>', unsafe_allow_html=True)

# =========================================
# PANTALLA 2: PANTALLA DE BLOQUEO (TRANSICIÓN)
# =========================================
elif st.session_state.game_state == "transition":
    turno = st.session_state.turno
    st.markdown(f"""
    <div style="padding-top: 50px;"></div>
    <div class="stop-card">
        <div style="font-size: 80px;">🛑</div>
        <h2 style="color: white; margin: 20px 0;">¡ALTO AHÍ!</h2>
        <p style="color: #9CA3AF; font-size: 18px;">No mires la pantalla si no eres tú.</p>
        <hr style="border-color: #374151; margin: 30px 0;">
        <p style="color: white; font-weight: bold;">PASA EL MÓVIL AL:</p>
        <h1 style="color: #F87171; font-size: 3rem; margin: 0;">JUGADOR {turno + 1}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"✅ SOY EL JUGADOR {turno + 1}, VER ROL"):
        st.session_state.game_state = "playing"
        st.rerun()

# =========================================
# PANTALLA 3: JUEGO (CARTAS)
# =========================================
elif st.session_state.game_state == "playing":
    turno = st.session_state.turno
    
    # Barra de progreso visual
    progreso = (turno + 1) / st.session_state.total
    st.progress(progreso)
    st.markdown(f'<p style="text-align:center; color:#6B7280; font-size: 14px;">Jugador {turno + 1} de {st.session_state.total}</p>', unsafe_allow_html=True)

    if st.session_state.roles_bool[turno]:
        contenido = """<div style="text-align: center;">
            <span style="font-size: 60px;">🤫</span><br>
            <h2 style="color: #EF4444; margin-top: 10px;">ERES EL INFILTRADO</h2>
            <p style="font-size: 16px;">Tu misión: Engañar a todos.</p>
            <div style="background: #FEF2F2; padding: 10px; border-radius: 10px; margin-top: 15px; color: #B91C1C; font-size: 14px;">
            ⚠️ No conoces la palabra secreta. Escucha y miente.
            </div>
            </div>"""
    else:
        contenido = f"""<div style="text-align: center;">
            <p style="color: #6B7280; font-weight: 600;">La palabra secreta es:</p>
            <h1 style="font-size: 42px; margin: 15px 0; color: #4F46E5;">{st.session_state.palabra.upper()}</h1>
            <span style="font-size: 40px;">🧐</span>
            <p style="font-size: 14px; margin-top: 10px;">Encuentra al mentiroso.</p>
            </div>"""

    flip_cls = "flipped" if st.session_state.get('card_flipped', False) else ""
    
    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner {flip_cls}">
        <div class="flip-card-front">
            <span style="font-size: 60px; margin-bottom: 20px;">🃏</span>
            <h2 style="color: white;">TU CARTA DE ROL</h2>
            <p style="opacity: 0.9;">Toca el botón para girar</p>
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
        txt = "🗳️ IR A LAS VOTACIONES" if es_ultimo else "🔒 OCULTAR Y SIGUIENTE"
        
        if st.button(txt):
            st.session_state.card_flipped = False
            if es_ultimo: 
                st.session_state.game_state = "voting_round"
            else: 
                st.session_state.turno += 1
                st.session_state.game_state = "transition"
            st.rerun()

# =========================================
# PANTALLA 4: VOTACIÓN
# =========================================
elif st.session_state.game_state == "voting_round":
    st.markdown(f"""
    <div class="hero-container" style="margin-top: 0; padding: 20px;">
        <h2 class="hero-title" style="font-size: 2rem !important;">VOTACIÓN</h2>
        <p>¿Quién es el infiltrado?</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    for i in range(st.session_state.total):
        if i not in st.session_state.eliminados:
            st.markdown('<div class="vote-btn">', unsafe_allow_html=True)
            if st.button(f"👉 ACUSAR AL JUGADOR {i+1}", key=f"vote_{i}"):
                st.session_state.ultimo_expulsado = i
                st.session_state.eliminados.append(i)
                st.session_state.game_state = "round_result"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
             st.markdown(f'<div style="text-align:center; padding: 10px; color: #D1D5DB; text-decoration: line-through;">💀 Jugador {i+1} (Eliminado)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# PANTALLA 5: RESULTADO
# =========================================
elif st.session_state.game_state == "round_result":
    expulsado = st.session_state.ultimo_expulsado
    es_impostor = st.session_state.roles_bool[expulsado]
    
    impostores_vivos = sum(1 for i in range(st.session_state.total) if st.session_state.roles_bool[i] and i not in st.session_state.eliminados)
    inocentes_vivos = sum(1 for i in range(st.session_state.total) if not st.session_state.roles_bool[i] and i not in st.session_state.eliminados)
    
    st.markdown('<div class="setup-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #6B7280;'>El Jugador {expulsado + 1} era...</h3>", unsafe_allow_html=True)
    
    if es_impostor:
        st.markdown(f"<h1 style='color: #10B981; font-size: 3rem; margin: 20px 0;'>¡INFILTRADO! 😈</h1>", unsafe_allow_html=True)
        if impostores_vivos == 0:
            st.balloons()
            st.success("🎉 ¡VICTORIA DE LOS INOCENTES!")
            st.markdown(f"**La palabra era:** {st.session_state.palabra}")
            if st.button("🔄 JUGAR OTRA PARTIDA"):
                st.session_state.game_state = "setup"
                st.rerun()
            st.stop()
        else:
            st.info(f"¡Bien hecho! Pero quedan {impostores_vivos} infiltrados...")
    else:
        st.markdown(f"<h1 style='color: #EF4444; font-size: 3rem; margin: 20px 0;'>¡INOCENTE! 😱</h1>", unsafe_allow_html=True)
        if impostores_vivos >= inocentes_vivos:
            st.error("💀 ¡VICTORIA DE LOS INFILTRADOS!")
            st.markdown("Han conseguido la mayoría numérica.")
            st.markdown(f"**La palabra era:** {st.session_state.palabra}")
            if st.button("🔄 JUGAR OTRA PARTIDA"):
                st.session_state.game_state = "setup"
                st.rerun()
            st.stop()
        else:
            st.warning("Habéis expulsado a un inocente. La partida continúa.")

    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("➡️ SEGUIR JUGANDO"):
        st.session_state.game_state = "voting_round"
        st.rerun()