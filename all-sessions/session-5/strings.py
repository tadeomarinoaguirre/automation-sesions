
# Strings en Python
# --------------------------

# Los strings son secuencias de caracteres y se definen utilizando comillas simples o dobles.
# Por ejemplo, aquí tenemos un string que representa un saludo:
mi_string = "¡Hola, mundo!"
print(mi_string)

# Podemos acceder a cada carácter en un string utilizando su índice. Los índices en Python comienzan en 0.
# Por ejemplo, si queremos acceder al primer carácter de nuestro string de saludo, haríamos lo siguiente:
print(mi_string[0])  # Salida: ¡

# Python también admite la indexación negativa. Esto significa que el índice -1 se refiere al último elemento, -2 al penúltimo y así sucesivamente.
# Por ejemplo, si queremos acceder al último carácter de nuestro string de saludo, haríamos lo siguiente:
print(mi_string[-1])  # Salida: !

# A diferencia de las listas, los strings en Python son inmutables. Esto significa que no puedes cambiar un carácter de un string una vez que se ha definido.
# Si intentas hacerlo, Python te dará un error. Por ejemplo:
# mi_string[0] = 'h'  # Esto dará un error

# Podemos concatenar strings con el operador +.
saludo = "¡Hola, "
nombre = "mundo!"
mi_string = saludo + nombre
print(mi_string)  # Salida: ¡Hola, mundo!

# Python proporciona una serie de métodos útiles que puedes usar con strings.
# Los métodos upper() y lower() devuelven una copia del string original en mayúsculas y minúsculas respectivamente.
print(mi_string.upper())  # Salida: ¡HOLA, MUNDO!
print(mi_string.lower())  # Salida: ¡hola, mundo!

# El método split() divide un string en una lista donde cada palabra es un elemento de la lista.
palabras = mi_string.split()
print(palabras)  # Salida: ['¡Hola,', 'mundo!']

# El método join() toma todos los elementos de una lista y los une en un string. El string del que se llama el método se utiliza como separador.
nuevo_string = ' '.join(palabras)
print(nuevo_string)  # Salida: ¡Hola, mundo!