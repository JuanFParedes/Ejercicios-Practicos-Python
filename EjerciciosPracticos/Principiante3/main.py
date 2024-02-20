from tabulate import tabulate

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categoria_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidad grado I'
    elif imc < 40:
        return 'Obesidad grado II'
    else:
        return 'Obesidad grado III'

estudiantes = []

def registrar_paciente():
    nombreEstudiante = input("Ingrese el nombre del estudiante: ")
    edadEstudiante = int(input("Ingrese la edad del estudiante: "))
    pesoEstudiante = float(input("Ingrese el peso del estudiante en kg: "))
    alturaEstudiante = float(input("Ingrese la altura del estudiante en metros: "))

    imc = calcular_imc(pesoEstudiante, alturaEstudiante)
    categoria = categoria_imc(imc)

    estudiantes.append([nombreEstudiante, edadEstudiante, round(imc, 2), categoria])
    print("Estudiante registrado con éxito.")

while True:
    print("""          
        ######################################
        #########  MENU PRINCIPAL ############
        ######################################
        
    1. Registrar nuevo estudiante 
    2. Cuántos estudiantes se encuentran en el peso ideal.
    3. Cuántos estudiantes se encuentran en obesidad grado I.
    4. Cuántos estudiantes se encuentran en obesidad grado II.
    5. Cuántos estudiantes se encuentran en obesidad grado III.
    6. Cuántos estudiantes se encuentran en Sobrepeso.
    7. Mostrar todos los estudiantes
    8. Salir
""")

    opcion = input("Seleccione una opción del menú: ")

    if opcion == '1':
        registrar_paciente()
    elif opcion == '2':
        peso_normal_count = sum(1 for paciente in estudiantes if paciente[3] == 'Peso normal')
        print("Cantidad de estudiantes en peso ideal:", peso_normal_count)
    elif opcion == '3':
        obesidad_grado_I_count = sum(1 for paciente in estudiantes if paciente[3] == 'Obesidad grado I')
        print("Cantidad de estudiantes en obesidad grado I:", obesidad_grado_I_count)
    elif opcion == '4':
        obesidad_grado_II_count = sum(1 for paciente in estudiantes if paciente[3] == 'Obesidad grado II')
        print("Cantidad de estudiantes en obesidad grado II:", obesidad_grado_II_count)
    elif opcion == '5':
        obesidad_grado_III_count = sum(1 for paciente in estudiantes if paciente[3] == 'Obesidad grado III')
        print("Cantidad de estudiantes en obesidad grado III:", obesidad_grado_III_count)
    elif opcion == '6':
        sobrepeso_count = sum(1 for paciente in estudiantes if paciente[3] == 'Sobrepeso')
        print("Cantidad de estudiantes en Sobrepeso:", sobrepeso_count)
    elif opcion == '7':
        print(tabulate(estudiantes, headers=["Nombre", "Edad", "IMC", "Categoría"]))
    elif opcion == '8':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

print("Gracias por usar el programa, hasta la proxima :) ....")