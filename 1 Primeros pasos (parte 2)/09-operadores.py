#Operadores logicos
numero = 1
puerta = True

if numero == 4:
    print("El numero es igual a 4")

if numero != 3:
    print("El numero no es igual a 3")

if numero > 2:
    print("El numero es mayor a 2")

if numero >= 4:
    print("El numero es mayor o igual a 4")

#if numero <= 4 and numero > 2 and puerta == True:
#    print("El numero es menor o igual a 4, mayor a 2 y puerta es verdadero")
#else: 
#    print("No se cumplen todas las condiciones")

if numero <= 4 and numero > 2 or puerta == True:
    print("El numero es menor o igual a 4, mayor a 2 y puerta es verdadero")
else: 
    print("No se cumplen todas las condiciones")