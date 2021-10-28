print("En este test vamos a seleccionar el celular que se adecue a tus necesidades \n")

opcion = input("A: Android \n"
               "B: IOS \n")

if opcion == "A":
    presupuesto = input("1: Estoy corto de presupuesto \n"
          "2: Tengo plata para gastar en un buen celular\n")
    if presupuesto == "1":
        print("Android chino (Xiaomi o Realme) U$D100")
    else:
        print("¿Te importa la cámara?")
        caracteristicas = input("1: Sí, me gusta que saque buenas fotos \n"
              "2: No tanto, con que me sirva para FB o IG estoy hecho \n")
        if caracteristicas == "1":
            print("Google Pixel o Samsung Galaxy")
        else:
            print("Android calidad-precio (Xiaomi, Motorola o Samsung)")
elif opcion == "B":
    presupuesto = input("1: Estoy corto de presupuesto \n"
                        "2: Tengo plata para gastar en un buen iPhone \n")
    if presupuesto == "1":
        print("iPhone usado o antiguo \n"
              "Usado (iPhone 11, 11 Pro, 11 Pro MAX, 12 mini, 12, 12 Pro o 12 Pro MAX) \n"
              "Antiguo (6, 7, 8, X, XS o XR)")
    elif presupuesto == "2":
        print("La línea más reciente (2021: iPhone 12)")