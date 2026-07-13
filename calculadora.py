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
    print("resultado: ", numero_1 / numero_2)
elif operador == "//":
    print("resultado: ", numero_1 // numero_2)
elif operador == "**":
    print("resultado: ", numero_1 ** numero_2)
elif operador == "%":
    print("resultado: ", numero_1 % numero_2)
    
else:
    print("valor invalido o operador faltante espere futuras actualizaciones")  

