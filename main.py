#Par o impar?      Xavier Martin Rodriguez  27/10/2021

#Introducimos un número
x = int(input("¿En que número estás pensando?"))

#condicion (if/else) para comprobar si el resto de dividir por 2 es 0
if (x % 2) == 0:
    print(20*"*")
    print("*",16*" ","*" )
    print("*", 3*" ", "Es Par", 5*" ", "*")
    print("*", 16 * " ", "*")
    print(20 * "*")
else:
    print(20 * "*")
    print("*", 16 * " ", "*")
    print("*", 3 * " ", "Es Impar", 3* " ", "*")
    print("*", 16 * " ", "*")
    print(20 * "*")

print("Gracias por participar")