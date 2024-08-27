numbers = {1:"uno", 2:"dos", 3:"tres"} #en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre":"Miguel",
"apellidos":"Gonzalez","estatura":1.78,"esta feliz":True}
print(information)
del information["apellidos"]
print(information)
claves = information.keys()
print(claves)
values = information.values()
print(values)
items = information.items()
print(items)
contacts = {"Miguel" :{"apellidos":"Gonzalez",
                       "estatura":1.78,
                       "edad":30,
                       "esta feliz":True,
                       "Telefono":"123456789",
                       "Signo zodiacal":"Leo",
                       "Serie favorita":"Naruto",
                       "Cancion favorita":"Huracan-Gundad Merced",
                       "Comida favorita":"Milanesa",
                       "lugar sonñado vacaciones":"Costa Rica",
                       "Habilidad secreta":"Cantar",
                       "pasa tiempo":"Dormir",
                       "heroe o persona que admiras":"Toreto",
                       "libro que mas me ha inpactado":"El Quijote",
                       "cena con alguien":"La baldiri",
                       "super poder":"la jenquidama",
                       "qie logro personal te enorgullese":"aprender a programar"},
            "Andy" :{"apellidos":"Carabali",
                       "estatura":1.58,
                       "edad":5,
                       "esta feliz":True,
                       "Telefono":"123456789",
                       "Signo zodiacal":"Leo",
                       "Serie favorita":"Tayo",
                       "Cancion favorita":"La vaca lola",
                       "Comida favorita":"Masitas de queso",
                       "lugar sonñado vacaciones":"Miami",
                       "Habilidad secreta":"Jugar",
                       "pasa tiempo":"Dormir",
                       "heroe o persona que admiras":"Mi papa",
                       "libro que mas me ha inpactado":"****",
                       "cena con alguien":"Papa y Mama",
                       "super poder":"tener todo los juguetes",
                       "que logro personal te enorgullese":"ser un buen Hijo"},}
print (contacts)

