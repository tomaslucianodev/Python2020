#Calcula la edad de tu perro

#Funciones
def calcularEdad(nombre, parametroEdad):
    multiplica = 7
    edadPerro = parametroEdad * multiplica
    return print('La edad de tu perro ' +nombre+ ' en años perrunos es: ' + str(edadPerro))

calcularEdad("Robert", 3)

calcularEdad("Pitu", 4)

calcularEdad(str(input("¿Cómo se llama tu perro?\n")), int(input("¿Cuántos años tiene tu perro?\n")))