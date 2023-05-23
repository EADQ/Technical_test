# Ejercicio:
# Escribe una función en Python llamada "conteo_vocales" que reciba una cadena de texto y devuelva un diccionario con el conteo de cada vocal presente en la cadena. El diccionario debe tener las vocales como claves y el número de veces que aparecen como valores.

# Tips y pistas:
# - Puedes utilizar un bucle `for` para recorrer cada caracter de la cadena.
# - Puedes utilizar el método `lower()` para convertir todos los caracteres a minúsculas y así evitar diferencias de mayúsculas y minúsculas.
# - Puedes utilizar un condicional `if` para verificar si cada caracter es una vocal.
# - Utiliza un diccionario para ir almacenando el conteo de cada vocal.
# - Al final de la función, debes retornar el diccionario con los conteos.

def conteo_vocales(text):
    count = 0
    for x in text:
        y = text.lower()
        count += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0


text = 'prueba'
prueba_codigo = conteo_vocales(text)
print(prueba_codigo)

