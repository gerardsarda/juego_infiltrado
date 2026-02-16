import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA ---
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"
st.set_page_config(page_title="Infiltrado", page_icon=URL_LOGO, layout="centered")

# --- 💰 TU NEGOCIO (CONFIGURACIÓN) ---
# 👇👇👇 ¡PEGA AQUÍ TU ENLACE DE STRIPE! 👇👇👇
STRIPE_LINK = "https://buy.stripe.com/PON_AQUI_TU_LINK_REAL" 
CLAVE_MAESTRA = "IMP-VIP-99" # La palabra que el usuario recibe al pagar

# --- 🎨 CSS AGRESIVO (FORZADO DE FUENTE) ---
st.markdown(f"""
    <style>
    /* 1. IMPORTAMOS LA FUENTE 'FREDOKA' (ESTILO JUEGO) */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;600;700&display=swap');
    
    /* 2. REGLAS MAESTRAS PARA FORZAR LA FUENTE */
    html, body, .stApp {{
        font-family: 'Fredoka', sans-serif !important;
        background: radial-gradient(circle at 50% 0%, #4c1d95 0%, #1e1b4b 60%, #000000 100%);
        color: white;
    }}

    /* TÍTULOS */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Fredoka', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        color: white !important;
    }}
    
    h1 {{
        font-size: 3.5rem !important;
        text-shadow: 4px 4px 0px #4c1d95;
        margin-bottom: 10px !important;
        text-align: center;
    }}

    /* TEXTOS Y ETIQUETAS */
    p, label, span, div {{
        font-family: 'Fredoka', sans-serif !important;
    }}
    
    label {{
        font-size: 18px !important;
        color: #a78bfa !important; /* Color lila claro para etiquetas */
        font-weight: 600 !important;
    }}

    /* 3. FORZAR FUENTE EN LOS INPUTS (LO QUE FALLABA ANTES) */
    /* Selectores y Cajas de Texto */
    div[data-baseweb="select"], div[data-baseweb="base-input"], input {{
        font-family: 'Fredoka', sans-serif !important;
        font-size: 18px !important;
    }}
    
    /* Fondo de los inputs */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
        background-color: rgba(255,255,255,0.1) !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        border-radius: 15px !important;
        color: white !important;
    }}

    /* 4. BOTONES DIVERTIDOS */
    .stButton>button {{
        font-family: 'Fredoka', sans-serif !important;
        width: 100%;
        border-radius: 20px !important;
        height: 60px;
        background: #ec4899;
        border: none;
        border-bottom: 6px solid #be185d;
        color: white;
        font-weight: 700 !important;
        font-size: 22px !important;
        text-transform: uppercase;
        transition: all 0.1s;
    }}
    
    .stButton>button:hover {{
        transform: translateY(2px);
        border-bottom-width: 4px;
        filter: brightness(1.1);
    }}
    
    .stButton>button:active {{
        transform: translateY(6px);
        border-bottom-width: 0px;
    }}

    /* 5. TARJETAS PERSONALIZADAS */
    .game-card {{
        background: rgba(255, 255, 255, 0.08);
        border: 3px solid rgba(255, 255, 255, 0.15);
        border-radius: 30px;
        padding: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        text-align: center;
    }}

    /* 6. ICONO 3D (Showcase) */
    .icon-showcase {{
        background: linear-gradient(180deg, #8b5cf6 0%, #6d28d9 100%);
        border-radius: 25px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 8px 0px #4c1d95;
        border: 2px solid rgba(255,255,255,0.2);
        position: relative;
    }}
    
    .floating-icon {{
        font-size: 80px;
        filter: drop-shadow(0 5px 0px rgba(0,0,0,0.2));
        animation: bounce 2s infinite;
        display: inline-block;
    }}
    
    @keyframes bounce {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    /* 7. ETIQUETAS DE ESTADO */
    .vip-tag {{ background: #fbbf24; color: #78350f; padding: 5px 12px; border-radius: 12px; font-weight: 700; font-size: 14px; display: inline-block; border-bottom: 3px solid #b45309; }}
    .free-tag {{ background: #34d399; color: #064e3b; padding: 5px 12px; border-radius: 12px; font-weight: 700; font-size: 14px; display: inline-block; border-bottom: 3px solid #065f46; }}

    /* 8. JUEGO DE CARTAS */
    .flip-card {{ background-color: transparent; width: 100%; height: 420px; perspective: 1000px; margin-bottom: 20px; }}
    .flip-card-inner {{ position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }}
    .flipped {{ transform: rotateY(180deg); }}
    .flip-card-front, .flip-card-back {{ 
        position: absolute; width: 100%; height: 100%; 
        -webkit-backface-visibility: hidden; backface-visibility: hidden; 
        border-radius: 30px; display: flex; flex-direction: column; 
        justify-content: center; align-items: center; padding: 20px; 
        box-shadow: 0 15px 0px rgba(0,0,0,0.3);
        border: 4px solid rgba(255,255,255,0.2);
    }}
    .flip-card-front {{ background: linear-gradient(180deg, #6366f1, #4338ca); }}
    .flip-card-back {{ background: #1e1b4b; transform: rotateY(180deg); border: 4px solid #6366f1; }}

    /* OCULTAR ELEMENTOS MOLESTOS DE STREAMLIT */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    </style>
    """, unsafe_allow_html=True)
    
