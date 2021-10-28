print("Ingrese el primer numero para sumar: ")
numerito = int(input())
total = 0

while numerito != 0:
    total = total + numerito
    print("Ingrese otro numero para sumar o 0 para terminar")
    numerito = int(input())
print("La suma total es de: " +str(total))