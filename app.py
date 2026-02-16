import streamlit as st
import random

# =============================================================================
# CONFIGURACIÓN DE PÁGINA
# =============================================================================
URL_LOGO = "https://raw.githubusercontent.com/gerardsarda/juego_infiltrado/main/Gemini_Generated_Image_poe3ntpoe3ntpoe3.png"
st.set_page_config(
    page_title="Infiltrado", 
    page_icon=URL_LOGO, 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CONFIGURACIÓN DE NEGOCIO
# =============================================================================
STRIPE_LINK = "https://buy.stripe.com/PON_AQUI_TU_LINK_REAL" 
CLAVE_MAESTRA = "IMP-VIP-99"

# =============================================================================
# SISTEMA DE DISEÑO MODERNO
# =============================================================================
st.markdown("""
    <style>
    /* ===== TIPOGRAFÍA ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    /* ===== VARIABLES DE DISEÑO ===== */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --primary-light: #818cf8;
        --secondary: #8b5cf6;
        --accent: #ec4899;
        --success: #10b981;
        --danger: #ef4444;
        --warning: #f59e0b;
        --dark: #0f172a;
        --dark-light: #1e293b;
        --gray: #64748b;
        --gray-light: #cbd5e1;
        --bg: #f8fafc;
        --card: #ffffff;
        --radius: 16px;
        --radius-lg: 24px;
        --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
    }
    
    /* ===== FONDO GLOBAL ===== */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    /* ===== CONTENEDOR PRINCIPAL ===== */
    .main > div {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* ===== HERO HEADER ===== */
    .hero-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: var(--radius-lg);
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-xl);
        border: 1px solid rgba(255, 255, 255, 0.8);
        position: relative;
        overflow: hidden;
    }
    
    .hero-header::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    }
    
    .hero-title {
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 900;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, var(--accent) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        color: var(--gray);
        font-size: 1.125rem;
        margin-top: 1rem;
        font-weight: 500;
    }
    
    /* ===== CARDS ===== */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: var(--radius-lg);
        padding: 2rem;
        box-shadow: var(--shadow-lg);
        border: 1px solid rgba(255, 255, 255, 0.8);
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-xl);
    }
    
    .dark-card {
        background: linear-gradient(135deg, var(--dark) 0%, var(--dark-light) 100%);
        color: white;
        border-radius: var(--radius-lg);
        padding: 2.5rem;
        text-align: center;
        box-shadow: var(--shadow-xl);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1.5rem;
    }
    
    .premium-card {
        background: linear-gradient(135deg, #1e1e1e 0%, #000000 100%);
        color: #fbbf24;
        border-radius: var(--radius-lg);
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 0 40px rgba(251, 191, 36, 0.3), var(--shadow-xl);
        border: 2px solid #fbbf24;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }
    
    .premium-card::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(251, 191, 36, 0.1), transparent);
        animation: premium-shine 3s infinite;
    }
    
    @keyframes premium-shine {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* ===== BOTONES ===== */
    .stButton > button {
        width: 100%;
        border-radius: 12px !important;
        padding: 0.875rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: none !important;
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
        color: white !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5) !important;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* ===== FLIP CARD (MEJORADA) ===== */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 400px;
        perspective: 1000px;
        margin: 2rem 0;
    }
    
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        transform-style: preserve-3d;
    }
    
    .flipped {
        transform: rotateY(180deg);
    }
    
    .flip-card-front, 
    .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: var(--radius-lg);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        box-shadow: var(--shadow-xl);
    }
    
    .flip-card-front {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
    }
    
    .flip-card-back {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        color: var(--dark);
        transform: rotateY(180deg);
        border: 2px solid rgba(99, 102, 241, 0.2);
    }
    
    .card-emoji {
        font-size: 5rem;
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .card-title {
        font-size: 2rem;
        font-weight: 700;
        margin: 1rem 0 0.5rem;
    }
    
    .card-subtitle {
        font-size: 1.125rem;
        opacity: 0.9;
    }
    
    /* ===== PROGRESS BAR ===== */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--primary), var(--secondary)) !important;
        border-radius: 10px;
    }
    
    .stProgress > div > div {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px;
        height: 8px !important;
    }
    
    /* ===== SELECTBOX ===== */
    .stSelectbox > div > div {
        background: white !important;
        border-radius: var(--radius) !important;
        border: 2px solid var(--gray-light) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* ===== SLIDER ===== */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, var(--primary), var(--secondary)) !important;
    }
    
    /* ===== VOTE BUTTONS ===== */
    .vote-button {
        width: 100%;
        padding: 1.25rem;
        border-radius: var(--radius);
        border: 2px solid var(--primary);
        background: white;
        color: var(--primary);
        font-weight: 600;
        font-size: 1.125rem;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 0.75rem;
        text-align: center;
        box-shadow: var(--shadow);
    }
    
    .vote-button:hover {
        background: var(--primary);
        color: white;
        transform: translateX(4px);
        box-shadow: var(--shadow-lg);
    }
    
    .vote-button:active {
        transform: translateX(2px);
    }
    
    .eliminated-player {
        text-align: center;
        padding: 1rem;
        color: var(--gray);
        text-decoration: line-through;
        opacity: 0.5;
        margin-bottom: 0.75rem;
    }
    
    /* ===== BADGES ===== */
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.875rem;
        margin: 0.25rem;
    }
    
    .badge-vip {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: #78350f;
    }
    
    .badge-free {
        background: linear-gradient(135deg, var(--success) 0%, #059669 100%);
        color: white;
    }
    
    /* ===== ALERTS ===== */
    .custom-alert {
        padding: 1rem 1.5rem;
        border-radius: var(--radius);
        margin: 1rem 0;
        font-weight: 500;
    }
    
    .alert-info {
        background: #dbeafe;
        color: #1e40af;
        border-left: 4px solid #3b82f6;
    }
    
    .alert-warning {
        background: #fef3c7;
        color: #92400e;
        border-left: 4px solid #f59e0b;
    }
    
    .alert-danger {
        background: #fee2e2;
        color: #991b1b;
        border-left: 4px solid #ef4444;
    }
    
    .alert-success {
        background: #d1fae5;
        color: #065f46;
        border-left: 4px solid #10b981;
    }
    
    /* ===== STARTER CARD ===== */
    .starter-card {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
        border-radius: var(--radius-lg);
        padding: 3rem 2rem;
        text-align: center;
        box-shadow: var(--shadow-xl);
        margin: 2rem 0;
    }
    
    .starter-number {
        background: white;
        color: var(--primary);
        border-radius: var(--radius);
        padding: 1.5rem;
        margin: 1.5rem 0;
        font-size: 3rem;
        font-weight: 900;
        box-shadow: var(--shadow-lg);
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .glass-card, .dark-card, .premium-card {
            padding: 1.5rem;
        }
        
        .flip-card {
            height: 350px;
        }
    }
    
    /* ===== ANIMACIONES ===== */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* ===== OCULTAR ELEMENTOS DE STREAMLIT ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# BASE DE DATOS DE PALABRAS
# =============================================================================

# LISTAS GRATUITAS
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

# Mix gratis
lista_tutifruti = lista_animales + lista_casa + lista_colores + lista_profesiones

# Diccionario de listas gratuitas
DATOS_FREE = {
    "🎲 TUTIFRUTI (Mix Gratis)": lista_tutifruti, 
    "🐶 Animales": lista_animales,
    "🏠 Objetos de Casa": lista_casa,
    "🎨 Colores y Formas": lista_colores,
    "👔 Profesiones": lista_profesiones
}

# LISTAS VIP (contenido completo)
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

# =============================================================================
# INICIALIZACIÓN DE SESSION STATE
# =============================================================================
if 'game_state' not in st.session_state:
    st.session_state.game_state = "setup"
if 'vip_unlocked' not in st.session_state:
    st.session_state.vip_unlocked = False
if 'card_flipped' not in st.session_state:
    st.session_state.card_flipped = False
if 'eliminados' not in st.session_state:
    st.session_state.eliminados = []

# =============================================================================
# PANTALLA 1: SETUP INICIAL
# =============================================================================
if st.session_state.game_state == "setup":
    
    # Hero header
    st.markdown("""
        <div class="hero-header fade-in">
            <h1 class="hero-title">🕵️ INFILTRADO</h1>
            <p class="hero-subtitle">El juego social de mentiras y deducciones</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Card de configuración
    st.markdown('<div class="glass-card fade-in">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Configuración de la Partida")
    
    # Número de jugadores
    num = st.slider(
        "👥 Número de jugadores",
        min_value=3,
        max_value=15,
        value=5,
        help="Mínimo 3 jugadores para jugar"
    )
    
    # Número de infiltrados
    max_inf = max(1, num // 3)
    inf = st.slider(
        "😈 Número de infiltrados",
        min_value=1,
        max_value=max_inf,
        value=1,
        help="Los infiltrados no conocerán la palabra secreta"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Selección de categoría
    st.markdown('<div class="glass-card fade-in">', unsafe_allow_html=True)
    st.markdown("### 📚 Selecciona una Categoría")
    
    # Mostrar categorías disponibles
    categorias_disponibles = list(DATOS_FREE.keys())
    
    # Mostrar VIP si está desbloqueado
    if st.session_state.vip_unlocked:
        categorias_disponibles += list(DATOS_VIP.keys())
        st.success("🌟 ¡Contenido VIP desbloqueado!")
    
    categoria = st.selectbox(
        "Categoría",
        categorias_disponibles,
        label_visibility="collapsed"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Paywall VIP
    if not st.session_state.vip_unlocked:
        st.markdown("""
            <div class="premium-card fade-in">
                <div style="font-size: 4rem; margin-bottom: 1rem;">👑</div>
                <h2 style="margin: 1rem 0; font-size: 2rem;">DESBLOQUEA CONTENIDO VIP</h2>
                <p style="opacity: 0.9; margin-bottom: 1.5rem;">
                    Accede a categorías exclusivas: Modo Canalla (+18), Películas, Videojuegos, Música y más
                </p>
                <div style="background: rgba(251, 191, 36, 0.1); padding: 1rem; border-radius: 12px; margin: 1rem 0;">
                    <p style="margin: 0; font-size: 1.125rem;">💎 Solo <strong>3,99€</strong> - Acceso de por vida</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔓 Desbloquear VIP", use_container_width=True):
                st.markdown(f'<meta http-equiv="refresh" content="0; url={STRIPE_LINK}">', unsafe_allow_html=True)
        
        with col2:
            codigo = st.text_input("Código de acceso", type="password", placeholder="Introduce tu código")
            if codigo == CLAVE_MAESTRA:
                st.session_state.vip_unlocked = True
                st.rerun()
    
    # Botón para iniciar
    st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
    if st.button("🎮 INICIAR PARTIDA", type="primary"):
        # Seleccionar palabra
        if categoria in DATOS_FREE:
            palabra = random.choice(DATOS_FREE[categoria])
        else:
            palabra = random.choice(DATOS_VIP[categoria])
        
        # Asignar roles
        roles = [False] * num
        indices_infiltrados = random.sample(range(num), inf)
        for idx in indices_infiltrados:
            roles[idx] = True
        
        # Guardar en session state
        st.session_state.palabra = palabra
        st.session_state.total = num
        st.session_state.roles_bool = roles
        st.session_state.turno = 0
        st.session_state.jugador_inicial = random.randint(0, num - 1)
        st.session_state.eliminados = []
        st.session_state.game_state = "transition"
        st.rerun()

# =============================================================================
# PANTALLA 2: TRANSICIÓN
# =============================================================================
elif st.session_state.game_state == "transition":
    turno_actual = st.session_state.turno + 1
    
    st.markdown(f"""
        <div class="dark-card fade-in" style="margin-top: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🎯</div>
            <h1 style="font-size: 3rem; margin: 1rem 0;">JUGADOR {turno_actual}</h1>
            <p style="font-size: 1.25rem; opacity: 0.9;">Prepárate para ver tu rol</p>
            <div style="margin-top: 2rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 12px;">
                <p style="margin: 0; font-size: 0.875rem;">⚠️ Asegúrate de que nadie más esté mirando</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("👁️ VER MI ROL", type="primary"):
        st.session_state.game_state = "playing"
        st.session_state.card_flipped = False
        st.rerun()

# =============================================================================
# PANTALLA 3: JUEGO (CARTAS)
# =============================================================================
elif st.session_state.game_state == "playing":
    turno = st.session_state.turno
    progreso = (turno + 1) / st.session_state.total
    
    st.progress(progreso)
    st.markdown(
        f'<p style="text-align:center; color: rgba(255,255,255,0.8); font-size: 0.875rem; margin: 0.5rem 0;">Jugador {turno + 1} de {st.session_state.total}</p>',
        unsafe_allow_html=True
    )
    
    # Preparar contenido de la carta
    if st.session_state.roles_bool[turno]:
        # Es infiltrado
        contenido = """
            <div style="text-align: center;">
                <span class="card-emoji">😈</span>
                <h2 class="card-title" style="color: #ef4444;">ERES EL INFILTRADO</h2>
                <div class="custom-alert alert-danger" style="margin-top: 1.5rem;">
                    ⚠️ No conoces la palabra. Debes mentir y pasar desapercibido
                </div>
            </div>
        """
    else:
        # Es inocente
        contenido = f"""
            <div style="text-align: center;">
                <p style="color: #64748b; margin-bottom: 0.5rem;">La palabra secreta es:</p>
                <h1 class="card-title" style="font-size: 3rem; color: #6366f1; margin: 1rem 0;">
                    {st.session_state.palabra.upper()}
                </h1>
                <span class="card-emoji">✅</span>
                <div class="custom-alert alert-success" style="margin-top: 1.5rem;">
                    💡 Tienes que descubrir quién es el infiltrado
                </div>
            </div>
        """
    
    flip_cls = "flipped" if st.session_state.get('card_flipped', False) else ""
    
    # Renderizar carta con flip
    st.markdown(f"""
        <div class="flip-card">
            <div class="flip-card-inner {flip_cls}">
                <div class="flip-card-front">
                    <span class="card-emoji">🃏</span>
                    <h2 class="card-title">TU CARTA</h2>
                    <p class="card-subtitle">Toca el botón para revelar</p>
                </div>
                <div class="flip-card-back">
                    {contenido}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Botones de acción
    if not st.session_state.get('card_flipped'):
        if st.button("👁️ REVELAR MI ROL", type="primary"):
            st.session_state.card_flipped = True
            st.rerun()
    else:
        es_ultimo = turno >= st.session_state.total - 1
        
        if es_ultimo:
            if st.button("🗳️ IR A VOTACIONES", type="primary"):
                st.session_state.card_flipped = False
                st.session_state.game_state = "show_starter"
                st.rerun()
        else:
            if st.button("➡️ SIGUIENTE JUGADOR", type="primary"):
                st.session_state.card_flipped = False
                st.session_state.turno += 1
                st.session_state.game_state = "transition"
                st.rerun()

# =============================================================================
# PANTALLA 3.5: MOSTRAR QUIÉN EMPIEZA
# =============================================================================
elif st.session_state.game_state == "show_starter":
    inicial = st.session_state.jugador_inicial
    
    st.markdown(f"""
        <div class="starter-card fade-in" style="margin-top: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🎲</div>
            <h2 style="font-size: 2rem; margin: 1rem 0;">¡ROLES REPARTIDOS!</h2>
            <p style="font-size: 1.125rem; opacity: 0.9; margin-bottom: 1rem;">Comienza hablando:</p>
            <div class="starter-number">
                JUGADOR {inicial + 1}
            </div>
            <p style="font-size: 1rem; opacity: 0.9;">Hacedle la primera pregunta sobre la palabra</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("⏱️ EMPEZAR DEBATE", type="primary"):
        st.session_state.game_state = "voting_round"
        st.rerun()

# =============================================================================
# PANTALLA 4: VOTACIÓN
# =============================================================================
elif st.session_state.game_state == "voting_round":
    st.markdown("""
        <div class="hero-header fade-in" style="margin-top: 0; padding: 2rem;">
            <h2 class="hero-title" style="font-size: 2rem;">🗳️ VOTACIÓN</h2>
            <p class="hero-subtitle" style="margin-top: 0.5rem;">¿Quién es el infiltrado?</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    for i in range(st.session_state.total):
        if i not in st.session_state.eliminados:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(
                    f'<div class="vote-button">👤 JUGADOR {i+1}</div>',
                    unsafe_allow_html=True
                )
            with col2:
                if st.button("Votar", key=f"vote_{i}", type="primary"):
                    st.session_state.ultimo_expulsado = i
                    st.session_state.eliminados.append(i)
                    st.session_state.game_state = "round_result"
                    st.rerun()
        else:
            st.markdown(
                f'<div class="eliminated-player">💀 Jugador {i+1} (Eliminado)</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# PANTALLA 5: RESULTADO
# =============================================================================
elif st.session_state.game_state == "round_result":
    expulsado = st.session_state.ultimo_expulsado
    es_impostor = st.session_state.roles_bool[expulsado]
    
    # Contar supervivientes
    impostores_vivos = sum(
        1 for i in range(st.session_state.total)
        if st.session_state.roles_bool[i] and i not in st.session_state.eliminados
    )
    inocentes_vivos = sum(
        1 for i in range(st.session_state.total)
        if not st.session_state.roles_bool[i] and i not in st.session_state.eliminados
    )
    
    st.markdown('<div class="glass-card fade-in" style="text-align: center; margin-top: 3rem;">', unsafe_allow_html=True)
    
    if es_impostor:
        st.markdown("""
            <div style="font-size: 5rem; margin-bottom: 1rem;">😈</div>
            <h1 style="color: #10b981; font-size: 3rem; margin-bottom: 1rem;">¡ERA INFILTRADO!</h1>
        """, unsafe_allow_html=True)
        
        if impostores_vivos == 0:
            st.balloons()
            st.markdown("""
                <div class="custom-alert alert-success">
                    🎉 ¡VICTORIA DE LOS INOCENTES!
                </div>
            """, unsafe_allow_html=True)
            st.info(f"**La palabra era:** {st.session_state.palabra}")
            
            if st.button("🔄 JUGAR OTRA PARTIDA", type="primary"):
                st.session_state.game_state = "setup"
                st.session_state.eliminados = []
                st.rerun()
            st.stop()
        else:
            st.markdown(f"""
                <div class="custom-alert alert-info">
                    ℹ️ Quedan {impostores_vivos} infiltrado(s) en el juego
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="font-size: 5rem; margin-bottom: 1rem;">😱</div>
            <h1 style="color: #ef4444; font-size: 3rem; margin-bottom: 1rem;">¡ERA INOCENTE!</h1>
        """, unsafe_allow_html=True)
        
        if impostores_vivos >= inocentes_vivos:
            st.markdown("""
                <div class="custom-alert alert-danger">
                    💀 ¡GANAN LOS INFILTRADOS!
                </div>
            """, unsafe_allow_html=True)
            st.info(f"**La palabra era:** {st.session_state.palabra}")
            
            if st.button("🔄 JUGAR OTRA PARTIDA", type="primary"):
                st.session_state.game_state = "setup"
                st.session_state.eliminados = []
                st.rerun()
            st.stop()
        else:
            st.markdown("""
                <div class="custom-alert alert-warning">
                    ⚠️ Habéis fallado. La partida continúa
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("➡️ SIGUIENTE RONDA", type="primary"):
        st.session_state.game_state = "voting_round"
        st.rerun()
