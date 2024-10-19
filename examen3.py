import random
def numero_azar():
    numero_azar = random.randint(1, 100)
    intentos = 0
    print("Intenta adivinar el número en pocos intentos")
    while True:
        intento = input("El número que debes de adivinar es del 1 al 100: ")
        try:
            intento = int(intento)
            intentos += 1
        except ValueError:
            print("Solamente se permiten números.")
            continue
        if intento < numero_azar:
            print("El número que elegiste es menor.")
        elif intento > numero_azar:
            print("El número que elegiste es mayor.")
        else:
            print(f"Felicidades adivinaste el número {numero_azar} en {intentos} intentos.")
            break
numero_azar()