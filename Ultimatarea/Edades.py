#Nombre: Brandon de Jesus Garza Jasso       Matricula: 250218
#pregunte el genero de 5 usuarios (H para Hombre y M para Mujer)
#intentos erroneos
#promedio de edad de ambos generos
#que genero por usuario tuvo la menor edad y la mayor

total_hombres = 0
total_mujeres = 0
suma_edad_hombres = 0
suma_edad_mujeres = 0
intentos_erroneos = 0

menor_edad = None
mayor_edad = None
genero_menor = ""
genero_mayor = ""

#Ciclo para 5 usuarios
for i in range(1, 6):
    while True:
        genero = input(f"Ingrese el género del usuario {i} (H/M): ").strip().upper()
        if genero in ["H", "M"]:
            break
        else:
            print("Error: ingrese solo H o M.")
            intentos_erroneos += 1

    edad = int(input(f"Ingrese la edad del usuario {i}: "))

    # Genro
    if genero == "H":
        total_hombres += 1
        suma_edad_hombres += edad
    else:
        total_mujeres += 1
        suma_edad_mujeres += edad

    # edadmenos
    if menor_edad is None or edad < menor_edad:
        menor_edad = edad
        genero_menor = genero

    # edadmas
    if mayor_edad is None or edad > mayor_edad:
        mayor_edad = edad
        genero_mayor = genero

#promedios
promedio_hombres = suma_edad_hombres / total_hombres if total_hombres > 0 else 0
promedio_mujeres = suma_edad_mujeres / total_mujeres if total_mujeres > 0 else 0

# Mostrar resultados
print("\n RESULTADOS ")
print(f"Intentos erróneos: {intentos_erroneos}")
print(f"Promedio edad hombres: {promedio_hombres:.2f}")
print(f"Promedio edad mujeres: {promedio_mujeres:.2f}")
print(f"Menor edad: {menor_edad} años - Género: {genero_menor}")
print(f"Mayor edad: {mayor_edad} años - Género: {genero_mayor}")
