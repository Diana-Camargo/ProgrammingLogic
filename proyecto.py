name=input("Ingrese su nombre: ")
age=input("Ingrese su edad: ")
table=input("Ingrese su número de mesa: ")
print("Su nombre es:")
print(name)
print("Su edad es:")
print(age)
print("Su mesa es:")
print(table)

print("MENÚ")
print("1- Hamburguesa \n2- Tacos \n3- Gorditas \n4- Flautas \n5- Enchiladas \n6- Sopes")
opcion = input("Qué plato gusta?: ") 
if opcion in ["1", "2", "3", "4", "5", "6"]:
    print("Preparando su comida")
else:
    ("Comida no disponible")

print("BEBIDAS")
print("1- Coca cola, \n2- Manzana, \n3- Ponche, \n4- Fanta, \n5- Uva, \n6- Pepsi, \n7- Agua de jamaica, \n8- Agua natural")
opcion = input("¿Qué gustaría tomar?: ")

if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
    print("En un momento le traeremos su bebida")
else:
    ("Bebida no disponible")

print("¿Le gustaría obtener el precio a pagar?: ")
print("si \nno")
opcion = input("")
if opcion in ["si"]:
    print("Sería un total de $120 pesos")
if opcion in ["no"]:
    print("Disfrute su comida")
print("¿Gusta algo más?")
print("si \nno")
opcion = input("")
if opcion in ["si"]:
    print("¿Que sería?")
if opcion in ["no"]:
    print("")
print("GRACIAS POR SU PREFERENCIA, LINDO DÍA")