
# DADA UNA LISTA DE NUMEROS ENTEROS, DETERMINE SI EL PRODUCTO DE TODOS LOS NUMEROS ES PAR O IMPAR, SI EL PRODUCTO ES PAR
# RETORNAR LA SUMA DE TODOS LOS NUMEROS DE LA LISTA, SI ES IMPAR RETORNAR CERO
# EJEMPLO: ENTRADA = [1,2,3,4] SALIDA 10

def par_impar(lista):
    producto = 1
    for num in lista:
        producto *= num

    if producto % 2 == 0:
        suma = sum(lista)
        return suma
    
    else:
        return 0


lista = [1,2,3,4]
resultado = par_impar(lista)
print(resultado)
  
