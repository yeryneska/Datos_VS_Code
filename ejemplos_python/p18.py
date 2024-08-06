print("****************************************************")
print("*Programa que determina numero mayor entre 3 numeros")
print("****************************************************\n")
num_uno = int(input("Indica primer numero "))
num_dos = int(input("Indica segundo numero "))
num_tres = int(input("Indica tercer numero "))

if num_uno > num_dos:
    if num_uno > num_tres:
        print("El numero ", num_uno, "es el mayor de los 3")

    elif num_tres > num_dos:
         print("El numero ", num_tres, "es el mayor de los 3") 

elif num_dos > num_tres:
    print("El numero ", num_dos, "es el mayor de los 3")

else:
    print("El numero ", num_tres, "es el mayor de los 3")