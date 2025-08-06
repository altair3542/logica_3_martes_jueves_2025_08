# clase 3 Metodos de ordenación.

# al finalizar esta sesion, los estudiantes sera capaces de:

# Compender el funcionamiento detallado de los algoritmos de ordenamiento (burbuja e insercion)

# comparar su rendimiento en distintos casos de ejecucion

# implementar estos en algoritmos en python

# aplcarlos a valores numericos y cadenas

# analizar la cantidad de comparaciones e intercabios realizados.

# Ordenacion por Burbuja.

# 🧠 principio...
# Compara pares de elementos adyacentes
# si estan en un orden incorrecto, los intercambia
# se repite el proceso hasta que la lista este ordenada.

# ⚡ Optimización: Flag de intercambio
# Si en una pasada no se hizo ningún swap, entonces la lista ya está ordenada → se puede detener antes de tiempo.

# 🪜 Algoritmo de Inserción

# 🧠 principio...
# arranca en el segundo elemento
# lo compara con la porcion dela lista a la izquierda
# lo inserta en la posicion correcta desplazando los mayores a la derecha.

# comparativa entre burbuja e insercion.

# ambos son igual de estables
# se hacen mas cambios en burbuja que en insercion para ordenar.
# burbuja es mas ineficiente que insercion
# burbuja es mas para ejercicios didacticos que inserciones en tiempo real.

# ordenamiento por burbuja.

numeros = [5, 2, 9, 1, 5, 6]

# print('orden por burbuja, con ordenamiento paso a paso')
# #ciclo for para inicializar el orden de los numeros, se toma la longitud del arreglo y se inserta un ciclo interior para continuar con el ordenamiento
# for i in range(len(numeros)):
#     #se pone otro ciclo que es el que va a contar los numeros del par que se va a a evaluar:
#     for j in range(len(numeros) - 1 - i):
#         print(f'comparando {numeros[j]} y {numeros[j+1]}')
#         # vamos a validar cual es mayor.
#         if numeros[j] > numeros[j+1]:
#             print(f'intercambiando {numeros[j]} y {numeros[j+1]}')
#             numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
#         print(f'estado general {numeros}')
#     print("-----")

