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
# 🌲 BASE DE DATOS DE LOS 15 HOTELES CON IMÁGENES
# ==========================================
HOTELES = [
    {
        "id": 1, 
        "nombre": "Hotel Plaza y Sol", 
        "direccion": "Fray Alonso de la Veracruz #2, Centro Histórico",
        "descripcion": "Hermoso hotel de arquitectura colonial ubicado en el corazón del pueblo mágico. Cuenta con vistas espectaculares a la Parroquia de San Pedro y San Pablo.", 
        "precio": "$1,200 MXN por noche",
        "telefono": "447-123-4567",
        "imagen": "https://tse4.mm.bing.net/th/id/OIP.4jr9YDWBagUw837dXbR2vQHaHp?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 2, 
        "nombre": "Cabañas El Mirador", 
        "direccion": "Camino al Mirador S/N, Barrio de Guadalupe",
        "descripcion": "Rodeadas de hermosa naturaleza boscosa con una vista espectacular a toda la sierra de Michoacán.", 
        "precio": "$1,500 MXN por noche",
        "telefono": "447-987-6543",
        "imagen": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/04/48/25/hotel-mansion-san-antonio.jpg?w=900&h=-1&s=1"
    },
    {
        "id": 3, 
        "nombre": "Posada Del Bosque", 
        "direccion": "Prolongación Moctezuma #45, Zona Boscosa",
        "descripcion": "Un lugar sumamente tranquilo y acogedor que cuenta con chimenea rústica de leña en cada habitación.", 
        "precio": "$950 MXN por noche",
        "telefono": "447-345-6789",
        "imagen": "https://th.bing.com/th/id/R.d32a92a2245b0e5e44fb5a79db85aecb?rik=MgtGQt%2fnszaTaA&pid=ImgRaw&r=0"
    },
    {
        "id": 4, 
        "nombre": "Hotel Real Tlalpujahua", 
        "direccion": "Juárez #12, A unos pasos del Santuario",
        "descripcion": "Excelente servicio con un toque tradicional inigualable y una cercanía perfecta al Santuario de la Virgen.", 
        "precio": "$1,350 MXN por noche",
        "telefono": "447-456-7890",
        "imagen": "https://th.bing.com/th/id/R.f2925a1d42aa4c0a272ef601d3c45d7b?rik=nb%2bUGlQo0x15Cw&pid=ImgRaw&r=0"
    },
    {
        "id": 5, 
        "nombre": "Eco-Hotel La Cantera", 
        "direccion": "Carretera Libre a El Oro Km 3",
        "descripcion": "Hospedaje 100% sustentable construido con la hermosa cantera rosa típica y materiales ecológicos de la región.", 
        "precio": "$1,100 MXN por noche",
        "telefono": "447-567-8901",
        "imagen": "https://tse2.mm.bing.net/th/id/OIP.a36O24W9R0-WBNKxT88oBAHaDf?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 6, 
        "nombre": "Cabañas Los Pinos", 
        "direccion": "Paraje Las Encinas S/N, Alta Montaña",
        "descripcion": "Disfruta del increíble olor a pino fresco y de una noche estrellada junto a una fogata familiar al aire libre.", 
        "precio": "$1,600 MXN por noche",
        "telefono": "447-678-9012",
        "imagen": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/6b/b9/04/hotel-posada-del-carmen.jpg?w=1000&h=-1&s=1"
    },
    {
        "id": 7, 
        "nombre": "Hotel San Juan", 
        "direccion": "Calle 5 de Mayo #88, Colonia Centro",
        "descripcion": "Habitaciones sumamente amplias, cómodas, con camas matrimoniales y un amplio estacionamiento privado vigilado.", 
        "precio": "$800 MXN por noche",
        "telefono": "447-789-0123",
        "imagen": "https://media-cdn.tripadvisor.com/media/photo-s/0e/ba/19/57/casa-tlalpujahua.jpg"
    },
    {
        "id": 8, 
        "nombre": "Posada Las Monarcas", 
        "direccion": "Avenida Constitución #14, Salida a Maravatío",
        "descripcion": "Decoración rústica estilo michoacano y un ambiente familiar muy agradable para descansar el fin de semana.", 
        "precio": "$900 MXN por noche",
        "telefono": "447-890-1234",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.yUUto855sLyR-e5ALbC1bwHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 9, 
        "nombre": "Cabañas El Rincón Escondido", 
        "direccion": "Camino Vecinal a los Azufres Km 1",
        "descripcion": "Privacidad absoluta en medio del espeso bosque, perfectas para un fin de semana romántico en pareja.", 
        "precio": "$1,450 MXN por noche",
        "telefono": "447-901-2345",
        "imagen": "https://tse2.mm.bing.net/th/id/OIP.o-Ds33sIBkk_6YNMzR0sNgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 10, 
        "nombre": "Hotel La Terraza", 
        "direccion": "Melchor Ocampo #33, Barrio Alto",
        "descripcion": "Cuenta con una espectacular terraza panorámica ideal para tomar fotos a los tejados tradicionales del pueblo.", 
        "precio": "$1,050 MXN por noche",
        "telefono": "447-012-3456",
        "imagen": "https://tse3.mm.bing.net/th/id/OIP.OS3BnHsR-VKh4BFY1cNnwwHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 11, 
        "nombre": "Hostal Centro Mágico", 
        "direccion": "Galeana #5, A media cuadra del Jardín Principal",
        "descripcion": "La mejor opción económica, limpia y confortable para mochileros, estudiantes y viajeros frecuentes.", 
        "precio": "$450 MXN por noche",
        "telefono": "447-111-2222",
        "imagen": "https://tse3.mm.bing.net/th/id/OIP.1nU7VIhKeAv4hHE7WTcudgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 12, 
        "nombre": "Cabañas Valle Verde", 
        "direccion": "Camino Real a Campo Azul S/N",
        "descripcion": "Hermosos y extensos jardines empastados con juegos infantiles de madera, ideal para toda la familia.", 
        "precio": "$1,700 MXN por noche",
        "telefono": "447-222-3333",
        "imagen": "https://th.bing.com/th/id/OIP.CWNsAYqdaO1FBoHiDxyUMwHaE9?r=0&o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 13, 
        "nombre": "Hotel Mineral del Oro", 
        "direccion": "Calle Minera #202, Zona Alta",
        "descripcion": "Inspirado por completo en el glorioso pasado minero de la región, con gran elegancia y lujo en sus acabados.", 
        "precio": "$1,300 MXN por noche",
        "telefono": "447-333-4444",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.k1W0Dl2vkqS4gHrA5eTfCQHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 14, 
        "nombre": "Posada Santa María", 
        "direccion": "Calle Corregidora #10, Barrio de San Miguel",
        "descripcion": "Atención familiar muy cálida y un riquísimo desayuno tradicional de la región incluido en tu estancia.", 
        "precio": "$850 MXN por noche",
        "telefono": "447-444-5555",
        "imagen": "https://tse1.mm.bing.net/th/id/OIP.HNZoGVJmSbB9HXlBktD9ZQHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
        "id": 15, 
        "nombre": "Cabañas Alpinas El Sol", 
        "direccion": "Bosque de los Cedros Sección A, Alta Sierra",
        "descripcion": "Diseño clásico alpino con techos altos de madera a dos aguas y todas las comodidades modernas necesarias.", 
        "precio": "$1,850 MXN por noche",
        "telefono": "447-555-6666",
        "imagen": "https://escapadas.mexicodesconocido.com.mx/wp-content/uploads/2024/02/tlalpujahua-1000x563.jpg"
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
