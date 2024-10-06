def calculadora():
    print("Calculadora básica")
    #pide al usuario dos números y los convierte a enteros
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    #Opciones de operación
    print("\nSelecciona la operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3: Multiplicación")
    print("4. División")
    #operaciones
    if opcion == '1':
        print(f"El resultado de sumar {num1} + {num2} es: {num1 + num2}")
    elif opcion == '2':
        print(f"\nEl resultado de restar {num1} - {num2} es: {num1 - num2}")
    elif opcion == '3':
        print(f"\nEl resultado de multiplicar {num1} * {num2} es: {num1 * num2}")
    elif opcion == '4':
        print(f"\nEl resultado de dividir {num1} / {num2} es: {num1 / num2}")
    if num2:int = 0
    else:
        print("\nError : No se puede dividir entre 0")
    