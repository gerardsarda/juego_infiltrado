import streamlit as st
import random

# --- CONFIGURACIÓN INICIAL ---
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"
st.set_page_config(page_title="Infiltrado", page_icon=URL_LOGO, layout="centered")

# --- 💰 TU NEGOCIO ---
STRIPE_LINK = "https://buy.stripe.com/PON_AQUI_TU_LINK_REAL"
CLAVE_MAESTRA = "IMP-VIP-99"

# --- 🎨 CSS DEFINITIVO (CONTRASTE REAL Y DISEÑO VIBRANT) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
    
    html, body, .stApp {{
        font-family: 'Montserrat', sans-serif !important;
        background: linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%);
        color: white !important;
    }}

    /* TÍTULO PRINCIPAL */
    h1 {{
        font-weight: 900 !important;
        text-transform: uppercase;
        font-size: 3.2rem !important;
        text-align: center;
        color: white !important;
        text-shadow: 0 5px 15px rgba(0,0,0,0.4);
        margin-bottom: 25px !important;
    }}

    /* INPUTS Y SELECTORES: FONDO BLANCO -> LETRA NEGRA */
    div[data-baseweb="input"], div[data-baseweb="select"] > div {{
        background-color: white !important;
        border-radius: 12px !important;
    }}
    
    input, .stSelectbox div[data-baseweb="select"] span {{
        color: black !important;
        -webkit-text-fill-color: black !important;
        font-weight: 800 !important;
    }}
    
    /* ICONOS DE LOS INPUTS */
    button[kind="secondary"], svg {{
        color: black !important;
        fill: black !important;
    }}

    /* TARJETA DE ROL: FONDO BLANCO -> LETRA NEGRA */
    .white-card {{
        background: white !important;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        min-height: 350px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 4px solid #a855f7;
    }}
    
    .white-card h1, .white-card h2, .white-card p, .white-card div {{
        color: black !important;
        text-shadow: none !important;
    }}

    .secret-word-box {{
        background: #f3f4f6;
        color: #4c1d95 !important;
        padding: 15px;
        border-radius: 12px;
        font-size: 2.5rem;
        font-weight: 900;
        margin: 15px 0;
        border: 1px solid #ddd;
    }}

    /* BOTONES ACCIÓN */
    .stButton>button {{
        width: 100%; border-radius: 16px !important; height: 62px;
        background: linear-gradient(90deg, #ec4899, #db2777);
        color: white !important; font-weight: 900 !important;
        text-transform: uppercase; border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- 📦 DATOS: BASE DE DATOS EXTENSA (V. TITÁNICA) ---

# 1. LISTAS GRATUITAS
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

lista_tutifruti = lista_animales + lista_casa + lista_colores + lista_profesiones

DATOS_FREE = {
    "🎲 TUTIFRUTI": lista_tutifruti, 
    "🐶 Animales": lista_animales,
    "🏠 Objetos de Casa": lista_casa,
    "🎨 Colores y Formas": lista_colores,
    "👔 Profesiones": lista_profesiones
}

# 2. LISTAS VIP
DATOS_VIP = {
    "😈 MODO CANALLA (+18) [VIP]": [
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

# --- LÓGICA DE ESTADOS ---
if 'game_state' not in st.session_state: st.session_state.game_state = "setup"
if 'eliminados' not in st.session_state: st.session_state.eliminados = []
if 'vip_unlocked' not in st.session_state: st.session_state.vip_unlocked = False

# PANTALLA 1: SETUP
if st.session_state.game_state == "setup":
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{URL_LOGO}" style="width: 200px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h1>INFILTRADO</h1>', unsafe_allow_html=True)
    st.markdown('<div style="background: rgba(0,0,0,0.2); padding: 25px; border-radius: 24px;">', unsafe_allow_html=True)
    
    tema_seleccionado = st.selectbox("MAZO DE CARTAS", list(TODOS_LOS_DATOS.keys()))
    
    # Bloque VIP
    acceso = True
    if "[VIP]" in tema_seleccionado and not st.session_state.vip_unlocked:
        acceso = False
        st.warning("🔒 CATEGORÍA VIP")
        c1, c2 = st.columns([2, 1])
        with c1: clave = st.text_input("CÓDIGO", placeholder="...")
        with c2: st.markdown(f'<a href="{STRIPE_LINK}" target="_blank"><button style="margin-top:28px; width:100%; height:42px; background:#fbbf24; color:black; font-weight:bold; border-radius:10px; border:none; cursor:pointer;">PAGAR</button></a>', unsafe_allow_html=True)
        if clave.upper() == CLAVE_MAESTRA:
            st.session_state.vip_unlocked = True
            st.rerun()

    if acceso:
        c1, c2 = st.columns(2)
        with c1: jug = st.number_input("JUGADORES", 3, 20, 4)
        with c2: imp = st.number_input("INFILTRADOS", 1, 2, 1)
        
        if st.button("INICIAR PARTIDA"):
            st.session_state.roles = [False] * jug
            for i in random.sample(range(jug), imp): st.session_state.roles[i] = True
            st.session_state.palabra = random.choice(TODOS_LOS_DATOS[tema_seleccionado])
            st.session_state.jugador_inicial = random.randint(1, jug)
            st.session_state.turno = 0
            st.session_state.total = jug
            st.session_state.eliminados = []
            st.session_state.flipped = False
            st.session_state.game_state = "playing"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA 2: TRANSICIÓN
elif st.session_state.game_state == "transition":
    st.markdown(f"""<div style="text-align: center; padding-top: 50px;">
        <div style="font-size: 80px; margin-bottom: 20px;">🛑</div>
        <h2>PASA EL MÓVIL AL:</h2>
        <h1 style="font-size: 4rem !important; color: white !important;">JUGADOR {st.session_state.turno + 1}</h1>
    </div>""", unsafe_allow_html=True)
    if st.button(f"SOY YO"):
        st.session_state.game_state = "playing"
        st.rerun()

# PANTALLA 3: REVELAR CARTA
elif st.session_state.game_state == "playing":
    if not st.session_state.flipped:
        st.markdown(f"""<div style="background: rgba(0,0,0,0.2); padding: 40px; border-radius: 24px; text-align: center; height: 400px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 100px;">🃏</div>
            <h2>JUGADOR {st.session_state.turno + 1}</h2>
            <p>Toca para revelar tu identidad</p>
        </div>""", unsafe_allow_html=True)
        if st.button("REVELAR"):
            st.session_state.flipped = True
            st.rerun()
    else:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        if st.session_state.roles[st.session_state.turno]:
            st.markdown('<div style="font-size:80px;">🤫</div><h1 style="color: #dc2626 !important;">INFILTRADO</h1><p>No sabes la palabra.<br>¡TU MISIÓN ES MENTIR!</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p>LA PALABRA SECRETA ES:</p><div class="secret-word-box">{st.session_state.palabra.upper()}</div><h2 style="color: #2563eb !important;">ERES INOCENTE</h2>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        texto_btn = "EMPEZAR DEBATE" if st.session_state.turno == st.session_state.total - 1 else "OCULTAR Y SIGUIENTE"
        if st.button(texto_btn):
            st.session_state.flipped = False
            if st.session_state.turno == st.session_state.total - 1:
                st.session_state.game_state = "show_starter"
            else:
                st.session_state.turno += 1
                st.session_state.game_state = "transition"
            st.rerun()

# PANTALLA 4: QUIÉN EMPIEZA
elif st.session_state.game_state == "show_starter":
    st.markdown(f"""<div style="text-align: center; padding-top: 50px;">
        <div style="font-size: 80px; margin-bottom: 20px;">🗣️</div>
        <h2>RONDA DE PREGUNTAS</h2>
        <p>Debe empezar preguntando el:</p>
        <div style="background: white; color: black; padding: 30px; border-radius: 20px; margin: 30px 0;">
            <h1 style="color: black !important; margin: 0 !important; font-size: 4rem !important;">JUGADOR {st.session_state.jugador_inicial}</h1>
        </div>
    </div>""", unsafe_allow_html=True)
    if st.button("IR A VOTACIÓN"):
        st.session_state.game_state = "voting"
        st.rerun()

# PANTALLA 5: VOTACIÓN
elif st.session_state.game_state == "voting":
    st.markdown('<h1>VOTACIÓN</h1>', unsafe_allow_html=True)
    for i in range(st.session_state.total):
        if i not in st.session_state.eliminados:
            if st.button(f"ACUSAR AL JUGADOR {i+1}", key=f"v_{i}"):
                st.session_state.ultimo_expulsado = i
                st.session_state.eliminados.append(i)
                st.session_state.game_state = "result"
                st.rerun()

# PANTALLA 6: RESULTADO
elif st.session_state.game_state == "result":
    es_imp = st.session_state.roles[st.session_state.ultimo_expulsado]
    st.markdown('<div style="text-align: center; background: rgba(0,0,0,0.2); padding: 40px; border-radius: 24px;">', unsafe_allow_html=True)
    if es_imp:
        st.markdown('<div style="font-size: 80px;">🎯</div><h1 style="color: #4ade80 !important;">¡ERA ÉL!</h1><p>Habéis pillado al infiltrado.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="font-size: 80px;">💀</div><h1 style="color: #ef4444 !important;">¡FALLO!</h1><p>Era un agente inocente.</p>', unsafe_allow_html=True)
    
    st.write(f"### PALABRA: {st.session_state.palabra.upper()}")
    if st.button("REINTENTAR"):
        st.session_state.game_state = "setup"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)