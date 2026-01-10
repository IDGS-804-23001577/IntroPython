''' Operacion de multiplicacion de a x b utilizando sumas


a=3
b=4
salida 3+3+3=12

'''

a = 3
b = 4
x = 0
resultado = 0
tem = ''

while x < b:
    resultado += a
    tem += str(a) + '+'
    x += 1

print('La operacion de multiplicacion es: ')

print(tem + '=' + str(resultado))