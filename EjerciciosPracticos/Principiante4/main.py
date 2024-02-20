numeros = []
total_numeros = 0
total_pares = 0
suma_pares = 0
total_impares = 0
suma_impares = 0
menores_10 = 0
entre_20_50 = 0
mayores_100 = 0

while True:
    num = int(input("Ingrese un número entero positivo (ingrese un número negativo para finalizar): "))
    
    if num < 0:
        print("\nReporte:")
        print(f"a. Total de números ingresados: {total_numeros}")
        print(f"b. Total de números pares ingresados: {total_pares}")
        if total_pares > 0:
            promedio_pares = suma_pares / total_pares
            print(f"c. Promedio de los números pares: {promedio_pares}")
        if total_impares > 0:
            promedio_impares = suma_impares / total_impares
            print(f"d. Promedio de los números impares: {promedio_impares}")
        print(f"e. Cuántos números son menores que 10: {menores_10}")
        print(f"f. Cuántos números están entre 20 y 50: {entre_20_50}")
        print(f"g. Cuántos números son mayores que 100: {mayores_100}")
        break
    
    total_numeros += 1
    
    if num % 2 == 0:
        total_pares += 1
        suma_pares += num
    else:
        total_impares += 1
        suma_impares += num
    
    if num < 10:
        menores_10 += 1
    elif 20 <= num <= 50:
        entre_20_50 += 1
    elif num > 100:
        mayores_100 += 1