# --- 📦 DATOS: BASE DE DATOS EXTENSA (V. TITÁNICA) ---

# =========================================
# 1. LISTAS GRATUITAS (GIGANTES PERO "FAMILY FRIENDLY")
# =========================================
lista_animales = [
    "Perro", "Gato", "Elefante", "León", "Delfín", "Hormiga", "Jirafa", "Vaca", "Cerdo", 
    "Gallina", "Koala", "Pingüino", "Tiburón", "Águila", "Canguro", "Panda", "Murciélago", 
    "Serpiente", "Cocodrilo", "Gorila", "Lobo", "Oso", "Zorro", "Camello", "Hipopótamo", 
    "Ornitorrinco", "Capibara", "Medusa", "Pulpo", "Avestruz", "Loro", "Hámster", "Tigre", 
    "Ballena", "Rinoceronte", "Cebra", "Ardilla", "Rata", "Mosquito", "Abeja", "Mariposa", 
    "Camaleón", "Perezoso", "Nutria", "Suricata", "Búho", "Flamenco", "Mapache", "Erizo",
    "Lemur", "Pavo Real", "Hiena", "Guepardo", "Topo", "Castor", "Cisne", "Buitre",
    "Escorpión", "Araña", "Calamar", "Estrella de mar", "Caballito de mar", "Narval",
    "Beluga", "Manatí", "Komodo", "Iguana", "Salamandra", "Rana", "Sapo", "Tarántula",
    "Avispa", "Libélula", "Grillo", "Saltamontes", "Mariquita", "Escarabajo", "Ciervo",
    "Alce", "Bisonte", "Jabalí", "Lince", "Puma", "Jaguar", "Leopardo", "Pantera",
    "Oso Polar", "Foca", "Morsa", "León Marino", "Pelícano", "Gaviota", "Paloma",
    "Cuervo", "Colibrí", "Tucán", "Cacatúa", "Canario", "Periquito", "Tortuga", "Caracol"
]

lista_casa = [
    "Mesa", "Silla", "Cama", "Lámpara", "Nevera", "Sofá", "Espejo", "Ventana", "Puerta", 
    "Televisión", "Microondas", "Lavadora", "Ducha", "Inodoro", "Almohada", "Sartén", 
    "Cuchillo", "Reloj", "Maceta", "Ordenador", "Secador", "Toalla", "Llaves", 
    "Mando a distancia", "Papel higiénico", "Cepillo de dientes", "Fregona", "Escoba", 
    "Alfombra", "Cuadro", "Estantería", "Armario", "Percha", "Plancha", "Tostadora", 
    "Cafetera", "Exprimidor", "Batidora", "Horno", "Lavavajillas", "Grifo", "Enchufe", 
    "Interruptor", "Bombilla", "Manta", "Sábana", "Colchón", "Edredón", "Cojín",
    "Mesita de noche", "Despertador", "Radiador", "Aire acondicionado", "Ventilador",
    "Cortina", "Persiana", "Felpudo", "Timbre", "Buzón", "Cubo de basura", "Bolsa de basura",
    "Estropajo", "Bayeta", "Detergente", "Suavizante", "Pinzas", "Tendedero", "Plato",
    "Vaso", "Copa", "Tenedor", "Cuchara", "Cucharilla", "Servilleta", "Mantel",
    "Tupper", "Abrelatas", "Sacacorchos", "Rallador", "Colador", "Olla", "Cazuela",
    "Vitrocerámica", "Campana extractora", "Frutero", "Salero", "Azucarero", "Esponja",
    "Champú", "Gel", "Jabón de manos", "Peine", "Maquillaje", "Cortauñas", "Báscula"
]

