# el primer tipo de datos compuesto que veremos sera la lista

lista = ["miguel carabali", "Estudiante", True, 1.74]
print(lista)
lista[3]= "Macarabali"
print(lista[3])

tupla = ("miguel carabali", "Estudiante", True, 1.74)
print(tupla[1])


# tuplas no se pueden modificar
#tupla[1]= "tenomig"
#print(tupla[1])

#creando un conjunto o set
conjunto = {"miguel carabali", "Estudiante", True, 1.74,1.74}    
print

# Creando un diccionario o diccionario
diccionario = {
    "nombre": "miguel ",
    "apellido": "carabali",
    "estudiante": True,
    "estatura": 1.74
}

print(diccionario["nombre"])
print(diccionario["apellido"])
print (diccionario["estatura"])