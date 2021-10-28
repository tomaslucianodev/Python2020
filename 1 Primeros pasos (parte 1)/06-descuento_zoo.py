edad = int(input("¿Cuántos años tenés?: "))
tipo_de_carnet = input("¿Qué tipo de carnet tenés? "
                       "(E para Estudiante) / (P para pensionado) / (F para familia numerosa) (N para nada) : ")

if (edad <= 35 and edad >= 25 and tipo_de_carnet == "E") \
        or edad <= 10 \
        or (edad >= 65 and tipo_de_carnet ==  "P") \
        or (tipo_de_carnet == "F"):
    print("Se te aplica el descuento.")
else:
    print("No se te aplica el descuento.")
