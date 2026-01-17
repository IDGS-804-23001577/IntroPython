import os

#definir lo que hace cada funcion
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def main():
    # limpiar la pantalla de cmd
    os.system('cls')
    
    # enseña el menuu
    menu()
    
    
    opcion = int(input("Elige una opcion: "))
    
    
    print("")
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    
    resultado = 0

    # Usamos if y elif básicos para decidir qué hacer
    if opcion == 1:
        resultado = sumar(num1, num2)
    elif opcion == 2:
        resultado = restar(num1, num2)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
    elif opcion == 4:
        resultado = dividir(num1, num2)
    
    
    
    print("El resultado es: {}".format(resultado))

# corra el programa
if __name__ == "__main__":
    main()