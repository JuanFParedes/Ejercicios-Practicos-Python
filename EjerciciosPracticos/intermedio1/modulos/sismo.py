from tabulate import tabulate
import sys
from os import system

lista_ciudades = []
cantidad_sismos = 0
los_sismos_son_iguales = False

def borrar_pantalla():
    system("cls")

def app():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+
  +--CONTROL DE SISMOS--+
  +-+-+-+-+-+-+-+-+-+-+-+
"""
  print(titulo)
  menu = [["1.","Registrar una Ciudad"], ["2.", "Registrar un Sismo"], ["3.", "Buscar sismos por ciudad"], ["4.", "Informe de Riesgo"], ["5.", "Salir"]]
  print(tabulate(menu, tablefmt="fancy_grid"))
  option = input("\n>> ")
  if option == "1":
    registrar_ciudad()
  elif option == "2":
    registrar_sismo()
  elif option == "3":
    buscar_sismo_ciudad()
  elif option == "4":
    informe_riesgo()
    pass
  elif option == "5":
    sys.exit("Bye Bye")
  else:
    app()

def registrar_ciudad():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+--+
  +--REGISTRO DE CIUDADES--+
  +--+-+-+-+-+-+-+-+-+-+-+-+
"""
  print(titulo)
  if len(lista_ciudades) < 5:
    print(tabulate(lista_ciudades, tablefmt="fancy_grid"))
    nombre = input("Ingrese el nombre de la ciudad que va a registrar: ").capitalize()
    ciudad = [nombre, []]
    lista_ciudades.append(ciudad)
    print(f"Se ha registrado la ciudad {nombre} con exito")
    option = input("Quiere registrar otra ciudad? S(si) Enter(no)").upper()
    if option == "S":
      registrar_ciudad()
    else:
      app()
  else:
    input("Ya hay 5 ciudades registradas, no puede registrar más. Pulse ENTER para ir al menú principal")
    app()

def buscar_ciudad(nombre:str):
  for ciudad in lista_ciudades:
    if ciudad[0] == nombre:
      respuesta = ciudad
  return respuesta

def sismos_iguales():
  response = False
  for i in range(len(lista_ciudades)-1):
    if len(lista_ciudades[i][1]) == len(lista_ciudades[i+1][1]):
      response = True
    else:
      response = False
  return response

def registrar_sismo():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+
  +--SERVICIO DE REGISTRO DE SISMOS--+
  +--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""
  print(titulo)
  print(tabulate(lista_ciudades, tablefmt="fancy_grid"))
  nombre = input("\nIngrese el nombre de la ciudad que presentó sismo: ").capitalize()
  ciudad = buscar_ciudad(nombre)
  borrar_pantalla()
  print(titulo)
  magnitud = float(input("Cúal fue la magnitud del sismo? "))
  ciudad[1].append(magnitud)

  print(tabulate([ciudad], headers="keys",tablefmt="fancy_grid"))
  option = input("Quieres agregar otro sismo? S(si) Enter(no)").upper()
  if option == "S":
    registrar_sismo()
  else:
    app()

def buscar_sismo_ciudad():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--BUSCAR LISTA DE SISMOS POR CIUDAD--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  resultado = []
  for ciudad in lista_ciudades:
    resultado.append([ciudad["nombre"]])

  print(tabulate(resultado, tablefmt="fancy_grid"))
  nombre = input("\nQué ciudad quiere consultar?").capitalize()
  ciudad_buscada = buscar_ciudad(nombre)

  print(tabulate([ciudad_buscada[0], ciudad_buscada[1]],headers=["Nombre", "Sismos"],tablefmt="fancy_grid"))
  input("Presiona ENTER para volver al menú principal")
  app()

def informe_riesgo():
  are_sismos_los_mismos = sismos_iguales()
  if isinstance(are_sismos_los_mismos, False):
    input("Las ciudades no tienen la misma cantidad de sismos, revise los datos\nPresiona ENTER para volver al menú principal")
    app()
  else:
    borrar_pantalla()
    titulo = """
      +-+-+-+-+-+-+-+-+-+-+--+
      +  INFORMES DE RIESGO  +
      +--+-+-+-+-+-+-+-+-+-+-+
    """
    print(titulo)
    clasificacion =[[],[],[]]
    for ciudad in lista_ciudades:
      contador = 0
      for sismos in ciudad[1]:
        contador += sismos
      promedio = contador / len(ciudad[1])
      if promedio < 2.5:
        clasificacion[0].append(ciudad[0])
      elif promedio <= 4.5 and promedio >= 2.6:
        clasificacion[1].append(ciudad[0])
      else:
        clasificacion[2].append(ciudad[0])
    print(tabulate([clasificacion],headers=["Amarillo", "Naranja", "Rojo"],tablefmt="fancy_grid"))
    input("Presione ENTER para volver")
    app()