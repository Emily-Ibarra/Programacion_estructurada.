'''lista=[
     ["Ruben",10.0,8.9,9.2],
     ["Andres",10.0,10.0,10.0],
     ["Maria",10.0,10.0,10.0]
      ]'''

def borrarPantalla():
    import os 
    os.system("cls")

def esperarTecla():
 input("Oprima cualquier tecla para cantinuar")

def menu_principal():
 print("\n\t\t\t..::: Sistema de Gestión de Calificaciones:::...\n-1.--Agregar--\n-2.--Mostrar--\n-3.--Calcular Promedios--\n-4.--SALIR--")
 opcion = input("\n\t\t Elige una opción (1-4): ").upper()
 return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  print("Agregar Calificaciones")
  lista.nombre = input("Ingresa tu nombre completo: ")
  lista.calif_1 = int("Ingresa la primera calificacion: ")
  lista.calif_2 = int("Ingresa la segunda calificacion: ")
  lista.calif_3 = int("Ingresa la tercera calificacion: ")
    