lista = [11,12,13,14,15, 16, 17, 18, 19]
miTupla = (1,2,3,4,5,6,7,8,9, 10)

combineta = zip(miTupla, lista)
nuevaTupla = tuple(combineta)
print(nuevaTupla)

listaNueva = list(miTupla)
print(listaNueva)

nuevaTupla2 = tuple(lista)
print(nuevaTupla2)