lista_colores = [
    "Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco", "Rosa", "Lila", "Naranja", 
    "Gris", "Marrón", "Turquesa", "Dorado", "Plateado", "Beige", "Violeta", "Círculo", 
    "Cuadrado", "Triángulo", "Rectángulo", "Estrella", "Corazón", "Rombo", "Pentágono", 
    "Línea recta", "Curva", "Hexágono", "Óvalo", "Cilindro", "Cubo", "Esfera", "Pirámide",
    "Cono", "Trapecio", "Espiral", "Zigzag", "Punto", "Raya", "Ajedrez", "Transparente",
    "Multicolor", "Arcoíris", "Granate", "Azul Marino", "Verde Lima", "Fucsia", "Coral",
    "Mostaza", "Caqui", "Salmón", "Índigo", "Cian", "Magenta", "Ocre", "Vainilla",
    "Chocolate", "Carbón", "Hueso", "Crema", "Lavanda", "Menta", "Pistacho"
]

lista_profesiones = [
    "Médico", "Profesor", "Policía", "Bombero", "Cocinero", "Futbolista", "Peluquero", 
    "Astronauta", "Mecánico", "Abogado", "Youtuber", "Camarero", "Jardinero", "Dentista", 
    "Piloto", "Pintor", "Detective", "Enfermero", "Carpintero", "Electricista", "Fontanero", 
    "Veterinario", "Arquitecto", "Juez", "Cantante", "Actor", "Escritor", "Científico", 
    "Programador", "Influencer", "Político", "Taxista", "Busero", "Farmacéutico",
    "Panadero", "Carnicero", "Pescadero", "Frutero", "Cajero", "Reponedor", "Repartidor",
    "Cartero", "Periodista", "Fotógrafo", "Diseñador", "Modelo", "Bailarín", "Músico",
    "DJ", "Director de cine", "Guionista", "Traductor", "Bibliotecario", "Arqueólogo",
    "Psicólogo", "Psiquiatra", "Cirujano", "Pediatra", "Entrenador", "Árbitro",
    "Socorrista", "Militar", "Espía", "Ladrón", "Payaso", "Mago", "Sacerdote", "Monja",
    "Albañil", "Soldador", "Minero", "Pescador", "Agricultor", "Ganadero", "Azafata/o",
    "Recepcionista", "Secretario", "Contable", "Director de banco", "Empresario"
]

# --- CREACIÓN AUTOMÁTICA DEL MIX GRATIS ---
lista_tutifruti = lista_animales + lista_casa + lista_colores + lista_profesiones

# DICCIONARIO FINAL GRATIS
DATOS_FREE = {
    "🎲 TUTIFRUTI (Mix Gratis)": lista_tutifruti, 
    "🐶 Animales (Gratis)": lista_animales,
    "🏠 Objetos de Casa (Gratis)": lista_casa,
    "🎨 Colores y Formas (Gratis)": lista_colores,
    "👔 Profesiones (Gratis)": lista_profesiones
}

