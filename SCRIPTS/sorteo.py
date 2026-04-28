import pandas as pd
import random
import os

# --- 1. RUTAS ABSOLUTAS (Directo al grano) ---
# Usamos 'r' al principio para que Python entienda bien las barras invertidas \
RUTA_GENERAL = r'C:\Users\BRAYAN DUQUE\OneDrive\Documentos\SORTEO_PASOANCHO_PRESTIGIO\DATA\participantes_general.csv'
RUTA_ELITE = r'C:\Users\BRAYAN DUQUE\OneDrive\Documentos\SORTEO_PASOANCHO_PRESTIGIO\DATA\finalistas_elite.csv'

def cargar_datos(ruta):
    try:
        if not os.path.exists(ruta):
            print(f"❌ No se encontró el archivo en: {os.path.abspath(ruta)}")
            return []
        
        # Leemos desde la fila 2 (skiprows=1) hasta la 10 (nrows=9)
        # sep=None detecta automáticamente si usas coma o punto y coma
        df = pd.read_csv(ruta, skiprows=1, nrows=9, header=None, sep=None, engine='python')
        
        # Tomamos la columna A (índice 0) y limpiamos celdas vacías
        lista = df[0].dropna().tolist()
        return [str(n).strip() for n in lista if str(n).strip() != '']
    except Exception as e:
        print(f"❌ Error al leer {ruta}: {e}")
        return []

# --- 2. CARGA DE LISTAS ---
participantes_general = cargar_datos(RUTA_GENERAL)
participantes_elite = cargar_datos(RUTA_ELITE)

def realizar_sorteo(lista, nombre_sorteo):
    if not lista:
        print(f"\n⚠️ La lista de {nombre_sorteo} está vacía.")
        return
    
    print(f"\n--- {nombre_sorteo.upper()} ---")
    print(f"Participantes en tómbola: {lista}")
    input("Presiona ENTER para elegir ganador... 🎰")
    
    ganador = random.choice(lista)
    lista.remove(ganador) # Se elimina para que no repita premio
    
    print("\n" + "⭐" * 40)
    print(f"🏆 EL GANADOR ES: {ganador.upper()}")
    print("⭐" * 40)
    print(f"Quedan {len(lista)} personas para el próximo turno.")

# --- 3. MENÚ PRINCIPAL ---
while True:
    print("\n" + "="*40)
    print("   SORTEOS EL PRESTIGIO DE PASOANCHO")
    print("="*40)
    print(f"1. Sorteo GENERAL (Quedan: {len(participantes_general)})")
    print(f"2. Sorteo ÉLITE   (Quedan: {len(participantes_elite)})")
    print("3. Ver quiénes faltan por pasar")
    print("4. Salir")
    
    opcion = input("\n¿Qué sorteo quieres realizar primero?: ")
    
    if opcion == "1":
        realizar_sorteo(participantes_general, "Sorteo General")
    elif opcion == "2":
        realizar_sorteo(participantes_elite, "Sorteo Élite")
    elif opcion == "3":
        print(f"\nLista General: {participantes_general}")
        print(f"Lista Élite: {participantes_elite}")
    elif opcion == "4":
        print("Cerrando sistema. ¡Buena suerte!")
        break
    else:
        print("Opción no válida.")