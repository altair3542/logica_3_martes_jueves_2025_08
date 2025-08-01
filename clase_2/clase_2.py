#Arreglos unidimensionales (vectores)

# Al finalizar esta sesión, los estudiantes serán capaces de:

# Inicializar arreglos unidimensionales (vectores) de forma literal y dinámica.

# Recorrer un vector utilizando for, while y funciones de orden superior como map.

# Aplicar operaciones comunes: inserción, eliminación y búsqueda lineal.

# Comprender la complejidad computacional básica de dichas operaciones.

# Resolver problemas prácticos manipulando vectores en Python.

# 2.1 ¿que es un arreglo unidimensional?
# un arreglo unidimensional es una estructura de datos que almacena una secuencia de elementos del mismo tipo logico. si bien, un arreglo puede contener todos los tipos de datos al tiempo, es una buena practica que el tipo sea igual para todos los elementos, es decir, un arreglo de arreglos, un arreglo numeros, de cadenas, de booleanos, etc.

# podemos inicializar los arreglos de dos formas.

# la asignacion estatica o literal:

numeros = [3, 5, 7, 9]

# Dinamica (por construccion en tiempo de ejecucion.)

n = 5
num = []

for i in range(n):
    valor = int(input(f"ingrese el valor {i + 1}: "))
    num.append(valor)
    print(num)



