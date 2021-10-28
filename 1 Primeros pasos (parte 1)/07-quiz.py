titulo = "Bienvenido al test sobre el queso"
print(titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Qué hacés cuando ves una tabla de queso?\n"
               "A: Salgo corriendo\n"
               "B: Pruebo uno de los quesos\n"
               "C: Me la devoro \n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("Pregunta 2: ¿Cómo te gusta la hamburguesa? \n"
               "A: Sin queso \n"
               "B: Con queso \n"
               "C: Pan y queso \n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
               "A: Si\n"
               "B: A veces\n"
               "C: No\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

if puntuacion >=25:
    print("Resultado: Felicidades, sos fan de los quesos")
elif puntuacion >=15:
    print("Resultado: Te gusta el queso")
else:
    print("Resultado: Odias el queso")

print("Tu puntuación es de:")
print(puntuacion)