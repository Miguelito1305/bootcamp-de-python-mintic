to_do =["Me levanto alas 6am",
        "fui la gym a 10am",
        "llegue a la iglesia",
        "desayune con mi mujer",
        "jugue con mi hijo",
        "estoy en clase de programacion"]

print(to_do)
numbers = [1,2,3,4,5,6,7,8,9,"diez"]
print(numbers)
print (type(numbers))
mix = ["uno",2,3,4,5,6,7,8,9,True,[1,2,3]]
print(mix)
print(len(mix))
print("primer elemento de la lista",mix[0])
print("segundo elemento de la lista",mix[1])
print("tercer elemento de la lista",mix[2])
print("cuarto elemento de la lista",mix[3])
print("ultimoelemento de la lista",mix[10])
print(mix[0:2])
print(mix[:2])
print(mix[2:-2])
print(mix[2:len(mix)])
mix.append(False)
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers=[1,2,100,90,45,3,4,5]
print(numbers)
print("mayor",max(numbers))
print("menor",min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)  