# =========================================
# 2. LISTAS VIP (DE PAGO Y MASIVAS)
# =========================================
DATOS_VIP = {
    "😈 MODO CANALLA (+18) [VIP]": [
        # EL COMBO MORTAL: SALSEO + FIESTA + ALCOHOL
        "Tu ex", "Ser infiel", "Un trío", "OnlyFans", "Tinder", "Ligar borracho", 
        "Nudismo", "Calabazas", "Amigo con derecho", "Striptease", "Resaca moral",
        "Sexo en público", "Juguetes eróticos", "Mensaje a las 4am", "Walk of Shame",
        "Besar a un desconocido", "Mentir en el CV", "Robar en una tienda", 
        "Dormir sin ropa interior", "Grindr", "Mandar nudes", "Bodycount", 
        "Fetiches raros", "Sugar Daddy", "Roleplay", "Kamasutra", "Una orgía",
        "El baño de la discoteca", "Hacerse un test de embarazo", "Stalkear a tu ex",
        "Fantasmada sexual", "Primera cita", "Despedida de soltero", "Gatillazo",
        "Friends with benefits", "Hacer la cobra", "Pagafantas", "Zona de amigos (Friendzone)",
        "Resaca", "Chupito", "Jagger", "Vomitar", "Perrear", "Discoteca",
        "Portero de discoteca", "VIP", "Barra libre", "Garrafón", "DJ",
        "Cerrar el bar", "Kebab de madrugada", "Perder el móvil", "Laguna mental",
        "Copas", "Cerveza", "Botellón", "La policía", "After", "Karaoke",
        "Tequila", "Gin Tonic", "Cerveza caliente", "El conductor sobrio",
        "Irse sin pagar (Simpa)", "Dormir en la calle", "Perder la chaqueta",
        "Llamar a tu ex borracho", "Churros de madrugada", "El bus de vuelta",
        "Fumar cachimba", "El segurata", "Perder la dignidad", "Ligar con el/la camarero/a",
        "Borrachera triste", "Borrachera alegre", "Pelea de bar", "Colarse en la cola",
        "Perder a tus amigos", "Acabar en otra ciudad", "Dormir en el sofá", "Pizza fría",
        "Ibuprofeno", "Agua con gas", "Juramento de no volver a beber", "Domingo de resaca",
        "Coma etílico", "Ron con Cola", "Whisky", "Vodka", "Absenta", "Chupito de fuego",
        "Juegos de beber", "Beer Pong", "Yo nunca", "Verdad o Reto", "Botella",
        "Besar a un amigo/a", "Confesión vergonzosa", "Baile sexy", "Quitarse la camiseta",
        "Hacer el gusano", "Cantar a gritos", "Llorar en el baño", "Pedir matrimonio borracho",
        "Tatuaje del que te arrepientes", "Tangas", "Calzoncillos de la suerte", "Condones", "Lubricante", "Esposas",
        "Látigo", "Antifaz", "Chocolate en el cuerpo", "Hielo", "Masaje con final feliz",
        "Cena romántica", "Motel de carretera", "Coche", "Playa de noche", "Ascensor",
        "Probador de ropa", "Cine", "Parque", "Piscina"
    ],

    "⚽ Fútbol [VIP]": [
        "Real Madrid", "FC Barcelona", "Champions League", "Copa del Mundo",
        "Leo Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Balón de Oro",
        "El Clásico", "Boca Juniors", "Manchester City", "La Liga",
        "Estadio Santiago Bernabéu", "Camp Nou", "Tarjeta Roja", "VAR",
        "Fuera de Juego", "Bota de Oro", "Selección Española", "Inter Miami", 
        "Luis de la Fuente", "Mundial 2030", "Árbitro", "Jabulani", "Barça de Guardiola",
        "La chilena de Cristiano", "El Chiringuito", "Kings League", "Atlético de Madrid", 
        "Cholo Simeone", "Florentino Pérez", "Joan Laporta", "Neymar Jr", "Pelé", 
        "Johan Cruyff", "Mundial de Sudáfrica 2010", "Gol de Iniesta",
        "Lamine Yamal", "Copa América", "Eurocopa", "Anfield", "River Plate", 
        "La Libertadores", "Saque de esquina", "Gol en propia puerta", "Tanda de penaltis", 
        "Luis Rubiales", "Fútbol Femenino","Alexia Putellas", "Aitana Bonmatí",
        "Hacer una rabona", "Tirar a lo Panenka", "Rueda de prensa", "Fichaje millonario", 
        "Cláusula de rescisión", "Mourinho", "Pep Guardiola", "La Masía", "La Fábrica",
        "Tiki Taka", "Autobús defensivo", "Wanda Metropolitano", "San Mamés", "Mestalla",
        "Brasil", "Old Trafford", "Allianz Arena", "Parque de los Príncipes",
        "Wembley", "Maracaná", "Bombonera", "Monumental", "Balón de Oro",
        "Manita", "Ruud Gullit", "Ryan Cherki", "Iñigo Martínez",
        "Alfredo Di Stéfano", "Johan Cruyff", "Zinedine Zidane", "Ronaldo Nazario", "Ronaldinho", "Franz Beckenbauer",
        "Michel Platini", "Gerd Müller", "Bobby Charlton", "George Best", "Lev Yashin",
        "Paolo Maldini", "Marco van Basten", "Eusébio", "Ferenc Puskás", "Garrincha",
        "Kylian Mbappé", "Erling Haaland", "Vinícius Jr", "Jude Bellingham", "Rodri Hernández",
        "Lamine Yamal", "Robert Lewandowski", "Harry Kane", "Kevin De Bruyne", "Mohamed Salah",
        "Neymar Jr", "Luka Modric", "Toni Kroos", "Antoine Griezmann", "Bernardo Silva",
        "Virgil van Dijk", "Bruno Fernandes", "Lautaro Martínez", "Julián Álvarez", "Phil Foden",
        "Jamal Musiala", "Florian Wirtz", "Bukayo Saka", "Cole Palmer", "Endrick",
        "Iker Casillas", "Xavi Hernández", "Andrés Iniesta", "Sergio Ramos", "Carles Puyol",
        "Gerard Piqué", "Sergio Busquets", "Xabi Alonso", "David Villa", "Fernando Torres",
        "Raúl González", "Emilio Butragueño", "Pep Guardiola", "Luis Enrique", "Fernando Hierro",
        "Cesc Fàbregas", "David Silva", "Santi Cazorla", "Jesús Navas", "Dani Carvajal",
        "Jordi Alba", "Nico Williams", "Dani Olmo", "Pedri", "Gavi",
        "Thierry Henry", "David Beckham", "Zlatan Ibrahimovic", "Wayne Rooney", "Kaká",
        "Roberto Carlos", "Cafú", "Dani Alves", "Marcelo", "Luis Figo",
        "Rivaldo", "Romário", "Samuel Eto'o", "Didier Drogba", "Frank Lampard",
        "Steven Gerrard", "Paul Scholes", "Andrea Pirlo", "Francesco Totti", "Alessandro Del Piero",
        "Gianluigi Buffon", "Oliver Kahn", "Fabio Cannavaro", "Carles Puyol", "Gareth Bale",
        "Thibaut Courtois", "Marc-André ter Stegen", "Jan Oblak", "Dibu Martínez", "Manuel Neuer",
        "Alisson Becker", "Ederson", "Keylor Navas", "Unai Simón", "David de Gea",
        "Pepe", "Ruben Dias", "Antonio Rüdiger", "Achraf Hakimi", "Alphonso Davies",
        "Luis Suárez", "Karim Benzema", "Harry Maguire", "Mario Balotelli", "Paul Pogba",
        "Eden Hazard", "James Rodríguez", "Radamel Falcao", "Arturo Vidal", "Alexis Sánchez",
        "Chicharito Hernández", "Joaquín Sánchez", "Arda Güler", "Vitor Roque"
    ],

    "🏅 Otros Deportes [VIP]": [
        "Baloncesto", "Tenis", "Fórmula 1", "MotoGP", "Pádel", "NBA",
        "Boxeo", "Natación", "Ciclismo", "Golf", "Rugby", "Carlos Alcaraz",
        "Fernando Alonso", "Rafa Nadal", "Marc Márquez", "Juegos Olímpicos",
        "Gimnasio", "Crossfit", "Maratón", "Surf", "Pau Gasol",
        "Tour de Francia", "Wimbledon", "Super Bowl", "La 33", "Michael Jordan",
        "LeBron James", "Kobe Bryant", "Usain Bolt", "Simone Biles", 
        "Lewis Hamilton", "Max Verstappen", "UFC", "Ilia Topuria", "McGregor",
        "Novak Djokovic", "Roger Federer", "Serena Williams", "Roland Garros",
        "Open de Australia", "US Open", "Copa Davis", "Anillo de la NBA", "Triple",
        "Mate", "Tapón", "Alley-oop", "Bocina", "Tiempo muerto", "Prórroga",
        "Touchdown", "Quarterback", "Haka", "Melé", "Ensayo", "Hoyo en uno",
        "Green", "Swing", "Caddie", "Tiger Woods", "Jon Rahm", "Indurain",
        "Contador", "Pogacar", "Vingegaard", "Maillot Amarillo", "Giro de Italia",
        "Vuelta a España", "Dakar", "Carlos Sainz", "Valentino Rossi", "Jorge Lorenzo",
        "Dani Pedrosa", "Ángel Nieto", "Pit Stop", "Safety Car", "Bandera a cuadros",
        "Pole Position", "Adelantamiento", "DRS", "Red Bull", "Ferrari", "Mercedes",
        "Aston Martin", "McLaren", "Ring de boxeo", "KO", "Gancho", "Uppercut",
        "Cinturón de campeón", "Mike Tyson", "Muhammad Ali", "Canelo", "Mayweather",
        "Judo", "Karate", "Taekwondo", "Cinturón Negro", "Tatami", "Kimono",
        "Piscina olímpica", "Michael Phelps", "Mireia Belmonte", "Waterpolo",
        "Sincronizada", "Salto de trampolín", "Bádminton", "Carolina Marín",
        "Ping Pong", "Voleibol", "Balonmano", "Petanca", "Curling", "Skate",
        "Snowboard", "Esquí", "Escalada", "Senderismo", "Triatlón", "Ironman"
    ],

    "🌟 Famosos, Youtubers y Memes [VIP]": [
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
        "Mark Zuckerberg", "Jeff Bezos", "Bill Gates", "Papa Francisco",
        "Fernando Alonso", "Carlos Alcaraz", "Isabel Pantoja", "Julio Iglesias",
        "Raphael", "Rocío Jurado", "Lola Flores", "Alaska", "Mario Vaquerizo",
        "Bertín Osborne", "Jorge Javier Vázquez", "Paz Padilla", "Chicote",
        "Arguiñano", "Dabiz Muñoz", "Cristina Pedroche", "Pilar Rubio",
        "Sergio Ramos", "Joaquín el del Betis", "Iniesta", "Casillas",
        "Puyol", "Xavi", "Villa", "Torres", "Raúl", "Guti", "Beckham",
        "Victoria Beckham", "Spice Girls", "Backstreet Boys", "One Direction",
        "BTS", "Blackpink", "Coldplay", "Imagine Dragons", "Queen", "Freddie Mercury",
        "Michael Jackson", "Madonna", "Britney Spears", "Jennifer Lopez",
        "Pitbull", "Enrique Iglesias", "Ricky Martin", "Chayanne", "Luis Miguel"
    ],

    "🎬 Cine y Series [VIP]": [
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
        "Operación Triunfo", "Supervivientes", "Masterchef", "First Dates",
        "Física o Química", "El Internado", "Oliver y Benji", "Doraemon",
        "Shin Chan", "Bob Esponja", "Patrulla Canina", "Peppa Pig", "Bluey",
        "Mickey Mouse", "Pato Donald", "Goofy", "Pluto", "Cenicienta",
        "Blancanieves", "La Sirenita", "La Bella y la Bestia", "Aladdin",
        "Mulan", "Pocahontas", "Tarzán", "Hércules", "101 Dálmatas",
        "Dumbo", "Bambi", "Pinocho", "Peter Pan", "Alicia en el País de las Maravillas",
        "Mary Poppins", "Pesadilla antes de Navidad", "Eduardo Manostijeras",
        "Charlie y la Fábrica de Chocolate", "Matilda", "Solo en Casa",
        "Grease", "Dirty Dancing", "Pretty Woman", "Notting Hill", "Love Actually"
    ],

    "🥘 Comida Rica [VIP]": [
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
        "Mercadona", "Hacendado", "Glovo", "Uber Eats", "Telepizza",
        "Domino's Pizza", "Burger King", "McDonald's", "KFC", "Subway",
        "Starbucks", "Dunkin Donuts", "Five Guys", "Goiko Grill", "Vips",
        "100 Montaditos", "La Tagliatella", "Fosters Hollywood", "Ginos",
        "Rodilla", "Telechino", "Pollo asado", "Costillas barbacoa", "Alitas de pollo",
        "Aros de cebolla", "Tequeños", "Empanadillas", "Gyozas", "Edamame",
        "Sashimi", "Makis", "Nigiris", "Wasabi", "Jengibre", "Soja",
        "Palillos chinos", "Tenedor libre", "Wok", "Buffet de desayuno"
    ],

    "✈️ Viajes y Lugares [VIP]": [
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
        "El baño de una discoteca", "La cola del paro", "Hacienda",
        "Marte", "Estación Espacial", "El Polo Norte", "El Triángulo de las Bermudas",
        "Atlantis", "Hogwarts", "Mordor", "Narnia", "Wakanda", "Gotham",
        "Springfield", "Bikini Bottom", "El País de Nunca Jamás", "El País de las Maravillas"
    ],
    
    "📱 Tecnología y Vida Moderna [VIP]": [
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
        "Historial de búsqueda", "Contraseña olvidada", "Verificación en dos pasos",
        "NFT", "Criptomoneda", "Bitcoin", "Metaverso", "Streaming", "Lag",
        "Bug", "Glitch", "Update", "Download", "Upload", "Nube", "Drive",
        "Dropbox", "WeTransfer", "PDF", "Word", "Excel", "PowerPoint"
    ]
}

