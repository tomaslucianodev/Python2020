print("Conversor de divisas \n")

conversion = 0

opcion = input("¿Qué operación querés realizar? \n"
               "A: Peso a Dolar \n"
               "B: Dolar a Peso \n"
               "C: Peso a Euro\n"
               "D: Euro a Peso\n")

if opcion == "A":
    conversion = float(input("Ingrese el valor que desea calcular: \n"))
    conversion = conversion / 150
elif opcion == "B":
    conversion = float(input("Ingrese el valor que desea calcular: \n"))
    conversion = conversion * 150
elif opcion == "C":
    conversion = float(input("Ingrese el valor que desea calcular: \n"))
    conversion = conversion / 112
elif opcion == "D":
    conversion = float(input("Ingrese el valor que desea calcular: \n"))
    conversion = conversion * 112
else:
    print("Las opciones posibles son A, B, C o D")
    exit()

print("Su conversión es:")
print(conversion)