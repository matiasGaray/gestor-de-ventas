import os
import time

encendido = True
# Como que ya no hay mensaje
print("Bienvenido a hamburguesas IT")
#Valido que la variable solo tenga letras
while True:
  encargado = input("Encargad@ -> ")
  if encargado.isalpha() == True:
    break
#Borro la pantalla para mejor legibilidad
os.system("cls")

while encendido:
  #Guardo la hora de ingreso del empleado  
  ingreso = time.strftime("%c")
  #Creo un archivo para registrar la hora de ingreso del empleado
  with open("registro.txt","a") as f:
    f.write(f"IN Encargad@: {encargado}, {ingreso}\n")
  #Creo la interfaz y el menu
  print("Bienvenido a hamburguesas IT")
  print("Encargad@: ",encargado)
  print("Recuerda, siempre hay que recibir al cliente con una sonrisa")
  print()
  print()
  print("1 – Ingreso nuevo pedido")
  print("2 – Cambio de turno")
  print("3 – Apagar sistema")
#Otro mensaje
  #Valido datos alfanumericos
  while True:
    try:
      opcion = int(input("Que opcion deseas elegir? "))
      if 0 < opcion < 4:
        break
    except:
      print("Debes ingresar un numero entre 1 y 3")
  if opcion == 1:
    while True:
      nombre_cliente = input("Ingrese el nombre del cliente ")
      if nombre_cliente.isalpha() == True:
        break
    while True:
      try:
        cant_combo_S = int(input("Ingrese la cantidad de combos S "))
        break
      except:
        print("Se debe introducir un numero")
    while True:
      try:
        cant_combo_D = int(input("Ingrese la cantidad de combos D "))
        break
      except:
        print("Se deben introducir numeros")
    while True:
      try:
        cant_combo_T = int(input("Ingrese la cantidad de combos T "))
        break
      except:
        print("Se deben introducir numeros")
    while True:
      try:
        cant_postre = int(input("Ingrese la cantidad de postres "))
        break
      except:
        print("Se deben introducir numeros")  
    total = 5 * cant_combo_S + 6 * cant_combo_D + 7 * cant_combo_T + 2 * cant_postre
    print(f"Total: ${total}")
    while True:
      try:
        dinero_pago = int(input("Con cuanto paga el cliente? $"))
        if dinero_pago > total:
          break
      except:
        print("Se deben ingresar numeros y la cantidad ingresada debe ser mayor al total")
    vuelto = dinero_pago - total
    print(f"Vuelto: ${vuelto}")
    while True:
      confirmar_pedido = input("Desea confirmar el pedido? Y/N ")
      if confirmar_pedido == "Y" or confirmar_pedido == "y" or confirmar_pedido == "N" or confirmar_pedido == "n":
        break
    if confirmar_pedido == "N" or confirmar_pedido == "n":
      os.system("cls")
    elif confirmar_pedido == "Y" or confirmar_pedido == "y":
       #Creo un archivo para registrar las ventas
       with open("ventas.txt","a") as f:
         ahora = time.strftime("%c")
         f.write(f"{encargado},{ahora},{cant_combo_S},{cant_combo_D},{cant_combo_T},{cant_postre},{nombre_cliente},{total}\n")
         os.system("cls")
  if opcion == 2:
    #Guardo el horario de salida del empleado y lo añado al regitro
    salida = time.strftime("%c")
    with open("registro.txt","a") as f:
      f.writelines([f"OUT Encargad@: {encargado},{salida}\n","########################################################\n"])
    print("Bienvenido a hamburguesas IT")
    while True:
      encargado = input("Encargad@ -> ")
      if encargado.isalpha() == True:
        break
    os.system("cls")
  if opcion == 3:
    #Guardo el horario de salida del empleado y termino el programa
    salida = time.strftime("%c")
    with open("registro.txt","a") as f:
      f.writelines([f"OUT Encargad@: {encargado},{salida}\n","########################################################\n"])
    encendido = False
