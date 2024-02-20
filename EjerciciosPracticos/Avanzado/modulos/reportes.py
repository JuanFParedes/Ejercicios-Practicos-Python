from . import menus as mn
from .participantes import lista_categorias
from tabulate import tabulate

def menu_reportes():
  mn.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +-REPORTES TORNEO DE TENIS--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  menu = [["1.","Registros por categoria"], ["2.","Ganadores de la categoría"], ["3.","Salir"]]
  print(tabulate(menu,tablefmt="fancy_grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    registro_categoria()
  elif opcion == "2":
    pass
  elif opcion == "3":
    mn.main_menu
  else:
    menu_reportes()

def registro_categoria():
  mn.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+
  +-- JUGADORES REGISTRADOS POR CATEGORIA--+
  +--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  menu = [["1.", "Novato"], ["2.","Intermedio"], ["3.","Avanzado"], ["4.","salir"]]
  print(tabulate(menu,tablefmt="fancy_grid"))
  opcion = input("\n>> ")
  tabla = []
  if opcion == "1":
    if len(lista_categorias["Novato"]) < 1:
      input("No hay jugadores en esta categoria.\nPresione cualquier tecla para volver atras")
      registro_categoria()
    else:
      for index, item in enumerate(lista_categorias["Novato"]):
        tabla.append([index + 1, item])
      print(tabulate(tabla,tablefmt="grid"))
      input("\nPresione cualquier tecla para volver.")
      registro_categoria()
  elif opcion == "2":
    if len(lista_categorias["Intermedio"]) < 1:
      input("No hay jugadores en esta categoria.\nPresione cualquier tecla para volver atras")
      registro_categoria()
    else:
      for index, item in enumerate(lista_categorias["Intermedio"]):
        tabla.append([index + 1, item])
      print(tabulate(tabla,tablefmt="grid"))
      input("\nPresione cualquier tecla para volver.")
      registro_categoria()
  elif opcion == "3":
    if len(lista_categorias["Avanzado"]) < 1:
      input("No hay jugadores en esta categoria.\nPresione cualquier tecla para volver")
      registro_categoria()
    else:
      for index, item in enumerate(lista_categorias["Avanzado"]):
        tabla.append([index + 1, item])
      print(tabulate(tabla,tablefmt="fancy_grid"))
      input("\nPresione cualquier tecla para volver.")
      registro_categoria()
  elif opcion == "4":
      mn.main_menu()
  else:
      registro_categoria()

def ganadores():
  mn.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+
  +--PODIO--+
  +-+-+-+-+-+
  """
  print(titulo)
  
  for participante in lista_categorias:
    contador_novato = 0
    contador_intermedio = 0
    contador_avanzado = 0

    categoria = participante["categoria"]
    puntos = participante["puntuacion"]["TP"]

    if categoria == "Novato" and puntos > contador_novato:
      contador_novato = puntos
      novato_ganador = participante
    elif categoria == "Intermedio" and puntos > contador_intermedio:
      contador_intermedio = puntos
      intermedio_ganador = participante
    elif categoria == "Avanzado" and puntos > contador_avanzado:
      contador_avanzado = puntos
      avanzado_ganador = participante
  ganadores = {
    "Notavo": novato_ganador,
    "Intermedio": intermedio_ganador,
    "Avanzado": avanzado_ganador
    }
  print(tabulate([ganadores],headers="keys",tablefmt="fancy_grid"))
  input("\nPresiona cualquier tecla para volver.")
  mn.main_menu()
