import random

print("ADIVINAR NUMERO")
print("---------------")

ingresar_numero = int(input("Ingrese un numero del 1 al 10 "
                            "(aunque por poner podés poner el numero que quieras en realidad..): "))
numeros = random.randint(1, 10)

if ingresar_numero != numeros:
    print("Mejor suerte para la proxima")
else:
    print("Felicidades, ganaste!!")

if ingresar_numero > 10:
    print("Te pasaste de largo, es del 1 al 10")

if ingresar_numero < 1:
    print("Te quedaste corto, es del 1 al 10 :)")

if ingresar_numero == 69:
    print("Cochinx!!!")

if ingresar_numero == 666:
    print("¡¡EL NÚMERO DEL DIABLO!! Alejate, por favor.")

if ingresar_numero == -666:
    print("Elegiste el numero del mal pero en negativo, por lo tanto, sos doblemente malvado.")

print("El numero ganador era: {}".format(numeros))
