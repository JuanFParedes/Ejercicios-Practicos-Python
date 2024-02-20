def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categoria_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

nombreEstudiante = input("Ingrese el nombre del estudiante: ")
edadEstudiante = int(input("Ingrese la edad del estudiante: "))
pesoEstudiante = float(input("Ingrese el peso del estudiante en kg: "))
alturaEstudiante = float(input("Ingrese la altura del estudiante en metros: "))

imc = calcular_imc(pesoEstudiante, alturaEstudiante)
categoria = categoria_imc(imc)

print("\nNombre del estudiante:", nombreEstudiante)
print("Edad:", edadEstudiante, "años")
print("IMC:", round(imc, 2))
print("Categoría IMC:", categoria)