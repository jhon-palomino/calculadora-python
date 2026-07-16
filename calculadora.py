repetir = "s"
while repetir == "s":
    numero_1 = int(input("ingrese primer valor:"))
    operador = input("ingrese el operador que dese")
    numero_2 = int(input("ingrese segundo valor:"))
    if operador == "+":
        print("resultado: ", numero_1 + numero_2)
    elif operador == "-":
        print("resultado: ", numero_1 - numero_2)
    elif operador == "*":
        print("resultado: ", numero_1 * numero_2)
    elif operador == "/":
        if numero_2 == 0:
            print("no se puede dividir un numero entre 0")
        else:
            print("resultado: ", numero_1 / numero_2)
    elif operador == "//":
        print("resultado: ", numero_1 // numero_2)
    elif operador == "**":
        print("resultado: ", numero_1 ** numero_2)
    elif operador == "%":
        print("resultado: ", numero_1 % numero_2)
    else:
        print("operador incorrecto : gracias por comprar Ecoin")
    repetir = input("si desea volver a usar la calculadora presione s y si no presione cualquier otra letra")
    
    

    


