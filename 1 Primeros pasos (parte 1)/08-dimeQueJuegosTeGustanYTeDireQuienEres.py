titulo = "Bienvenido al test sobre juegos"
print(titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Te gustan los Shooters?\n"
               "A: Odio\n"
               "B: Si\n"
               "C: Amo \n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("Pregunta 2: ¿Te gustan los juegos de estrategia? \n"
               "A: No \n"
               "B: Maso \n"
               "C: Amo \n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("Pregunta 3: ¿Te gustan los indies?\n"
               "A: Depende de cual\n"
               "B: Si\n"
               "C: Todos son indies en mi libreria\n")

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
    print("Resultado: Tenés gustos variados y encontrás la diversión probando cosas nuevas.\n"
          "Sos un inconformista que siempre busca un nuevo reto o nunca termina nada")
elif puntuacion >=15:
    print("Resultado: Ni mucho ni poco, sos como el común de los jugadores, selectivo y precavido.\n"
          "Preferís aprovechar ofertas a comprar un juego de lanzamiento")
else:
    print("Resultado: Te la pasás jugando un solo tipo de juego y de ahí no salís.\n"
          "Deberías soltar un poco y probar cosas nuevas, te prometo que hay joyas esperando a ser jugadas :)")

print("Tu puntuación es de:")
print(puntuacion)