from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Tu enlace de Discord Webhook directo y corregido
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1516502496258949211/CIZ1mLxxBt2MRiqMA4pQ8cV0x56D512n2diBMPCD_X_76Bt5Rgg4PuMobJn1Mhp"

def enviar_notificacion_discord(mensaje):
    try:
        payload = {"content": mensaje}
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print(f"Error al enviar a Discord: {e}")

# Base de datos con las 20 opciones de hospedaje y sus respectivas fotos
HOTELES = [
    {"id": 1, "nombre": "Hotel Plaza y Sol", "descripcion": "Hermoso hotel colonial ubicado en el centro histórico, ideal para descansar.", "precio": "$1,200 MXN", "imagen": "hotel1.jpg"},
    {"id": 2, "nombre": "Cabañas El Mirador", "descripcion": "Rodeadas de naturaleza con una vista espectacular a la sierra.", "precio": "$1,500 MXN", "imagen": "hotel2.jpg"},
    {"id": 3, "nombre": "Posada Del Bosque", "descripcion": "Un lugar tranquilo y acogedor con chimenea en cada habitación.", "precio": "$950 MXN", "imagen": "hotel3.jpg"},
    {"id": 4, "nombre": "Hotel Real Tlalpujahua", "descripcion": "Excelente servicio con un toque tradicional y cercanía al santuario.", "precio": "$1,350 MXN", "imagen": "hotel4.jpg"},
    {"id": 5, "nombre": "Eco-Hotel La Cantera", "descripcion": "Hospedaje sustentable construido con materiales de la región.", "precio": "$1,100 MXN", "imagen": "hotel5.jpg"},
    {"id": 6, "nombre": "Cabañas Los Pinos", "descripcion": "Disfruta del olor a pino y de una noche estrellada junto a la fogata.", "precio": "$1,600 MXN", "imagen": "hotel6.jpg"},
    {"id": 7, "nombre": "Hotel San Juan", "descripcion": "Habitaciones amplias, cómodas y con estacionamiento privado.", "precio": "$800 MXN", "imagen": "hotel7.jpg"},
    {"id": 8, "nombre": "Posada Las Monarcas", "descripcion": "Decoración rústica y un ambiente familiar muy agradable.", "precio": "$900 MXN", "imagen": "hotel8.jpg"},
    {"id": 9, "nombre": "Cabañas El Rincón Escondido", "descripcion": "Privacidad absoluta en medio del bosque para un fin de semana romántico.", "precio": "$1,450 MXN", "imagen": "hotel9.jpg"},
    {"id": 10, "nombre": "Hotel La Terraza", "descripcion": "Cuenta con una espectacular terraza con vista a los tejados del pueblo.", "precio": "$1,050 MXN", "imagen": "hotel10.jpg"},
    {"id": 11, "nombre": "Hostal Centro Mágico", "descripcion": "Opción económica y confortable para mochileros y viajeros.", "precio": "$450 MXN", "imagen": "hotel11.jpg"},
    {"id": 12, "nombre": "Cabañas Valle Verde", "descripcion": "Amplios jardines y juegos infantiles, ideal para toda la familia.", "precio": "$1,700 MXN", "imagen": "hotel12.jpg"},
    {"id": 13, "nombre": "Hotel Mineral del Oro", "descripcion": "Inspirado en el pasado minero de la región, con gran elegancia.", "precio": "$1,300 MXN", "imagen": "hotel13.jpg"},
    {"id": 14, "nombre": "Posada Santa María", "descripcion": "Atención cálida y un desayuno tradicional incluido en tu estancia.", "precio": "$850 MXN", "imagen": "hotel14.jpg"},
    {"id": 15, "nombre": "Cabañas Alpinas El Sol", "descripcion": "Diseño clásico alpino con todas las comodidades modernas.", "precio": "$1,850 MXN", "imagen": "hotel15.jpg"},
    {"id": 16, "nombre": "Hotel Los Faroles", "descripcion": "Iluminación cálida y patios interiores llenos de plantas locales.", "precio": "$1,000 MXN", "imagen": "hotel16.jpg"},
    {"id": 17, "nombre": "Quinta Las Flores", "descripcion": "Hermosa propiedad con alberca climatizada y extensas áreas verdes.", "precio": "$2,100 MXN", "imagen": "hotel17.jpg"},
    {"id": 18, "nombre": "Hotel Villa de Reyes", "descripcion": "Estilo señorial con muebles de madera fina tallados a mano.", "precio": "$1,400 MXN", "imagen": "hotel18.jpg"},
    {"id": 19, "nombre": "Cabañas La Presa", "descripcion": "Ubicadas a la orilla de la presa, perfectas para pesca y caminatas.", "precio": "$1,550 MXN", "imagen": "hotel19.jpg"},
    {"id": 20, "nombre": "Posada Del Campanario", "descripcion": "A unos pasos de la plaza principal, excelente ubicación y precio.", "precio": "$750 MXN", "imagen": "hotel20.jpg"}
]

@app.route('/')
def index():
    # Mandamos la alerta automática a tu Discord cada vez que alguien entra
    enviar_notificacion_discord("¡Alguien acaba de entrar a la página de Ecoturismo!")
    return render_template('index.html', hoteles=HOTELES)

if __name__ == '__main__':
    app.run(debug=True)
