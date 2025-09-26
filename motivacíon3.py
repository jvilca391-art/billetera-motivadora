import random
import os

# Funciones
def saludo_motivador(nombre):
    saludos = [
        f"👋 ¡Bienvenido, {nombre}! Hoy es un gran día para cuidar tu plata 💸",
        f"🐊 ¡Qué onda, {nombre}! Acá arranca tu camino financiero motivado 🔥",
        f"🦦 ¡Nutrias unidas jamás serán vencidas, {nombre}! Vamos a ahorrar juntos ✊",
        f"😎 ¡Crack {nombre}! Aunque no tengas un peso, tenés actitud, y eso vale oro 💪",
    ]
    print(random.choice(saludos))

def pregunta_estado(nombre):
    estado = input(f"{nombre}, ¿cómo estás hoy? (bien/mal): ").lower()
    if estado == "bien":
        print(f"¡Genial, {nombre}! 💪 Vamos a aprovechar este buen día para tus finanzas.")
    elif estado == "mal":
        print(f"Tranqui, {nombre}, ¡mañana será un mejor día! 🐊💸")
    else:
        print(f"No entendí, {nombre} 😅. Pero igual vamos a cuidar tu plata.")

def leer_ahorros():
    if os.path.exists("ahorros.txt"):
        with open("ahorros.txt", "r") as f:
            try:
                return float(f.read())
            except ValueError:
                return 0.0
    else:
        return 0.0

def guardar_ahorros(monto):
    with open("ahorros.txt", "w") as f:
        f.write(str(monto))

def ahorrar_hoy(nombre, total_ahorros):
    while True:
        try:
            hoy = float(input(f"{nombre}, ¿cuánto querés ahorrar hoy? (en $ARS): $"))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    total_ahorros += hoy
    print(f"¡Genial, {nombre}! Te felicito, hoy pudiste ahorrar ${hoy:,.2f} ARS. "
          f"Tu total acumulado ahora es ${total_ahorros:,.2f} ARS 🦦💸")
    guardar_ahorros(total_ahorros)
    return total_ahorros

def pregunta_viaje_y_ahorro(nombre, total_ahorros):
    while True:
        viaje = input(f"{nombre}, ¿tienes un viaje pensado? (sí/no): ").strip().lower()
        if viaje == "sí":
            lugar = input("¡Genial! ¿A dónde sería tu viaje?: ").strip()
            print(f"¡Qué buena, {nombre}! 💼 Planificar tu viaje a {lugar} también es una gran motivación para ahorrar 🦦")
            print(f"Genial, {nombre}! A continuación te ayudaremos a ahorrar para cumplir ese viaje 💸")
            total_ahorros = ahorrar_hoy(nombre, total_ahorros)
            break
        elif viaje == "no":
            print(f"No hay drama, {nombre} 😎 Ahorrar para el futuro también es un viaje 💸")
            total_ahorros = ahorrar_hoy(nombre, total_ahorros)
            break
        else:
            print("Por favor, ingresa 'sí' o 'no'.")
    return total_ahorros

# Programa principal
nombre = input("Ingrese su nombre: ")
saludo_motivador(nombre)
pregunta_estado(nombre)
ahorros_totales = leer_ahorros()
ahorros_totales = pregunta_viaje_y_ahorro(nombre, ahorros_totales)