TODOS_LOS_DATOS = {**DATOS_FREE, **DATOS_VIP}


# --- INICIALIZACIÓN ---
if 'game_state' not in st.session_state: st.session_state.game_state = "setup"
if 'eliminados' not in st.session_state: st.session_state.eliminados = []
if 'roles_bool' not in st.session_state: st.session_state.roles_bool = []
if 'total' not in st.session_state: st.session_state.total = 4
if 'palabra' not in st.session_state: st.session_state.palabra = ""
if 'vip_unlocked' not in st.session_state: st.session_state.vip_unlocked = False

# =========================================
# PANTALLA 1: SETUP
# =========================================
if st.session_state.game_state == "setup":
    st.markdown(f"""
        <div class="hero-container">
            <img src="{URL_LOGO}" style="width: 100px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 15px;">
            <h1 class="hero-title">INFILTRADO</h1>
            <div style="color: #6B7280; font-weight: 600;">Versión 4.0 Premium</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    st.markdown('<h3>⚙️ Configuración</h3>', unsafe_allow_html=True)
    
    tema_seleccionado = st.selectbox("📚 Elige mazo de cartas", list(TODOS_LOS_DATOS.keys()))
    
    es_vip = tema_seleccionado in DATOS_VIP
    acceso_concedido = False
    
    if not es_vip:
        acceso_concedido = True
        st.success("✅ Categoría Gratuita seleccionada")
    else:
        if st.session_state.vip_unlocked:
            acceso_concedido = True
            st.success("🔓 ¡PACK VIP DESBLOQUEADO! A DISFRUTAR")
        else:
            st.markdown(f"""
            <div class="premium-lock">
                <div style="font-size: 50px;">👑</div>
                <h2 style="color: white; margin: 10px 0;">PACK PREMIUM</h2>
                <p style="color: #E5E7EB;">Has elegido <b>{tema_seleccionado}</b></p>
                <p style="font-size: 14px; margin-top: 10px;">Accede al <b>Modo Canalla</b> y todas las categorías VIP por solo 1€.</p>
            </div>
            """, unsafe_allow_html=True)
            
            c_pago1, c_pago2 = st.columns([2, 1])
            with c_pago1:
                clave = st.text_input("🔑 Introducir Clave VIP", placeholder="¿Ya la tienes?")
            with c_pago2:
                st.link_button("💳 Pagar 1€", STRIPE_LINK)
            
            if clave:
                if clave.upper() == CLAVE_MAESTRA:
                    st.session_state.vip_unlocked = True
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ Clave incorrecta.")

    if acceso_concedido:
        st.write("")
        c1, c2 = st.columns(2)
        with c1: jug = st.number_input("👥 Jugadores", 3, 20, 4)
        with c2: imp = st.number_input("🕵️ Infiltrados", 1, jug, 1) # Ahora el máximo es 'jug'
        
        st.write("")
        if st.button("🔥 GENERAR PARTIDA"):
            st.session_state.roles_bool = [False] * jug
            indices_imp = random.sample(range(jug), imp)
            for idx in indices_imp: st.session_state.roles_bool[idx] = True
            
            st.session_state.palabra = random.choice(TODOS_LOS_DATOS[tema_seleccionado])
            st.session_state.turno = 0
            st.session_state.total = jug
            st.session_state.eliminados = []
            st.session_state.game_state = "playing" 
            st.session_state.card_flipped = False
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# PANTALLA 2: TRANSICIÓN (STOP)
# =========================================
elif st.session_state.game_state == "transition":
    turno = st.session_state.turno
    st.markdown(f"""
    <div style="padding-top: 50px;"></div>
    <div class="stop-card">
        <div style="font-size: 80px;">🛑</div>
        <h2 style="color: white; margin: 20px 0;">¡ALTO AHÍ!</h2>
        <p style="color: #9CA3AF;">Pasa el dispositivo al siguiente.</p>
        <hr style="border-color: #374151; margin: 30px 0;">
        <h1 style="color: #F87171; font-size: 3rem; margin: 0;">JUGADOR {turno + 1}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"✅ SOY EL JUGADOR {turno + 1}"):
        st.session_state.game_state = "playing"
        st.rerun()

