from os import system
import sys

from tabulate import tabulate
from modulos.inventario import registrar_producto, ver_productos, update_stock, productos_criticos, ganancia_potencial

def borrar_pantalla():
    system("cls")

def main_menu():
  borrar_pantalla()
  titulo = """
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+
    +--ADMINISTRADOR DE PRODUCTOS--+
    +--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  menu = [["1.","Registrar producto"],["2.","Ver lista de productos"], ["3.", "Actualizar Stock"],["4.", "Productos en estado critico"], ["5.", "Ganancia Potencial"], ["6.", "Salir"]]
  print(tabulate(menu,tablefmt="fancy_grid"))
  option = input("\n>> ")

  if option == "1":
    registrar_producto()
  elif option == "2":
    ver_productos()
  elif option == "3":
    update_stock()
  elif option == "4":
    productos_criticos()
  elif option == "5":
    ganancia_potencial()
  elif option == "6":
    sys.exit("Bye Bye")
  else:
    main_menu()