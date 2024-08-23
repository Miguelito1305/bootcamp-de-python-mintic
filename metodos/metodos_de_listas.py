lista = list(["hola", "Miguel",1993,14,3,True])
# nos devuelve la longitud de la lista
cadena = "hola"
resultado = len(cadena)
#agregar un elemento a la lista
lista.append("4")
#agregando un elemento en una posicion especifiva
lista.insert(2,False)
#agregando varios elementos a la lista
lista.extend([ 2024])
#remover un elemento de la lista
#lista.remove("hola")
#remover el ultimo elemento de la lista
print(len(lista))
lista.pop(-1)
print(len(lista))
#remover un elemento de una posicion especifica
#lista.remove("hola")
#remover el ultimo elemento de la lista
#lista.sort()
print(lista)
elemento_encontrado = lista.index("4")
print(elemento_encontrado)