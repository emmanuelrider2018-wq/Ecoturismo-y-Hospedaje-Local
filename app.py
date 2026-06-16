import os
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Configuración del Bot leyendo desde Render
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = "7823310574"

def enviar_notificacion_telegram(mensaje):
    try:
        # Si Render no le pasa el Token al código, arrojará un aviso en la consola
        if not TELEGRAM_TOKEN:
            print("❌ ERROR CRÍTICO: El código no detecta la variable TELEGRAM_TOKEN de Render.")
            return False
            
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensaje
        }
        res = requests.post(url, json=payload, timeout=5)
        return res.status_code == 200
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

# --- RUTA SECRETA DE PRUEBA ---
# Si entras a tu_link.onrender.com/probar-bot te dirá el error en la pantalla
@app.route('/probar-bot')
def probar_bot():
    if not TELEGRAM_TOKEN:
        return "<h3>❌ Error: Tu código de Python no puede leer el TELEGRAM_TOKEN de Render. Revisa que esté bien guardado en Environment.</h3>"
    
    exito = enviar_notificacion_telegram("🚀 ¡Prueba exitosa, Emmanuel! Tu código ya se conectó correctamente.")
    if exito:
        return "<h3>✅ ¡Código conectado! Revisa tu Telegram, te debió llegar un mensaje.</h3>"
    else:
        return f"<h3>❌ El Token existe de forma interna pero Telegram rechazó la petición. Verifica que no tenga espacios el valor en Render o que el Bot no esté bloqueado. Token detectado (primeros caracteres): {TELEGRAM_TOKEN[:5]}...</h3>"

# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    enviar_notificacion_telegram("🔔 ¡Emmanuel, alguien acaba de entrar a tu página de Ecoturismo en Tlalpujahua!")
    # Nota: Asegúrate de tener tu lista de HOTELES abajo de esto o arriba para que no marque error
    try:
        return render_template('index.html', hoteles=HOTELES)
    except NameError:
        return "<h3>Página activa (Falta pegar la lista de los 20 HOTELES en este archivo nuevo)</h3>"
        # Base de datos local con 20 opciones de hospedaje y sus respectivas fotos
