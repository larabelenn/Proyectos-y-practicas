numero = float(input("Ingresa un número: "))

# Dar formato como número entero
numero_entero = "{:.0f}".format(numero)
print("Entero", numero_entero)

# Dar formato como número decimal 
numero_decimal= "{:.2f}".format(numero)
print("Decimal", numero_decimal)

# Dejar ceros a al izquierda
numero_ceros_izquierda= "{:0>20}".format(numero)
print("Con ceros a la izquierda", numero_ceros_izquierda)

# Dejar ceros a al derecha
numero_ceros_derecha= "{:0<20}".format(numero)
print("Con ceros a la derecha", numero_ceros_derecha)

# Separador de miles con coma
numero_miles= "{:,}".format(numero)
print("Separado en miles con coma", numero_miles)