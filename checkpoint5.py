
# 1  Cree un bucle For de Python.
# Bucle for para imprimir números del 1 al 5
for i in range(1, 6):
    print(i)

# Output
# 1
# 2
# 3
# 4
# 5

# 2  Cree una función de Python llamada suma 
# que tome 3 argumentos y devuelva la suma 
# de los 3.

def suma(a, b, c):
    return a + b + c

# Ejemplo de uso de la función suma
resultado = suma(2, 3, 4)
print("La suma es:", resultado)

# Output
# La suma es: 9

# 3  Cree una función lambda con la misma 
# funcionalidad que la función de suma 
# que acaba de crear.
suma_lambda = lambda a, b, c: a + b + c

# Ejemplo de uso de la función lambda
resultado_lambda = suma_lambda(2, 3, 4)
print("La suma (lambda) es:", resultado_lambda)

# Output
# La suma (lambda) es: 9

# 4 -Utilizando la siguiente lista y variable, 
# determine si el valor de la variable 
# coincide o no con un valor de la lista. 
# *Sugerencia, si es necesario, utilice un 
# bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Utilizando un bucle for in y el operador in
for nombre_en_lista in lista_nombre:
    if nombre == nombre_en_lista:
        print("El nombre", nombre, "coincide con un valor de la lista.")
        break
else:
    print("El nombre", nombre, "no coincide con ningún valor de la lista.")

# Output
# El nombre Enrique no coincide con ningún valor de la lista.