print("Bienvenidos a la calculadora")
print("Para salir de la aplicacion escribe Salir")
print("Las operaciones son suma, mult, div y resta")

primer_numero = 0
segundo_numero = 0
suma = "suma"
primer_numero = int(input("Ingresa numero: "))
operacion = input("Ingresa operacion: ")

if operacion == suma:
    segundo_numero = int(input("Ingresa el siguinete numero: "))
    resultado = primer_numero + segundo_numero
    print(resultado)
