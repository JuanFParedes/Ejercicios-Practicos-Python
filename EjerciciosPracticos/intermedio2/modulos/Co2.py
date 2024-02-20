from os import system
from tabulate import tabulate

listInstal = [
  {
    "instalacion": "Alcaldia",
    "dependencias": [],
    "valor kilovatios/hora": 1500,
  },
  {
    "instalacion": "Biblioteca",
    "dependencias": [],
    "valor kilovatios/hora": 3000
  },
  {
    "instalacion": "Universidad",
    "dependencias": [],
    "valor kilovatios/hora": 800
  },
  {
    "instalacion": "Planta Electrica",
    "dependencias": [],
    "valor kilovatios/hora": 500
  },
  {
    "instalacion": "Bienestar Familiar",
    "dependencias": [],
    "valor kilovatios/hora": 2300
  }
]

dependencia_mayor_consumo = {"nombre": "", "consumo": 0}

def borrar_pantalla():
    system("cls")

def buscar_instalacion():
  nombre = input("Ingrese el nombre de la instalación: ").title()
  for instalacion in listInstal:
    if instalacion["instalacion"] == nombre:
      respuesta = instalacion
      break
  return respuesta

def agregar_dependencias():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+--+
  +--AGREGAR DEPENDENCIAS--+
  +--+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  print(tabulate(listInstal,headers="keys", tablefmt="fancy_grid"))
  instalacion = buscar_instalacion()
  nombre = input("Ingrese el nombre de la dependencia a regristrar: ").title()
  potencia = float(input("Ingrese el consumo del dispositivo: "))
  uso = float(input("Ingrese un estimado semanal del uso en horas del dispositivo: "))
  dependencia = {
    "nombre": nombre,
    "potencia": potencia,
    "horas": uso
  }
  instalacion["dependencias"].append(dependencia)
  actualizar_consumo()

  input(f"{nombre} se ha agregado correctamente.\nPresione cualquier tecla para volver")

def actualizar_consumo():
  for instalacion in listInstal:
    for dependencia in instalacion["dependencias"]:
      consumo = (dependencia["potencia"] * dependencia["horas"])/100
      dependencia.update({"consumo": consumo})
      if consumo > dependencia_mayor_consumo["consumo"]:
        dependencia_mayor_consumo["nombre"] = dependencia["nombre"]
        dependencia_mayor_consumo["consumo"] = consumo

def mostrar_mayor_consumo():
  borrar_pantalla()
  print(tabulate([dependencia_mayor_consumo], headers="keys", tablefmt="fancy_grid"))
  input("\nPresiona cualquier tecla para volver")