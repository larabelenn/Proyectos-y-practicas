#Inicializazo una variable llamada "Inventario" como un diccionario vacío. 
#Un diccionario es una estructura de datos que permite almacenar y organizar datos de manera eficiente, los datos se encuentran ordenados utilizando una clave única para cada uno de ellos, lo que permite localizar cada uno de los datos de una forma muy rápida. 

inventario = {}

def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad

def vender_producto(nombre, cantidad):
    if nombre in inventario:
        if inventario[nombre] >= cantidad:
            inventario[nombre] -= cantidad
        else:
            print("No hay suficiente cantidad de", nombre)
    else:
        print(nombre, "no está en el inventario")

# Mostrar el inventario completo
def mostrar_inventario():
    print("Inventario:")
    for producto, cantidad in inventario.items():
        print(producto, ":", cantidad)

# Menú principal
while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        agregar_producto(producto, cantidad)
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        vender_producto(producto, cantidad)
    elif opcion == '3':
        mostrar_inventario()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente de nuevo.")