# =========================================
# PANTALLA 3: JUEGO (CARTAS)
# =========================================
elif st.session_state.game_state == "playing":
    turno = st.session_state.turno
    progreso = (turno + 1) / st.session_state.total
    st.progress(progreso)
    st.markdown(f'<p style="text-align:center; color:#6B7280; font-size: 14px;">Jugador {turno + 1} de {st.session_state.total}</p>', unsafe_allow_html=True)

    if st.session_state.roles_bool[turno]:
        contenido = """<div style="text-align: center;">
            <span style="font-size: 60px;">🤫</span><br>
            <h2 style="color: #EF4444; margin-top: 10px;">ERES EL INFILTRADO</h2>
            <div style="background: #FEF2F2; padding: 10px; border-radius: 10px; margin-top: 15px; color: #B91C1C; font-size: 14px;">
            ⚠️ Miente. No conoces la palabra.
            </div></div>"""
    else:
        contenido = f"""<div style="text-align: center;">
            <p style="color: #6B7280;">La palabra secreta es:</p>
            <h1 style="font-size: 42px; margin: 15px 0; color: #4F46E5;">{st.session_state.palabra.upper()}</h1>
            <span style="font-size: 40px;">🧐</span></div>"""

    flip_cls = "flipped" if st.session_state.get('card_flipped', False) else ""
    
    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner {flip_cls}">
        <div class="flip-card-front">
            <span style="font-size: 60px; margin-bottom: 20px;">🃏</span>
            <h2 style="color: white;">TU CARTA</h2><p>Toca para revelar</p>
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
        txt = "🗳️ IR A VOTACIONES" if es_ultimo else "🔒 OCULTAR Y SIGUIENTE"
        if st.button(txt):
            st.session_state.card_flipped = False
            if es_ultimo: st.session_state.game_state = "voting_round"
            else: 
                st.session_state.turno += 1
                st.session_state.game_state = "transition"
            st.rerun()

