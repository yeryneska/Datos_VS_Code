print("Calculadora con una sola variable \n")
print("******************")
print("*Menu de Opciones*")
print("****************** \n")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Division Entera")
print("6.- Exponente")
print("7.- Modulo o Resto \n")
opcion = int(input("Introduce la deseada "))

if opcion == 1:
    print("Ud. selecciono la suma ")
    num_uno = int(input("Introduce primer numero "))
    num_dos = int(input("Introduce segundo numero "))
    suma = num_uno + num_dos
    print("El resultado de la suma es ", suma)

elif opcion == 2:
    print("Ud. selecciono la suma ")
    num_uno = int(input("Introduce primer numero "))
    num_dos = int(input("Introduce segundo numero "))
    resta = num_uno - num_dos
    print("El resultado de la resta es ", resta)

    