#Calcula la edad de tu perro

edad = int(input("¿Cuántos años tiene tu perro?\n"))


#Funciones
def calcularEdad():
    multiplica = 7
    edadPerro = edad * multiplica
    return print('La edad de tu perro en años perrunos es: ' + str(edadPerro))
calcularEdad()