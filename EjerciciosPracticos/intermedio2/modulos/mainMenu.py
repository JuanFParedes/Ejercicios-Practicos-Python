import sys
from tabulate import tabulate
from .Co2 import agregar_dependencias, mostrar_mayor_consumo

def main_Menu():
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--CONSUMO DE ELECTRICIDAD DISTRITAL--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  menu = [["1.","Registrar Dependencia"],["2.","CO2 producido"],["3.","Dependencia que produce mayor CO2"], ["4.", "Salir"]]
  print(tabulate(menu, tablefmt="fancy_grid"))
  opcion = input("\n>> ").upper()
  
  if opcion == "1":
    agregar_dependencias()
    main_Menu()
  elif opcion == "2":
    pass
  elif opcion == "3":
    mostrar_mayor_consumo()
    main_Menu()
  elif opcion == "4":
    sys.exit("Bye Bye")
  else:
    main_Menu()