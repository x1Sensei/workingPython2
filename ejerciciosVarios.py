# #Ejercicio con 


# while True:
#     number = int(input("Ingrese un numero: "))

#     if number % 2 == 0:
#         print(f"El numero {number} es par")

#     else:
#         print(f"El numero {number} es impar")

#     #sISTEMA DE LOGIN CON DOS VARIABLES UN USUARIO Y UNA CONTRASEÑA, SENCILLO

#     user = input("Ingrese su usuario: ")
#     password = input("Ingrese su contraseña: ")
#     if user == "jimmy" and password == "1234":
#         print("Accediste crack")
#         break
#     else:
#         print("Quien eres, identificate")


#Creamos una lista con 100 numeros y vamos a obteer la suma de esos 100 numeros, usando condicione simple
numbers = list(range(1, 101))
total_sum = 0
for num in numbers:
    total_sum += num
print(f"La suma de los primeros 100 numeros es: {total_sum}")

#Haremos un ejercicio bancario, donde el usuario va a hacer un deposito , un retiro y ver el saldo, de manera sencilla con condicional y algun choice

saldo = 0

while True:
    print("\n1. Depositar  2. Retirar  3. Ver saldo  4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        saldo += float(input("Cantidad a depositar: "))
    elif opcion == '2':
        retiro = float(input("Cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
        else:
            print("Saldo insuficiente")
    elif opcion == '3': 
        print("Saldo:", saldo)
    elif opcion == '4':
        break
    else:
        print("Opción inválida")
