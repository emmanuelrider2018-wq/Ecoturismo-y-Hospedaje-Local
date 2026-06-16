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

if __name__ == '__main__':
    app.run(debug=True)
