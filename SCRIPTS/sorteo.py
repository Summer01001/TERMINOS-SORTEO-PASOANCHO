import pandas as pd
import random
import time

def sorteo_prestigio():
    print("\n==============================================")
    print("   BIENVENIDO AL SORTEO - EL PRESTIGIO")
    print("==============================================")
    print("1. Sortear 3er Lugar ($100.000)")
    print("2. Sortear 2do Lugar ($200.000)")
    print("3. Sortear 1er Lugar ($300.000) - ELITE")
    
    opcion = input("\nSeleccione el sorteo (1, 2 o 3): ")
    
    # IMPORTANTE: Aquí le decimos al programa dónde buscar los archivos
    archivo = "DATA/participantes_general.csv" if opcion in ['1', '2'] else "DATA/finalistas_elite.csv"
    
    try:
        df = pd.read_csv(archivo)
        participantes = df['Nombre'].tolist()
        
        print(f"\nCargando {len(participantes)} participantes...")
        time.sleep(2)
        print("¡Revolviendo la tómbola!")
        time.sleep(2)
        
        ganador = random.choice(participantes)
        print("\n" + "*"*35)
        print(f"🏆 ¡EL GANADOR ES: {ganador.upper()}! 🏆")
        print("*"*35 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: No se encontró el archivo. Asegúrate de estar en la carpeta principal.")

if__name__=="__main__":
    sorteo_prestigio()