HOTELES = [
    {
        "id": 1,
        "nombre": "Hotel Plaza y Sol",
        "direccion": "Fray Alonso de la Veracruz #2, Centro Histórico",
        "descripcion": "Hermoso hotel de arquitectura colonial ubicado en el corazón del pueblo mágico. Cuenta con vistas espectaculares a la Parroquia de San Pedro y San Pablo.",
        "precio": "$1,200 MXN",
        "servicios": ["Wi-Fi Gratis", "Estacionamiento", "Agua Caliente", "TV por Cable"],
        "contacto": "447-123-4567",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.4jr9YDWBagUw837dXbR2vQHaHp?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 2,
        "nombre": "Cabañas Quinta La Huerta",
        "direccion": "Camino a la Presa del Brockman Km 1.5",
        "descripcion": "Rodeadas de un entorno boscoso inigualable, perfectas para el ecoturismo y un descanso reparador cerca de la hermosa Presa del Brockman.",
        "precio": "$1,800 MXN",
        "servicios": ["Chimenea", "Área de Fogatas", "Pet Friendly", "Terraza Privada"],
        "contacto": "447-987-6543",
        "imagen": "https://tse3.mm.bing.net/th/id/OIP.jU69BMjndnM4hTUKdPzRjwHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 3,
        "nombre": "Hotel Rinconcito Artesanal",
        "direccion": "Juárez #45, Barrio de San Juan",
        "descripcion": "Un espacio acogedor decorado con las tradicionales esferas navideñas y la cantera rosa emblemática de nuestra región.",
        "precio": "$950 MXN",
        "servicios": ["Wi-Fi Gratis", "Desayuno Incluido", "Atención Turística"],
        "contacto": "447-456-7890",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.FMxZajHF5D5FA0GMc80FqAHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 4,
        "nombre": "Hotel Real de Tlalpujahua",
        "direccion": "Melchor Ocampo #12, Colonia Centro",
        "descripcion": "Excelente ubicación con un estilo rústico tradicional. Cuenta con un patio central pintoresco y habitaciones confortables ideales para familias.",
        "precio": "$1,100 MXN",
        "servicios": ["Wi-Fi Gratis", "Televisión HD", "Servicio a la Habitación", "Restaurante"],
        "contacto": "447-112-2334",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.x_cbPyyvEizXqLrdGW9liwHaE7?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 5,
        "nombre": "Cabañas Sierra Vista",
        "direccion": "Zona Boscosa Campo Azul, rumbo a la Presa",
        "descripcion": "Cabañas rústicas de madera con una vista panorámica espectacular a la sierra. Ideales para desconectarse de la ciudad y disfrutar del clima de montaña.",
        "precio": "$1,650 MXN",
        "servicios": ["Chimenea de Leña", "Asadores", "Estacionamiento Privado", "Área Infantil"],
        "contacto": "447-556-6778",
        "imagen": "https://th.bing.com/th/id/R.1938a4362c66c61297a1f2c766e11cd1?rik=Bn392%2bicYlkytg&pid=ImgRaw&r=0"
    },
    {
        "id": 6,
        "nombre": "Posada San José",
        "direccion": "5 de Mayo #8, Barrio de Santa María",
        "descripcion": "Una opción económica, limpia y muy acogedora a pocos minutos caminando de los principales talleres artesanales de esferas.",
        "precio": "$750 MXN",
        "servicios": ["Wi-Fi Gratis", "Agua Caliente 24/7", "Guía de Turistas", "Terraza Común"],
        "contacto": "447-889-9001",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.D9JH37rnr98gi0Q-YGYRcgHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 7,
        "nombre": "Hotel San Vicente",
        "direccion": "Calle San Vicente #4, Centro",
        "descripcion": "Hospedaje tradicional de ambiente familiar, con excelente atención y cercanía a los monumentos históricos principales.",
        "precio": "$900 MXN",
        "servicios": ["Wi-Fi Gratis", "TV Satelital", "Custodia de Equipaje"],
        "contacto": "447-101-2030",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.979nhBXn5djoXvNtMWL4tgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 8,
        "nombre": "Cabañas El Brockman",
        "direccion": "Ribera de la Presa del Brockman",
        "descripcion": "Despierta con la maravillosa vista de la niebla sobre la presa. Cabañas totalmente equipadas para una experiencia de campamento de lujo.",
        "precio": "$2,100 MXN",
        "servicios": ["Muelle Privado", "Chimenea", "Cocina Equipada", "Zona de Pesca"],
        "contacto": "447-223-3445",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.2rSq5_uZJeLUSgM5r06jewHaEk?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 9,
        "nombre": "Hotel Loss Santos",
        "direccion": "Torres Adalid #18, Barrio alta",
        "descripcion": "Estilo rústico elegante con vistas panorámicas hermosas de todo el pueblo mágico desde sus terrazas superiores.",
        "precio": "$1,350 MXN",
        "servicios": ["Wi-Fi", "Restaurante-Bar", "Terraza Mirador", "Caja Fuerte"],
        "contacto": "447-334-4556",
        "imagen": "https://th.bing.com/th/id/OIP._RsEK2ZsTDKveD8Au4PA2AHaFj?r=0&o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 10,
        "nombre": "Hotel  el oyo",
        "direccion": "Calle de la Mina #40, Zona Histórica",
        "descripcion": "Decoración temática inspirada en el pasado minero de Tlalpujahua, ofreciendo un viaje en el tiempo con comodidades modernas.",
        "precio": "$1,050 MXN",
        "servicios": ["Wi-Fi", "Recorridos Guiados", "Cafetería", "Agua Caliente"],
        "contacto": "447-445-5667",
        "imagen": "https://images.oyoroomscdn.com/uploads/hotel_image/95827/9facfaa269ad8d1a.jpg"
    },
    {
        "id": 11,
        "nombre": "Cabañas Los Azules",
        "direccion": "Carretera Tlalpujahua-Maravatío Km 4",
        "descripcion": "Hermosas cabañas ubicadas en un huerto privado llenas de paz, árboles frutales y amplios jardines para caminar.",
        "precio": "$1,400 MXN",
        "servicios": ["Jardín Grande", "Estacionamiento", "Asadores", "Acepta Mascotas"],
        "contacto": "447-556-6778",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.FwYBGaGWo-lTe3b-zh1ExgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 12,
        "nombre": "Hotel Boutique La Casa de las Enredaderas",
        "direccion": "Constitución #15, Barrio de San Pedro",
        "descripcion": "Una casona antigua restaurada con un gusto exquisito, perfecta para parejas que buscan una escapada romántica y relajante.",
        "precio": "$2,400 MXN",
        "servicios": ["Desayuno Gourmet", "Wi-Fi Premium", "Spa", "Tinas de Hidromasaje"],
        "contacto": "447-667-7889",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.XVT0btq_vP57t72TRY-y8gHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 13,
        "nombre": "Posada de la Cantera",
        "direccion": "Calle Libertad #9, Centro Histórico",
        "descripcion": "Construida completamente con la icónica cantera rosa de la región. Habitaciones frescas en verano y térmicas en invierno.",
        "precio": "$850 MXN",
        "servicios": ["Wi-Fi Gratis", "Patio Colonial", "Información Turística"],
        "contacto": "447-778-8990",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.vh4tDSoQfge_bugxbm-L_wHaFN?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 14,
        "nombre": "Hotel Albergue María",
        "direccion": "Prolongación Juárez #88",
        "descripcion": "Una excelente opción para grupos escolares o excursiones grandes. Instalaciones amplias, cómodas y muy seguras.",
        "precio": "$700 MXN",
        "servicios": ["Áreas Comunes", "Comedor", "Wi-Fi", "Seguridad 24 horas"],
        "contacto": "447-889-9001",
        "imagen": "https://th.bing.com/th/id/R.3c56ad927f7a09120fb934926a415c28?rik=hp19LZkCZIjQsA&pid=ImgRaw&r=0"
    },
    {
        "id": 15,
        "nombre": "Cabañas El Encanto Boscoso",
        "direccion": "Camino Viejo a San José s/n",
        "descripcion": "Ubicadas en lo profundo del bosque de oyamel. El lugar ideal para avistar luciérnagas en temporada y descansar rodeado de naturaleza.",
        "precio": "$1,600 MXN",
        "servicios": ["Fogatero", "Balcón Privado", "Senderismo Guiado", "Estacionamiento"],
        "contacto": "447-990-0112",
        "imagen": "https://th.bing.com/th/id/R.a9a013b624057375a4c2879a3b7c172e?rik=YuM1N6%2b0YXBO1g&pid=ImgRaw&r=0"

@app.route('/')
def inicio():
    # Detectamos de dónde viene la visita (Celular, Computadora o UptimeRobot)
    user_agent = request.headers.get('User-Agent', '')
    
    # Filtramos para no llenarte de alertas falsas cada 5 minutos por culpa de UptimeRobot
    if "UptimeRobot" not in user_agent:
        mensaje_alerta = "🔔 *¡Alerta de Tráfico!* Un usuario acaba de ingresar a la Plataforma Web de Hoteles de Tlalpujahua desde su navegador. 🏨✨"
        enviar_notificacion_telegram(mensaje_alerta)
        
    return render_template('index.html', hoteles=HOTELES)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
