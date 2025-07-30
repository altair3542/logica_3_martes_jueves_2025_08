# Estructrturas de datos y definicion de arreglos

# al finalizar esta sesion, vamos a poder:

#1. comprender que es una estructura de datos y por que son importantes en la programacion.

#2. identificar las caracteristicas claves de los arreglos: contiguidad, accesos por incide, cuales son las ventajas de usarlos y como se limitan.

# 3. diferenciar entre vectores unidimensionales y matrices multidimensionales.

# 4. escribiy codigo python para crear y recorrer arreglos, manejando posibles errores en el indice

# 5. resolver ejercicios practicos de definicion e inicializacion de vectores y matrices.

# que son es una estructura de datos?

# es una forma de organizar y almacenar datos en la memoria para que puedan ser utilizados de forma eficiente.

# es importante elegir una estructura correcta por que esto impacta directamente en la velocidad de acceso, la facilidad de modificacion y el consumo de recursos.

# tipos basicos de estructuras de datos:
# Arreglos (listas o vectores), pilas (stacks),
# colas (queues), arboles (trees), grafos (graphs), tablas hash (hash tables).

# Caracteristicas de los arreglos.

# un arreglo es una coleccion de elementos ordenados por un indice que se almacenan de forma contigua en memoria, un arreglo puede contener cualquier tipo de dato y pueden mutar en tamaño (esto funciona en python.)

# caracterusticas:

# Contiguidad en memoria.

# los elementos se almacenan de forma continua, uno tras otro

# ventajas: acceso muy rapido a cualquier posicion.

# limitacion: redimensionar implica duplicar todo el contenido del arreglo.

# acceso por indice

# Cada elemento tiene un indice ENTERO asociado, comienzan desde cero.

# permite lecturas rapidas de tipo lineal.

# lista[3]

# lista[-1]

# ventajas como el acceso directo a un elemento especifico por indice es posible, tambien permite que las iteraciones sean mas simples.

# limitaciones:
# lenguajes estaticos son de tamaño fijo o en lenguajes dinamicos son costosos de redimensionar.

# inserciones/borrados en posiciones intermedias requieren desplazar los elementos en memoria, lo que puede tambien ser costoso.

# 2.3 Vectores unidimensionales vs. matrices multidimensionales.

# vector unidimensional, tambien conocido como lista es un arreglo que contiene tipos de datos simples o primitivos.

# dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# print(f"hoy es {dias_semana[0]}")


# listas multidimensionales o matrices.

# suele contener tipos de datos compuestos:
# arreglos o diccionarios

# matriz_3x3 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(f"quiero imprimir el numero {matriz_3x3[1][1]}")

# Vector de cadenas:

# definir un vector llamado frutas que contenga al menos 5 nombres de frutas, luego los vamos a recorrer y vamos a imprimir su nombre y su indice.

# frutas = ["Mango", "Cereza", "Fresa", "Piña", "Aguacate", "Arandanos", "tomate", "Banano", "kiwi", "Lulo", "Mangostino", "Zapote", "Guayaba", "Granadilla", "Coco"]

# print("holi, estoy resoliviendo el reto de las furtas")

# for idx, fruta in enumerate(frutas):
#     print(f"[{idx}] -> {fruta}")
# print("\n")

# matriz 3 x 3

# enunciado: crear una matriz 3 x 3 con valores aleatorios, eso si, numericos, despues, recorremos las filas y las columnas para imprimir el valor de cada celda con el siguiente formato:

# fila, columna -> valor.

tablero = [
    [0, 1, 2],
    [13, 4, 3],
    [20, 2, 8]
]

print("Este es el reto de la matriz.")
for fila in range(len(tablero)):
    for julanito in range(len(tablero[fila])):
        valor = tablero[fila][julanito]
        print(f"({fila}, {julanito}) -> {valor}")
    print()
