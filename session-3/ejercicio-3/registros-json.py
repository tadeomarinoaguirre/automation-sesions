# Lista que contiene registros JSON.
    
registros = [
    {
        "Nombre": 'Tadeo',
        "Apellido": "Marino",
        "Edad": 23,
    },
    {
        "Nombre": 'Ju*an',
        "Apellido": "Perez",
        "Edad": 43,
    },
]

# 1. Almacenamos el 'Nombre' + 'Apellido' del primer registro en variables.

nombre1  = registros[0]["Nombre"]
apellido1 = registros[0]["Apellido"]

print(nombre1 + ", " + apellido1)

# 2. Almacenamos las Edades de ambos registros.

edad1  = registros[0]["Edad"]
edad2 = registros[1]["Edad"]

print(nombre1 + " tiene " + str(edad1) + " años.")

# 3. Eliminamos el '*' en el "Nombre" del segundo registro.

registros[1]["Nombre"] = registros[1]["Nombre"].replace('*', '') # podemos agregar un argumento mas para el caso que haya mas de uno indicar cuantos se reemplazarian.

nombre2 = registros[1]["Nombre"]

print(nombre2)