# Lista de nombres: 
# Tenemos una lista de IDs de usuarios que comienzan con una comilla (") y queremos eliminar esa comilla.

# Lista
userIDs = [
    "#Tadeo",
    "Luis#",
    "#Pedro",
    "#Isidro",
    "#Juan",
]

# Accedemos a los elementos por indexación.

userIDs[0] = userIDs[0].replace('#', "")
userIDs[1] = userIDs[1].replace('#', "")

# Imprime la lista 'userIDs' para verificar los cambios.
print(userIDs)

# Bucle for para imprimir cada elemento de la lista en una línea separada
#for user in userIDs:
    # print(user)