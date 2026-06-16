import os
from flask import Flask, render_template
import requests

app = Flask(__name__)

# ==========================================
# ⚙️ CONFIGURACIÓN DE TU BOT DE TELEGRAM
# ==========================================
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = "7823310574"

def enviar_notificacion_telegram(mensaje):
    try:
        if not TELEGRAM_TOKEN:
            print("❌ ERROR CRÍTICO: No se detecta TELEGRAM_TOKEN en Render.")
            return False
            
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN.strip()}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensaje
        }
        res = requests.post(url, json=payload, timeout=5)
        return res.status_code == 200
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

# ==========================================
# 🌲 BASE DE DATOS DE LOS 15 HOTELES RESTANTES
# ==========================================
HOTELES = [
    {
        "id": 1, 
        "nombre": "Hotel Plaza y Sol", 
        "direccion": "Fray Alonso de la Veracruz #2, Centro Histórico",
        "descripcion": "Hermoso hotel de arquitectura colonial ubicado en el corazón del pueblo mágico. Cuenta con vistas espectaculares a la Parroquia de San Pedro y San Pablo.", 
        "precio": "$1,200 MXN por noche",
        "telefono": "447-123-4567"
    },
    {
        "id": 2, 
        "nombre": "Cabañas El Mirador", 
        "direccion": "Camino al Mirador S/N, Barrio de Guadalupe",
        "descripcion": "Rodeadas de hermosa naturaleza boscosa con una vista espectacular a toda la sierra de Michoacán.", 
        "precio": "$1,500 MXN por noche",
        "telefono": "447-987-6543"
    },
    {
        "id": 3, 
        "nombre": "Posada Del Bosque", 
        "direccion": "Prolongación Moctezuma #45, Zona Boscosa",
        "descripcion": "Un lugar sumamente tranquilo y acogedor que cuenta con chimenea rústica de leña en cada habitación.", 
        "precio": "$950 MXN por noche",
        "telefono": "447-345-6789"
    },
    {
        "id": 4, 
        "nombre": "Hotel Real Tlalpujahua", 
        "direccion": "Juárez #12, A unos pasos del Santuario",
        "descripcion": "Excelente servicio con un toque tradicional inigualable y una cercanía perfecta al Santuario de la Virgen.", 
        "precio": "$1,350 MXN por noche",
        "telefono": "447-456-7890"
    },
    {
        "id": 5, 
        "nombre": "Eco-Hotel La Cantera", 
        "direccion": "Carretera Libre a El Oro Km 3",
        "descripcion": "Hospedaje 100% sustentable construido con la hermosa cantera rosa típica y materiales ecológicos de la región.", 
        "precio": "$1,100 MXN por noche",
        "telefono": "447-567-8901"
    },
    {
        "id": 6, 
        "nombre": "Cabañas Los Pinos", 
        "direccion": "Paraje Las Encinas S/N, Alta Montaña",
        "descripcion": "Disfruta del increíble olor a pino fresco y de una noche estrellada junto a una fogata familiar al aire libre.", 
        "precio": "$1,600 MXN por noche",
        "telefono": "447-678-9012"
    },
    {
        "id": 7, 
        "nombre": "Hotel San Juan", 
        "direccion": "Calle 5 de Mayo #88, Colonia Centro",
        "descripcion": "Habitaciones sumamente amplias, cómodas, con camas matrimoniales y un amplio estacionamiento privado vigilado.", 
        "precio": "$800 MXN por noche",
        "telefono": "447-789-0123"
    },
    {
        "id": 8, 
        "nombre": "Posada Las Monarcas", 
        "direccion": "Avenida Constitución #14, Salida a Maravatío",
        "descripcion": "Decoración rústica estilo michoacano y un ambiente familiar muy agradable para descansar el fin de semana.", 
        "precio": "$900 MXN por noche",
        "telefono": "447-890-1234"
    },
    {
        "id": 9, 
        "nombre": "Cabañas El Rincón Escondido", 
        "direccion": "Camino Vecinal a los Azufres Km 1",
        "descripcion": "Privacidad absoluta en medio del espeso bosque, perfectas para un fin de semana romántico en pareja.", 
        "precio": "$1,450 MXN por noche",
        "telefono": "447-901-2345"
    },
    {
        "id": 10, 
        "nombre": "Hotel La Terraza", 
        "direccion": "Melchor Ocampo #33, Barrio Alto",
        "descripcion": "Cuenta con una espectacular terraza panorámica ideal para tomar fotos a los tejados tradicionales del pueblo.", 
        "precio": "$1,050 MXN por noche",
        "telefono": "447-012-3456"
    },
    {
        "id": 11, 
        "nombre": "Hostal Centro Mágico", 
        "direccion": "Galeana #5, A media cuadra del Jardín Principal",
        "descripcion": "La mejor opción económica, limpia y confortable para mochileros, estudiantes y viajeros frecuentes.", 
        "precio": "$450 MXN por noche",
        "telefono": "447-111-2222"
    },
    {
        "id": 12, 
        "nombre": "Cabañas Valle Verde", 
        "direccion": "Camino Real a Campo Azul S/N",
        "descripcion": "Hermosos y extensos jardines empastados con juegos infantiles de madera, ideal para toda la familia.", 
        "precio": "$1,700 MXN por noche",
        "telefono": "447-222-3333"
    },
    {
        "id": 13, 
        "nombre": "Hotel Mineral del Oro", 
        "direccion": "Calle Minera #202, Zona Alta",
        "descripcion": "Inspirado por completo en el glorioso pasado minero de la región, con gran elegancia y lujo en sus acabados.", 
        "precio": "$1,300 MXN por noche",
        "telefono": "447-333-4444"
    },
    {
        "id": 14, 
        "nombre": "Posada Santa María", 
        "direccion": "Calle Corregidora #10, Barrio de San Miguel",
        "descripcion": "Atención familiar muy cálida y un riquísimo desayuno tradicional de la región incluido en tu estancia.", 
        "precio": "$850 MXN por noche",
        "telefono": "447-444-5555"
    },
    {
        "id": 15, 
        "nombre": "Cabañas Alpinas El Sol", 
        "direccion": "Bosque de los Cedros Sección A, Alta Sierra",
        "descripcion": "Diseño clásico alpino con techos altos de madera a dos aguas y todas las comodidades modernas necesarias.", 
        "precio": "$1,850 MXN por noche",
        "telefono": "447-555-6666"
    }
]

# --- RUTA DE PRUEBA ---
@app.route('/probar-bot')
def probar_bot():
    if not TELEGRAM_TOKEN:
        return "<h3>❌ Error: No se lee el TELEGRAM_TOKEN de Render.</h3>"
    
    exito = enviar_notificacion_telegram("🚀 ¡Prueba exitosa, Emmanuel! Tu código ya funciona.")
    if exito:
        return "<h3>✅ ¡Código conectado! Revisa tu Telegram.</h3>"
    else:
        return f"<h3>❌ Telegram rechazó la petición. Verifica el Token en Render.</h3>"

# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    enviar_notificacion_telegram("🔔 ¡Emmanuel, alguien entró a tu página de Ecoturismo!")
    return render_template('index.html', hoteles=HOTELES)

if __name__ == '__main__':
    app.run(debug=True)
