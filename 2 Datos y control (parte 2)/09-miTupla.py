#Tuplas
lista = [10,11,12,13,14,15]
miTupla = (1,2,3,4,5,6,7,8,9, lista)
miTupla2 = ("Perrito", "Perron", "Perruno", miTupla)
print(miTupla2)

colores = ("Rojo", "Amarillo", "Verde", "Azul", "Violeta")
uno, dos, tres, *cuatro = colores
print(uno)
print(dos)
print(tres)
print(cuatro)