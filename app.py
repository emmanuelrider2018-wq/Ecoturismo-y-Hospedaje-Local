from flask import Flask, render_template

app = Flask(__name__)

HOTELES = [
    {
        "id": 1,
        "nombre": "Hotel Plaza y Sol",
        "direccion": "Fray Alonso de la Veracruz #2, Centro Histórico",
        "descripcion": "Hermoso hotel de arquitectura colonial ubicado en el corazón del pueblo mágico. Cuenta con vistas espectaculares a la Parroquia de San Pedro y San Pablo.",
        "precio": "$1,200 MXN",
        "servicios": ["Wi-Fi Gratis", "Estacionamiento", "Agua Caliente", "TV por Cable"],
        "contacto": "447-123-4567"
    },
    {
        "id": 2,
        "nombre": "Cabañas Quinta La Huerta",
        "direccion": "Camino a la Presa del Brockman Km 1.5",
        "descripcion": "Rodeadas de un entorno boscoso inigualable, perfectas para el ecoturismo y un descanso reparador cerca de la hermosa Presa del Brockman.",
        "precio": "$1,800 MXN",
        "servicios": ["Chimenea", "Área de Fogatas", "Pet Friendly", "Terraza Privada"],
        "contacto": "447-987-6543"
    },
    {
        "id": 3,
        "nombre": "Hotel Rinconcito Artesanal",
        "direccion": "Juárez #45, Barrio de San Juan",
        "descripcion": "Un espacio acogedor decorado con las tradicionales esferas navideñas y la cantera rosa emblemática de nuestra región.",
        "precio": "$950 MXN",
        "servicios": ["Wi-Fi Gratis", "Desayuno Incluido", "Atención Turística"],
        "contacto": "447-456-7890"
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', hoteles=HOTELES)

if __name__ == '__main__':
    app.run(debug=True)
