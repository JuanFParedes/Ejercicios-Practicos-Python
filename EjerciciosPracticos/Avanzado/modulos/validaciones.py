def validar_edad(edad:int,categoria:str):
  if edad < 15:
    input("El participante es muy joven para registrarse en esta categoria.\nPresione cualquier tecla para volver atras.")
    return False
  elif categoria == "Novato" and edad not in range(15,16):
    input("El participante debe tener entre 15 y 16 años para poder participar en esta categoría.\nPresione cualquier tecla para volver atras.")
    return False
  elif categoria == "Intermedio" and edad not in range(17,20):
    input("El participante debe tener entre 17 y 20 años para poder participar en esta categoría.\nPresione cualquier tecla para volver atras.")
    return False
  elif categoria not in ["Novato", "Intermedio", "Avanzado"]:
    input("La categoría ingresada no es válida.\nPresione cualquier tecla para volver atras")
    return False

