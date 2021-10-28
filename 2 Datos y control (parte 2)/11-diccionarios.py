#Diccionarios

diccionario = {"edad": 15, "nombre": "Azul", "apellido": "Ariste"}
#diccionario2 = dict()

print(diccionario)

#Creamos diccionario vacio
dic = {}
#Asignamos valores al diccionario
dic["Nombre"] = "Tomas"
dic["Apellido"] = "Lopez"
#Obtenemos un valor del diccionario
valor = dic["Apellido"]
#Modificar valor o crearlo
dic["Apellido"] = "Sosa"
print("Telefono" in dic)
print(dic)

#if "Telefono" in dic :
#    print(dic["Apellido"])
#else:  
#    print("Este valor no existe") 

#Metodo GET
print(dic.get("Telefono", "Este valor no es encontrado"))
print(dic.setdefault("Telefono", "22358216558"))
print(dic.setdefault("Apellido", "22358216558"))

#ELIMINAR ELEMENTOS
#del dic["Nombre"]
#dic.pop("Nombre")
#dic = {}
dic.clear()
print(dic)