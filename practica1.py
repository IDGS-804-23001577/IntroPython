''' Operacion de multiplicacion de a x b utilizando sumas


a=3
b=4

'''

a = 3
b = 4

resultado = 0
contador = 0

# Usamos un ciclo while para sumar 'a' la cantidad de veces que diga 'b'
while contador < b:
    resultado = resultado + a
    contador = contador + 1

print("El resultado es:", resultado)