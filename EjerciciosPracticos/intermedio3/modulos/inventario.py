import sys
from tabulate import tabulate
from modulos import menus
from os import system

list_products = []

def registrar_producto():
  menus.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--REGISTRO DE PRODUCTOS--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  codigo = input("Ingrese el código del producto: ").title()
  nombre = input("Ingrese el nombre del producto: ").title()
  valor_compra = float(input("Ingrese el valor de compra: "))
  valor_venta = float(input("Ingrese el valor de venta: "))
  stock_actual = int(input("Ingese el stock actual: "))
  stock_minimo = int(input("Ingrese el stock mínimo del producto: "))
  stock_maximo = int(input("Ingrese el stock máximo del producto: "))
  nombre_proveedor = input("Ingrese el nombre del proveedor: ").title()

  producto = {
    "codigo": codigo,
    "nombre": nombre,
    "valor de compra": valor_compra,
    "valor de venta": valor_venta,
    "stock actual": stock_actual,
    "stock minimo": stock_minimo,
    "stock maximo": stock_maximo,
    "nombre del proveedor": nombre_proveedor
  }

  for item in list_products:
    if item["nombre"] == nombre or item["codigo"] == codigo:
      input("Este producto ya está en la base de datos.\nPresione cualquier tecla para volver al inicio")
      menus.main_menu()

  list_products.append(producto)
  print(tabulate(list_products, headers="keys", tablefmt="fancy_grid"))
  input("\nPresione cualquier tecla para volver al menú principal")
  menus.main_menu()

def ver_productos():
  menus.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+--+
  +--LISTADO DE PRODUCTOS--+
  +--+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  print(tabulate(list_products, headers="keys", tablefmt="fancy_grid"))
  input("Pulsa cualquier tecla para volver al menu principal")
  menus.main_menu()

def update_stock():
  menus.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--ACTUALIZADOR DE STOCK--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)

  nombre = input("\nIngrese el nombre del producto a editar en la base de datos: ").title()
  resultado = {}
  for producto in list_products:
    if producto["nombre"] == nombre or producto["codigo"] == nombre:
      resultado = producto
      break

  print(tabulate([resultado], headers="keys", tablefmt="fancy_grid"))
  stock_actual = int(input("Cuánto es el stock actual del producto? "))
  resultado["stock actual"] = stock_actual

  menus.borrar_pantalla()
  print("Se ha actualizado con exito, revise la nueva base de datos")
  print(tabulate([resultado], headers="keys", tablefmt="fancy_grid"))
  input("\nPresione cualquier tecla para continuar")
  menus.main_menu()

def productos_criticos():
  menus.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--PRODUCTOS EN ESTADO CRITICO--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  productos_criticos = []
  for producto in list_products:
    if producto["stock actual"] < producto["stock minimo"]:
      productos_criticos.append(producto)
  print(tabulate(productos_criticos, headers="keys", tablefmt="fancy_grid"))
  input("Presione cualquier tecla para volver al menu principal")
  menus.main_menu()

def ganancia_potencial():
  menus.borrar_pantalla()
  titulo = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  +--GANANCIA POTENCIAL POR PRODUCTO--+
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """
  print(titulo)
  lista_ganancias = []
  for producto in list_products:
    ganancia = (producto["valor de venta"] - producto["valor de compra"]) * producto["stock actual"]
    newProducto = {
      "nombre": producto["nombre"],
      "ganancia potencial": ganancia
    }
    lista_ganancias.append(newProducto)
  print(tabulate(lista_ganancias, headers="keys", tablefmt="fancy_grid"))
  input("\nPresione cualquier tecla para volver al menu principal")
  menus.main_menu()