from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANIO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate

    # Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola voltio! \n")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda trueno! \n")
        vida_squirtle -= 11

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...")
    os.system("cls")

    # Turno Squirtle
    print("Turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: \n")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje!")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de agua!")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja!")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada...")

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:  [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))

if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")
