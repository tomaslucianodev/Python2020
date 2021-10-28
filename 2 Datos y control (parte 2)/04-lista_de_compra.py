print("Lista de la compra\n")

lista = []
input_de_usuario = None

while True:
    input_de_usuario = input("¿Que desea comprar? [Q] para salir \n")
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista:
        print("{} ya está en la lista ".format(input_de_usuario))
    else:
        if input("¿Seguro que quieres añadir ese elemento a la lista? [S/N] ".format(input_de_usuario)) == "S":
            lista.append(input_de_usuario)
print("Su lista de compra es: \n")
print(lista)