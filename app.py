from flask import Flask, jsonify, render_template
import pandas as pd
import random
import os
from dotenv import load_dotenv
from flask_cors import CORS

# 1. CARGA DE CONFIGURACIÓN
load_dotenv()
app = Flask(__name__)
CORS(app)

RUTA_GENERAL = os.getenv("RUTA_GENERAL")
RUTA_ELITE = os.getenv("RUTA_ELITE")

def cargar_datos(ruta):
    try:
        if not ruta or not os.path.exists(ruta):
            return []
        df = pd.read_csv(ruta, skiprows=1, nrows=1000, header=None, sep=None, engine='python')
        lista = df[0].dropna().tolist()
        return [str(n).strip().upper() for n in lista if str(n).strip() != '']
    except Exception as e:
        print(f"Error al cargar: {e}")
        return []

# 2. LISTAS DE PARTICIPANTES
participantes = {
    "general": cargar_datos(RUTA_GENERAL),
    "elite": cargar_datos(RUTA_ELITE)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sortear/<tipo>')
def sortear(tipo):
    lista = participantes.get(tipo)
    if not lista:
        return jsonify({"error": "No hay participantes disponibles"}), 400
    
    ganador = random.choice(lista)
    lista.remove(ganador) # Blindaje: No repite
    
    return jsonify({
        "ganador": ganador,
        "restantes": len(lista),
        "foto": f"{ganador}.jpg"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)