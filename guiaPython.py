# guia_basica.py

# GUÍA BÁSICA DE PYTHON
# Variables, listas, operaciones



# 1. VARIABLES

nombre = "Jimmy"       # String
edad = 21              # Entero
altura = 1.75          # Decimal
activo = True          # Booleano

print("=== VARIABLES ===")
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}, Activo: {activo}")
print()


# 2. OPERACIONES

a, b = 10, 3

print("=== OPERACIONES ARITMÉTICAS ===")
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo (residuo): {a % b}")
print(f"Potencia: {a ** b}")
print()

print("=== OPERACIONES DE COMPARACIÓN ===")
print(f"{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print()

print("=== OPERACIONES LÓGICAS ===")
x, y = True, False
print(f"AND: {x and y}")
print(f"OR: {x or y}")
print(f"NOT x: {not x}")
print()


# 3. LISTAS

frutas = ["manzana", "banana", "cereza"]

print("=== LISTAS ===")
print("Lista completa:", frutas)
print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])

# Agregar y eliminar elementos
frutas.append("naranja")
print("Después de agregar naranja:", frutas)

frutas.remove("banana")
print("Después de eliminar banana:", frutas)

# Recorriendo la lista
print("Recorriendo la lista:")
for fruta in frutas:
    print("-", fruta)
print()

# Crear lista con numeros del 1 al 10
numeros = list(range(1, 11))
print("Lista de números del 1 al 10:", numeros)


# 4. DICCIONARIOS

persona = {
    "nombre": "Alejandro",
    "edad": 22,
    "ciudad": "Santo Domingo"
}

print("=== DICCIONARIOS ===")
print("Diccionario completo:", persona)
print("Nombre:", persona["nombre"])
print("Edad:", persona.get("edad"))

persona["profesion"] = "Estudiante"
print("Diccionario actualizado:", persona)
print()
del persona["ciudad"]
print("Después de eliminar ciudad:", persona)
print()

del persona["edad"]
print("Después de eliminar edad:", persona)


persona["edad"] = 23
persona["ciudad"] = "Santiago"
persona["profesion"] = "Ingeniero"
print("Diccionario modificado:", persona)
print()

for item in persona:
    feature = persona[item]
    print(f"{item}: {persona[item]}")
print()

# 5. EJEMPLO PRÁCTICO

# Gestion, lista de tareas

print("=== EJEMPLO PRÁCTICO: GESTOR DE TAREAS ===")

tareas = []

# Agregar tareas
tareas.append("Estudiar Python")
tareas.append("Hacer ejercicio")
tareas.append("Leer un libro")

print("Tareas actuales:", tareas)

# Marcar una tarea como hecha (eliminarla)
tareas.remove("Hacer ejercicio")
print("Tareas después de completar una:", tareas)

# Mostrar todas las tareas pendientes
print("Tareas pendientes:")
for t in tareas:
    print("-", t)


containertuple = ("Jimmy", 21, 1.75, True)

print(containertuple[0])
print(containertuple[1])
print(containertuple[2])
print(containertuple[3])


# Otro ejemplo de Diccionario

mydictionary=dict()
mydictionary['humans']=2
mydictionary['cats']=3
mydictionary['dogs']=1
mydictionary['spider']=8


for animal in mydictionary:
    data=mydictionary[animal]
    print('the %s has %d' % (animal, data))


# LOOPS

counter=0
while counter < 5:
    print('counter is %d' % counter)
    counter += 1
name=input('Enter your name: ')
print('Hello %s' % name)



# Lista de 100 numeros y se seleccionan los pares 
numbers=list(range(1,101))
even_numbers=[]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# ahora haremos lo mismo de los pares pero en una sola linea
even_numbers2=[number for number in range(1,101) if number % 2 == 0]
print(even_numbers2)

# Definir funciones, devolviendo un valor
def saludar(nombre):
    return 'Hola %s' % nombre

tmp= saludar('Jimmy')
print(tmp)  

# Serie de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci(10)) 

# Lista con 10 elementos numericos, para identificar el numero mayor con for
numeros = [34, 12, 5, 67, 23, 89, 1, 45, 78, 56]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print("El número mayor es:", mayor)


def greetings(name="friend"):
    print(f"Hello, {name}!")
    return name
greetings("Jimmy")


# Calculadora con dos numeros con menu, con while

def calculator():
    while True:
        n1 = float(input("Ingresa el primer numero: "))
        n2 = float(input("Ingresa el segundo numero: "))

        print("Selecciona la operacion:")
        print("1. Sumar")
        print("2. Restar")
        

        choice = input("Ingresa tu opcion (1-3): ")
        if choice == '1':
            print(f"{n1} + {n2} = {n1 + n2}")
        elif choice == '2':
            print(f"{n1} - {n2} = {n1 - n2}")
        else:
            print("Opcion invalida.")

            return calculator()
