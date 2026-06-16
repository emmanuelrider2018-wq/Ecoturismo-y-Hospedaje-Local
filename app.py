from flask import Flask, render_template, request
import requests

app = Flask(name)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1516502496258949211/CIZlmLxxBt2MRiqMA4pQ8cV0x56D512n2diBMPCD_X_76Bt5Rgg4PuMobJnlMhp"

def enviar_notificacion_discord(mensaje):
    try:
        payload = {"content": mensaje}
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print(f"Error: {e}")
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
        "imagen": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 2,
        "nombre": "Cabañas Quinta La Huerta",
        "direccion": "Camino a la Presa del Brockman Km 1.5",
        "descripcion": "Rodeadas de un entorno boscoso inigualable, perfectas para el ecoturismo y un descanso reparador cerca de la hermosa Presa del Brockman.",
        "precio": "$1,800 MXN",
        "servicios": ["Chimenea", "Área de Fogatas", "Pet Friendly", "Terraza Privada"],
        "contacto": "447-987-6543",
        "imagen": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 3,
        "nombre": "Hotel Rinconcito Artesanal",
        "direccion": "Juárez #45, Barrio de San Juan",
        "descripcion": "Un espacio acogedor decorado con las tradicionales esferas navideñas y la cantera rosa emblemática de nuestra región.",
        "precio": "$950 MXN",
        "servicios": ["Wi-Fi Gratis", "Desayuno Incluido", "Atención Turística"],
        "contacto": "447-456-7890",
        "imagen": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 4,
        "nombre": "Hotel Real de Tlalpujahua",
        "direccion": "Melchor Ocampo #12, Colonia Centro",
        "descripcion": "Excelente ubicación con un estilo rústico tradicional. Cuenta con un patio central pintoresco y habitaciones confortables ideales para familias.",
        "precio": "$1,100 MXN",
        "servicios": ["Wi-Fi Gratis", "Televisión HD", "Servicio a la Habitación", "Restaurante"],
        "contacto": "447-112-2334",
        "imagen": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 5,
        "nombre": "Cabañas Sierra Vista",
        "direccion": "Zona Boscosa Campo Azul, rumbo a la Presa",
        "descripcion": "Cabañas rústicas de madera con una vista panorámica espectacular a la sierra. Ideales para desconectarse de la ciudad y disfrutar del clima de montaña.",
        "precio": "$1,650 MXN",
        "servicios": ["Chimenea de Leña", "Asadores", "Estacionamiento Privado", "Área Infantil"],
        "contacto": "447-556-6778",
        "imagen": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 6,
        "nombre": "Posada San José",
        "direccion": "5 de Mayo #8, Barrio de Santa María",
        "descripcion": "Una opción económica, limpia y muy acogedora a pocos minutos caminando de los principales talleres artesanales de esferas.",
        "precio": "$750 MXN",
        "servicios": ["Wi-Fi Gratis", "Agua Caliente 24/7", "Guía de Turistas", "Terraza Común"],
        "contacto": "447-889-9001",
        "imagen": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 7,
        "nombre": "Hotel San Vicente",
        "direccion": "Calle San Vicente #4, Centro",
        "descripcion": "Hospedaje tradicional de ambiente familiar, con excelente atención y cercanía a los monumentos históricos principales.",
        "precio": "$900 MXN",
        "servicios": ["Wi-Fi Gratis", "TV Satelital", "Custodia de Equipaje"],
        "contacto": "447-101-2030",
        "imagen": "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 8,
        "nombre": "Cabañas El Brockman",
        "direccion": "Ribera de la Presa del Brockman",
        "descripcion": "Despierta con la maravillosa vista de la niebla sobre la presa. Cabañas totalmente equipadas para una experiencia de campamento de lujo.",
        "precio": "$2,100 MXN",
        "servicios": ["Muelle Privado", "Chimenea", "Cocina Equipada", "Zona de Pesca"],
        "contacto": "447-223-3445",
        "imagen": "https://images.unsplash.com/photo-1449034446853-66c86144b0ad?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 9,
        "nombre": "Hotel Loss Santos",
        "direccion": "Torres Adalid #18, Barrio alta",
        "descripcion": "Estilo rústico elegante con vistas panorámicas hermosas de todo el pueblo mágico desde sus terrazas superiores.",
        "precio": "$1,350 MXN",
        "servicios": ["Wi-Fi", "Restaurante-Bar", "Terraza Mirador", "Caja Fuerte"],
        "contacto": "447-334-4556",
        "imagen": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 10,
        "nombre": "Hotel El Mineral",
        "direccion": "Calle de la Mina #40, Zona Histórica",
        "descripcion": "Decoración temática inspirada en el pasado minero de Tlalpujahua, ofreciendo un viaje en el tiempo con comodidades modernas.",
        "precio": "$1,050 MXN",
        "servicios": ["Wi-Fi", "Recorridos Guiados", "Cafetería", "Agua Caliente"],
        "contacto": "447-445-5667",
        "imagen": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 11,
        "nombre": "Cabañas Los Azules",
        "direccion": "Carretera Tlalpujahua-Maravatío Km 4",
        "descripcion": "Hermosas cabañas ubicadas en un huerto privado llenas de paz, árboles frutales y amplios jardines para caminar.",
        "precio": "$1,400 MXN",
        "servicios": ["Jardín Grande", "Estacionamiento", "Asadores", "Acepta Mascotas"],
        "contacto": "447-556-6778",
        "imagen": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 12,
        "nombre": "Hotel Boutique La Casa de las Enredaderas",
        "direccion": "Constitución #15, Barrio de San Pedro",
        "descripcion": "Una casona antigua restaurada con un gusto exquisito, perfecta para parejas que buscan una escapada romántica y relajante.",
        "precio": "$2,400 MXN",
        "servicios": ["Desayuno Gourmet", "Wi-Fi Premium", "Spa", "Tinas de Hidromasaje"],
        "contacto": "447-667-7889",
        "imagen": "https://images.unsplash.com/photo-1613553507747-5f8d62ad5904?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 13,
        "nombre": "Posada de la Cantera",
        "direccion": "Calle Libertad #9, Centro Histórico",
        "descripcion": "Construida completamente con la icónica cantera rosa de la región. Habitaciones frescas en verano y térmicas en invierno.",
        "precio": "$850 MXN",
        "servicios": ["Wi-Fi Gratis", "Patio Colonial", "Información Turística"],
        "contacto": "447-778-8990",
        "imagen": "https://images.unsplash.com/photo-1504624244673-496552433c00?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 14,
        "nombre": "Hotel Albergue María",
        "direccion": "Prolongación Juárez #88",
        "descripcion": "Una excelente opción para grupos escolares o excursiones grandes. Instalaciones amplias, cómodas y muy seguras.",
        "precio": "$700 MXN",
        "servicios": ["Áreas Comunes", "Comedor", "Wi-Fi", "Seguridad 24 horas"],
        "contacto": "447-889-9001",
        "imagen": "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 15,
        "nombre": "Cabañas El Encanto Boscoso",
        "direccion": "Camino Viejo a San José s/n",
        "descripcion": "Ubicadas en lo profundo del bosque de oyamel. El lugar ideal para avistar luciérnagas en temporada y descansar rodeado de naturaleza.",
        "precio": "$1,600 MXN",
        "servicios": ["Fogatero", "Balcón Privado", "Senderismo Guiado", "Estacionamiento"],
        "contacto": "447-990-0112",
        "imagen": "https://images.unsplash.com/photo-1542718610-a1d656d1884c?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 16,
        "nombre": "Hotel Colonial Tlalpujahua",
        "direccion": "Allende #22, Centro",
        "descripcion": "Con el clásico diseño de los portales tradicionales, amplios pasillos y una atmósfera tranquila en el corazón de la acción turística.",
        "precio": "$1,150 MXN",
        "servicios": ["Wi-Fi", "TV por cable", "Café de Cortesía", "Plancha a solicitud"],
        "contacto": "447-112-3581",
        "imagen": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 17,
        "nombre": "Hotel Rancho Viejo",
        "direccion": "Domicilio Conocido, Comunidad de Santa María",
        "descripcion": "Un concepto de hotel campestre que combina las comodidades modernas con actividades rurales y paseos a caballo.",
        "precio": "$1,500 MXN",
        "servicios": ["Caballerizas", "Alberca Techada", "Restaurante de Antojitos", "Wi-Fi"],
        "contacto": "447-213-4711",
        "imagen": "https://images.unsplash.com/photo-1535827841776-24afc882f03e?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 18,
        "nombre": "Posada Santa Fe",
        "direccion": "Galeana #5, Barrio de los Remedios",
        "descripcion": "Pequeño y pintoresco hospedaje que destaca por la amabilidad de su personal y la espectacular limpieza de sus instalaciones.",
        "precio": "$800 MXN",
        "servicios": ["Wi-Fi Gratis", "Agua Caliente 24/7", "Amenities de Baño"],
        "contacto": "447-314-1592",
        "imagen": "https://images.unsplash.com/photo-1495365200479-c4ed1d35e1aa?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 19,
        "nombre": "Cabañas Villa de las Esferas",
        "direccion": "Salida a las Torres de la Iglesia Hundida",
        "descripcion": "Cabañas familiares muy cerca de los talleres de vidrio soplado de esferas navideñas. Espaciosas y con áreas verdes privadas.",
        "precio": "$1,300 MXN",
        "servicios": ["Área de Asado", "Juegos Infantiles", "Wi-Fi", "Estacionamiento"],
        "contacto": "447-414-2135",
        "imagen": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=500&auto=format&fit=crop&q=60"
    },
    {
        "id": 20,
        "nombre": "Hotel Vista Hermosa",
        "direccion": "Camino al Mirador Poniente #31",
        "descripcion": "Ubicado en el punto más alto del pueblo, ofrece la mejor vista panorámica para fotografiar los atardeceres de Tlalpujahua.",
        "precio": "$1,250 MXN",
        "servicios": ["Balcón Panorámico", "Wi-Fi", "Desayuno Americano", "TV HD"],
        "contacto": "447-515-3141",
        "imagen": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500&auto=format&fit=crop&q=60"
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', hoteles=HOTELES)

if __name__ == '__main__':
    app.run(debug=True)
