from tabulate import tabulate

from . import menus as mn
from .validaciones import validar_edad

lista_participantes = []
lista_categorias = {"Novato": [], "Intermedio": [], "Avanzado": []}

def search_player(nombre:str):
  for participante in lista_participantes:
    if participante["nombre"] == nombre:
      return participante

def puntuar(participante1, participante2):
  nombre1 = participante1["nombre"]
  nombre2 = participante2["nombre"]
  puntos_participante1 = int(input(f"Cuántos puntos hizo {nombre1}"))
  puntos_participante2 = int(input(f"Cuántos puntos hizo {nombre2}"))

  participante1["PJ"] += 1
  participante2["PJ"] += 1

  if puntos_participante1 > puntos_participante2:
    participante1["PG"] += 1
    participante1["TP"] += 2
    participante1["PA"] += (puntos_participante1 - puntos_participante2)
    participante2["PP"] += 1
  elif puntos_participante2 > puntos_participante1:
    participante2["PG"] += 1
    participante2["TP"] += 2
    participante2["PA"] += (puntos_participante2 - puntos_participante1)
    participante1["PP"] += 1
  else:
    participante1["TP"] += 1
    participante2["TP"] += 1
def add_category(participante:dict):
  nombre = participante["nombre"]
  categoria = participante["categoria"]

  if categoria == "Novato":
    lista_categorias["Novato"].append(nombre)
  elif categoria == "Intermedio":
    lista_categorias["Intermedio"].append(nombre)
  elif categoria == "Avanzado":
    lista_categorias["Avanzado"].append(nombre)

def add_player():
  mn.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--SISTEMA DE  REGISTRO PARA PARTICIPANTES--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  try:
    nombre = input("Ingrese el nombre del participante: ").title()
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    categoria = input(f"Ingrese la categoria de {nombre} puede ser (Novato, Intermedio, Avanzado): ").title()
    if validar_edad(edad, categoria) == False:
      add_player()
    nuevo_participante = {
      "nombre": nombre,
      "edad": edad,
      "categoria": categoria,
      "puntuacion": {
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PA": 0,
        "TP": 0
        }
      }
    lista_participantes.append(nuevo_participante)
    add_category(nuevo_participante)

    print(f"{nombre} ha sido registrad@ correctamente, quiere ingresar otro participante? S(si) Enter(no)")
    opcion = input("\n>> ").upper()
    if opcion == "S":
      add_player()
    else:
      mn.main_menu()
  except ValueError:
    input("Valor invalido. Presione cualquier tecla para volver al menu principal")
    mn.main_menu()

def add_date():
  mn.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--REGISTRO DE FECHAS DEL TORNEO--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  print(tabulate([["1.", "Novato"], ["2.","Intermedio"], ["3.","Avanzado"]], tablefmt="fancy_grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    definir_fecha("Novato")
  elif opcion == "2":
    definir_fecha("Intermedio")
  elif opcion == "3":
    definir_fecha("Avanzado")
  else:
    add_date()

def definir_fecha(categoria:str):
  if len(lista_categorias[categoria]) < 5:
    input("Aún faltan participantes para iniciar los partidos de esta categoría.\nPresione cualquier tecla para volver al menu principal.")
    mn.main_menu()
  else:
    print(tabulate([lista_categorias[categoria]],tablefmt="fancy_grid"))
    participante1 = input("Ingrese el nombre del primer participante: ").title()
    participante2 = input("Ingrese el nombre del segundo participante: ").title()
    atleta1 = search_player(participante1)
    atleta2 = search_player(participante2)
    if atleta1["categoria"] != categoria or atleta2["categoria"] != categoria:
      input("Alguno de los participantes no hace parte de la categoría.\nPresione cualquier tecla para volver al menu principal.")
      mn.main_menu()
    puntuar(atleta1, atleta2)
    mn.borrar_pantalla()
    print(tabulate([participante1, participante2], headers="keys",tablefmt="fancy_grid"))
    input("Presione cualquier tecla para volver al menu principal.")
    mn.main_menu()

