import sys
from os import system

from tabulate import tabulate
from .participantes import add_player, add_date
from .reportes import menu_reportes

def borrar_pantalla():
    system("cls")

def main_menu():
  borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--TORNEO DE TENIS DE MESA--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  menu = [["1.", "Agregar participante"], ["2.", "Registrar fecha"], ["3.","Reportes"], ["4.","Salir"]]
  print(tabulate(menu,tablefmt="fancy_grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    add_player()
    main_menu()
  elif opcion == "2":
    add_date()
    main_menu()
  elif opcion == "3":
    menu_reportes()
    main_menu()
  elif opcion == "4":
    sys.exit("Bye Bye")
  else:
    main_menu()