#Calcula la edad de tu perro

print("¿Cuantos años tiene tu perro?")
edad = int(input())

multiplicacion = 7

while edad != 0:
    edadPerro = edad * multiplicacion
    print("La edad de tu perro en años perrunos es de: " + str(edadPerro))
    print("\n¿Quieres ingresar la edad de otro perro? O pulsa 0 para terminar")
    edad = int(input())
