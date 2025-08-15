#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#Supongamos que tenemos n grupos con y numeros, se necesita sumar e imprimir la suma por qrupo,
#hasta que el usario ingrese 'x' y que se pueda cambiar de grupo con la letra s

grupo = 1
suma = 0

print("Ingrese números para cada grupo")
print("Escriba 's' para cambiar de grupo y 'x' para terminar\n")

while True:
    dato = input(f"[Grupo {grupo}] Ingrese un número: ").lower()

    if dato == "x":
        print(f"Suma del grupo {grupo}: {suma}")
        print("\nPrograma terminado.")
        break

    elif dato == "s":
        print(f"Suma del grupo {grupo}: {suma}")
        grupo += 1
        suma = 0

    else:
        if dato.replace(".", "", 1).isdigit():
            suma += float(dato)
        else:
            print("Entrada no valida, escriba un número, 's' o 'x'.")
