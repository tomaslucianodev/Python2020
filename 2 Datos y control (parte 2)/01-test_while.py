respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿Que opcion prefieres? [A, B o C]:")

if respuesta == "A":
    print("Has elegido bien")

elif respuesta == "B":
    print("Podrias haber elegido mejor")

elif respuesta == "C":
    print("Elegiste mal")

else:
    print("No me has dado una respuesta clara")