# Variables simples
nombre = "Jimmy"
edad = 21
altura = 1.75

# Tipos de datos comunes


numero = 10   # valor entero


precio = 19.99   # valor decimal


mensaje = "Hola, Python"  # valor cadena de texto

activo = True  # valor booleano


# Reasignacion de variables
x = 5
print(x)  # 5

x = "Esto es un texto ahora"
print(x)  #aqui se imprime el valor actual de la variable "x" --: Esto es un texto ahora

#OPeraciones con variables
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Suma:", suma)
print("División:", division)

# Concatenación de cadenas
nombre = "Jimmy"
apellido = "Izurieta"
edad = 21
altura = 1.75
color_favorito = "Azul"
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)
print(f"Me llamo {nombre} {apellido} y tengo {edad} años, mido {altura} metros y mi color favorito es {color_favorito}.")

#Listas
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # manzana
frutas.append("naranja")
print(frutas)  # ['manzana', 'banana', 'cereza', 'naranja']
frutas.remove("banana")
print(frutas)  # ['manzana', 'cereza', 'naranja']