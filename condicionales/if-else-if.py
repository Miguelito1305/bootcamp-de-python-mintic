ingreso_mensual = int(input("Ingresa tu ingreso mensual: "))

if ingreso_mensual <= 1000000:
    print("Estas bien economicamente en el mundo")
        
elif ingreso_mensual > 5000:
    print("Estas bien economicamente en Estados Unidos")    
    
elif ingreso_mensual > 2000:
    print("Estas bien economicamente en Canada")
    
elif ingreso_mensual > 90000:
    print("Estas bien economicamente en Europa")
    
else:
    print("No estas bien economicamente")