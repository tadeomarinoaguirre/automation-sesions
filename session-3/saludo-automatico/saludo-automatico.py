# Importamos el módulo datetime
from datetime import datetime

def saludo_automatico():
    # Obtenemos la hora actual
    hora_actual = datetime.now().hour

    # Dependiendo de la hora del día, seleccionamos un saludo apropiado
    if 5 <= hora_actual < 12:
        saludo = "¡Buenos días!"
    elif 12 <= hora_actual < 18:
        saludo = "¡Buenas tardes!"
    else:
        saludo = "¡Buenas noches!"

    # Imprimimos el saludo
    print(saludo)

# Llamamos a la función
saludo_automatico()