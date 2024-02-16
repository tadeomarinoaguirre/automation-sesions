
# Listas en Python
# --------------------------

# Las listas en Python son colecciones ordenadas de elementos. Estos elementos pueden ser de cualquier tipo y no necesariamente del mismo tipo.
# Definimos una lista colocando una serie de elementos separados por comas entre corchetes [].
# Por ejemplo, aquí tenemos una lista de frutas:
mi_lista = ['manzana', 'banana', 'cereza']
print(mi_lista)

# Podemos acceder a cualquier elemento de la lista utilizando su índice. Los índices en Python comienzan en 0.
# Por ejemplo, si queremos acceder al primer elemento de nuestra lista de frutas, haríamos lo siguiente:
print(mi_lista[0])  # Salida: 'manzana'

# Las listas son mutables, lo que significa que puedes cambiar sus elementos.
# Por ejemplo, si queremos cambiar 'banana' por 'naranja' en nuestra lista, haríamos lo siguiente:
mi_lista[1] = 'naranja'
print(mi_lista)  # Salida: ['manzana', 'naranja', 'cereza']

# Podemos añadir elementos al final de la lista con el método append().
# Por ejemplo, si queremos añadir 'kiwi' a nuestra lista, haríamos lo siguiente:
mi_lista.append('kiwi')
print(mi_lista)  # Salida: ['manzana', 'naranja', 'cereza', 'kiwi']

# Podemos eliminar elementos de la lista con el método remove().
# Por ejemplo, si queremos eliminar 'naranja' de nuestra lista, haríamos lo siguiente:
mi_lista.remove('naranja')
print(mi_lista)  # Salida: ['manzana', 'cereza', 'kiwi']

# Podemos obtener el número de elementos en la lista con la función len().
# Por ejemplo, si queremos saber cuántos elementos hay en nuestra lista, haríamos lo siguiente:
print(len(mi_lista))  # Salida: 3