# =========================================
# PANTALLA 3.5: MOSTRAR QUIÉN EMPIEZA (NUEVA)
# =========================================
elif st.session_state.game_state == "show_starter":
    inicial = st.session_state.jugador_inicial
    st.markdown(f"""
    <div style="padding-top: 50px;"></div>
    <div class="starter-card">
        <div style="font-size: 60px;">🎲</div>
        <h2 style="color: white; margin: 20px 0;">¡ROLES REPARTIDOS!</h2>
        <p style="color: #E0E7FF; font-size: 18px;">Empieza hablando el:</p>
        <div style="background: white; color: #4F46E5; border-radius: 15px; padding: 20px; margin: 20px 0;">
            <h1 style="font-size: 3.5rem; margin: 0;">JUGADOR {inicial + 1}</h1>
        </div>
        <p style="color: #E0E7FF;">Hacedle la primera pregunta.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⏱️ EMPEZAR CRONÓMETRO DE DEBATE"):
        st.session_state.game_state = "voting_round"
        st.rerun()
# =========================================
# PANTALLA 4: VOTACIÓN
# =========================================
elif st.session_state.game_state == "voting_round":
    st.markdown('<div class="hero-container" style="margin-top: 0; padding: 20px;"><h2 class="hero-title" style="font-size: 2rem !important;">VOTACIÓN</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    for i in range(st.session_state.total):
        if i not in st.session_state.eliminados:
            st.markdown(f'<div style="margin-bottom: 10px;"><button style="width:100%; padding:15px; border-radius:12px; border:2px solid #4F46E5; background:white; color:#4F46E5; font-weight:bold; cursor:pointer;" onclick="document.getElementById(\'vote_{i}\').click()">👉 ACUSAR AL JUGADOR {i+1}</button></div>', unsafe_allow_html=True)
            if st.button(f"Confirmar Voto Jugador {i+1}", key=f"vote_{i}"):
                st.session_state.ultimo_expulsado = i
                st.session_state.eliminados.append(i)
                st.session_state.game_state = "round_result"
                st.rerun()
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
    
    if es_impostor:
        st.markdown(f"<h1 style='color: #10B981; font-size: 3rem;'>¡INFILTRADO! 😈</h1>", unsafe_allow_html=True)
        if impostores_vivos == 0:
            st.balloons()
            st.success("🎉 ¡VICTORIA DE LOS INOCENTES!")
            st.markdown(f"**La palabra era:** {st.session_state.palabra}")
            if st.button("🔄 JUGAR OTRA"):
                st.session_state.game_state = "setup"
                st.rerun()
            st.stop()
        else:
            st.info(f"Quedan {impostores_vivos} infiltrados...")
    else:
        st.markdown(f"<h1 style='color: #EF4444; font-size: 3rem;'>¡INOCENTE! 😱</h1>", unsafe_allow_html=True)
        if impostores_vivos >= inocentes_vivos:
            st.error("💀 ¡GANAN LOS INFILTRADOS!")
            st.markdown(f"**La palabra era:** {st.session_state.palabra}")
            if st.button("🔄 JUGAR OTRA"):
                st.session_state.game_state = "setup"
                st.rerun()
            st.stop()
        else:
            st.warning("Habéis fallado. Seguimos.")

    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("➡️ SEGUIR"):
        st.session_state.game_state = "voting_round"
        st.rerun()