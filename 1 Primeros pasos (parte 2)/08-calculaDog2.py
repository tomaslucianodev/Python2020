#Calcula la edad de tu perro

#Funciones
def calcularEdad(nombre, parametroEdad, genero):
    multiplica = 7
    edadPerro = parametroEdad * multiplica
    if genero == True:
        print('La edad de tu perra ' +nombre+ ' en años perrunos es: ' + str(edadPerro))
        if parametroEdad >= 10:
            print("Tu perra " +nombre+ " es grande ya")
        if parametroEdad <= 10:
            print("Tu perra " +nombre+ " es jovencita") 
    elif genero == False:
        print('La edad de tu perro ' +nombre+ ' en años perrunos es: ' + str(edadPerro))
        if parametroEdad >= 10:
            print("Tu perro " +nombre+ " está grande ya")
        if parametroEdad <= 10:
            print("Tu perro " +nombre+ " es jovencito")
    else:
        print('La edad de tu perre ' +nombre+ ' en años perrunos es: ' + str(edadPerro))
        if parametroEdad >= 10:
            print("Tu perre " +nombre+ " está grande ya")
        if parametroEdad <= 10:
            print("Tu perre " +nombre+ " es jovencite")
    return 

calcularEdad("Robert", 11, False)
calcularEdad("Pitu", 4, True)
calcularEdad("Amburguesito", 7, "")