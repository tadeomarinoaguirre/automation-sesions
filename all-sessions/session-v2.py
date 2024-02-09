# Variables

# Una variable es un nombre que se refiere a un valor.
# Aquí, 'nombre' y 'año' son variables que se refieren a los valores "Tadeo" y 2024, respectivamente.
nombre = "Tadeo"
año = 2024

# Concatenación de variables

# La concatenación de variables es la unión de dos o más cadenas de texto.
# Aquí, estamos pidiendo al usuario que ingrese su nombre y luego lo usamos para imprimir un mensaje de bienvenida.
userName = input("Ingresa tu nombre: ")
bienvenida = "¡Hola mundo, mi nombre es "
print(bienvenida + userName + "!")

# Listas

# Una lista es una colección de elementos.
# Aquí, estamos creando una lista de frutas y luego le pedimos al usuario que agregue una nueva fruta a la lista.
frutas = ["Manzana", "Pera", "Naranja"]
nuevaFruta = input("Ingrese una nueva fruta: ")
frutas.append(nuevaFruta)
print(frutas)

# Condicionales

# Los condicionales nos permiten tomar decisiones en nuestro código.
# Aquí, estamos pidiendo al usuario que ingrese su altura y luego usamos una declaración condicional para imprimir un mensaje basado en su altura.
altura = int(input("Ingresa tu altura: "))

if altura >= 180:
    print("Sos una persona alta!")
else:
    print("Sos una persona baja!")

# Funciones
    
# Una función es un bloque de código que sólo se ejecuta cuando es llamado.
#Aquí, estamos definiendo una función que toma la altura como parámetro y luego imprime un mensaje basado en esa altura.
def mostrarAltura(altura):
    if altura >= 180:
        print("Sos una persona alta!")
    else:
        print("Sos una persona baja!")

# Llamada a la función
# Aquí, estamos llamando a la función 'mostrarAltura' y pasándole la altura que el usuario ingresó anteriormente.
mostrarAltura(altura)
