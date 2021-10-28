
print("Ingrese el primer numero para sumar: ")
numerito = int(input())
total = 0
listaDeNumeros = []

while numerito != 0:
    listaDeNumeros.append(numerito)
    total = total + numerito
    print("Ingrese otro numero para sumar o 0 para terminar")
    numerito = int(input())
print("La suma total es de: " +str(total))
print("\nLos numeros sumados fueron: ")
print(listaDeNumeros)