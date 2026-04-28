import pandas as pd
import random
import time
import os

# Configuración de rutas (Saliendo de 'script' hacia 'data')
RUTA_GENERAL = os.path.join('..', 'data', 'participantes_general.csv')
RUTA_ELITE = os.path.join('..', 'data', 'finalistas_elite.csv')

def cargar_nombres(ruta, rango_inicio, rango_fin):
    try:
        # Leemos el CSV, saltamos las primeras 5 filas (empieza en la 6)
        # El rango A6-A10 en Python se traduce como filas 0 a 4 después del salto
        df = pd.read_csv(ruta, skiprows=5, header=None, sep=';', names=['NOMBRE', 'CEDULA', 'CONTACTO', 'LINK', 'SEDE', 'CUMPLE'])
        
        # Tomamos solo el rango que pediste (A6 a A10)
        # En pandas, .iloc[0:5] toma las primeras 5 filas de la data cargada
        nombres = df['NOMBRE'].iloc[0:5].tolist()
        return [n for n in nombres if str(n) != 'nan'] # Limpiamos celdas vacías
    except Exception as e:
        print(f"Error cargando archivo: {e}")
        return []

def realizar_sorteo(lista, premio):
    print(f"\n--- INICIANDO SORTEO PARA: {premio} ---")
    print("Cargando participantes...")
    time.sleep(1)
    
    # Efecto de animación "itinerante"
    for _ in range(10):
        print(f"Buscando... {random.choice(lista)}", end="\r")
        time.sleep(0.1)
    
    ganador = random.choice(lista)
    print(f"\n¡GANADOR(A): {ganador.upper()}! 🎉")
    lista.remove(ganador) # Eliminamos al ganador para que no repita
    return ganador

def menu():
    # Cargamos las listas iniciales
    lista_general = cargar_nombres(RUTA_GENERAL, 6, 10)
    lista_elite = cargar_nombres(RUTA_ELITE, 6, 10)
    
    ganadores_historial = []

    while True:
        print("\n=== SISTEMA DE SORTEOS EL PRESTIGIO ===")
        print("1. Realizar 1er Sorteo (General)")
        print("2. Realizar 2do Sorteo (General - Sin ganador anterior)")
        print("3. Realizar 3er Sorteo (ELITE - Premio Mayor)")
        print("4. Ver lista de ganadores de hoy")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1' and lista_general:
            ganador = realizar_sorteo(lista_general, "Primer Premio")
            ganadores_historial.append(f"1er Premio: {ganador}")
        elif opcion == '2' and lista_general:
            ganador = realizar_sorteo(lista_general, "Segundo Premio")
            ganadores_historial.append(f"2do Premio: {ganador}")
        elif opcion == '3' and lista_elite:
            ganador = realizar_sorteo(lista_elite, "PREMIO MAYOR 300K")
            ganadores_historial.append(f"Premio Mayor: {ganador}")
        elif opcion == '4':
            print("\n--- HISTORIAL DE HOY ---")
            for g in ganadores_historial: print(g)
        elif opcion == '5':
            print("Cerrando sistema. ¡Buena suerte!")
            break
        else:
            print("Opción no válida o lista vacía.")

if _name_ == "_main_":
    menu()