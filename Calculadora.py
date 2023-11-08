def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre 0"

while True:
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    print("5: Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 5:
        break

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == 1:
        print("Resultado: ", suma(num1, num2))
    elif opcion == 2:
        print("Resultado: ", resta(num1, num2))
    elif opcion == 3:
        print("Resultado: ", multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado: ", division(num1, num2))
