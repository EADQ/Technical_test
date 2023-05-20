
# Ejercicio:
# Escribe una función en Python llamada "suma_pares" que reciba una lista de números enteros y devuelva la suma de los números pares en la lista.

# Tips y pistas:

# - Puedes utilizar un bucle `for` para recorrer la lista de números.
# - Puedes utilizar el operador de módulo `%` para verificar si un número es par. Si el resultado de `numero % 2` es igual a cero, el número es par.
# - Puedes utilizar una variable para ir acumulando la suma de los números pares.
# - Al final de la función, debes retornar el valor de la suma acumulada.

def suma_pares(lista):
    suma = 0
    for x in lista:
        if x % 2 == 0:
            suma += x

    return(suma)

lista = [1,2,3,4,5,6,7]
resultado = suma_pares(lista)
print(resultado)
