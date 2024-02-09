# Variables y operaciones matemáticas
# Vamos a calcular el año en que una persona cumplirá 100 años
#nombre = input("Ingresa tu nombre: ")
#edad = int(input("Ingresa tu edad: "))
#año_actual = 2024
#año_100 = año_actual + (100 - edad)
#print(nombre + ", cumplirás 100 años en el año " + str(año_100))

# Concatenación de variables y control de flujo
# Automatización de saludos dependiendo de la hora del día

from datetime import datetime

hora_actual = int(12-0)
saludo = "¡Buenos días!" if 5 <= hora_actual < 12 else "¡Buenas tardes!" if 12 <= hora_actual < 18 else "¡Buenas noches!"
print(saludo)