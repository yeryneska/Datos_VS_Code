print("Practica 16 - Vacaciones ")
print("========================= \n")
print("Aplicacion Vcaciones G&M \n")
empleado = input("Indicar nombre del empleado: ")
clave = int(input("Indicar la clave de la gerencia del empleado: "))
tiempo = int(input("Indicar tiempo de trabajo en la empresa: "))

if clave == 1:
    if tiempo == 1:
        print("Al empleado " + empleado)
        print("De la Gerencia ", clave)
        print("Le corresponden 6 dias de vacaciones")
    elif tiempo >= 2 and tiempo <=6:
        print("Al empleado " + empleado)
        print("De la Gerencia ", clave)
        print("Le corresponden 14 dias de vacaciones")
    elif tiempo >=7:
        print("Al empleado " + empleado)
        print("De la Gerencia ", clave)
        print("Le corresponden 20 dias de vacaciones")

elif clave == 2:
        if tiempo == 1:
            print("Al empleado " + empleado)
            print("De la Gerencia ", clave)
            print("Le corresponden 6 dias de vacaciones")

        elif tiempo >= 2 and tiempo <=6:
            print("Al empleado " + empleado)
            print("De la Gerencia ", clave)
            print("Le corresponden 14 dias de vacaciones")

        elif tiempo >=7:
            print("Al empleado " + empleado)
            print("De la Gerencia ", clave)
            print("Le corresponden 20 dias de vacaciones")        

    