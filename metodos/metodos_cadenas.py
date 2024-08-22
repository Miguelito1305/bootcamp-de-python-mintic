cadena1 = "HolasoyMiguel"
cadena2 = "Estoy aprendiendo python"
#print(dir(cadena1))

resultado = dir(cadena1.lower())
print(resultado)

primera_letra_mayuscula = cadena1.capitalize()
print(primera_letra_mayuscula)

busqueda_find = cadena1.find("l")
print(busqueda_find)

busqueda_index = cadena1.index("a")
print(busqueda_index)

es_numerica = cadena1.isnumeric()
print(es_numerica)

es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

contar_coincidencias = cadena1.count("l")
print(contar_coincidencias)

contar_caracteres = len(cadena1)
print(contar_caracteres)

empienza_con = cadena1.startswith("H")
print(empienza_con)

termina_con = cadena1.endswith("j")
print(termina_con)

cadena_nueva = cadena1.replace("Miguel", "Miguelito")
print(cadena_nueva)

cadena_separada = cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])