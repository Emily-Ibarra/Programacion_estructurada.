#Proyecto 1. Crear un proyecto que permita gestionar (administrar peliculas;
#colocar un menu de opciones para agregar, eliminar, modificar, consultar, buscar y vaciar peliculas.)
#Notas: 
#1.- utilizar funciones y mandar llamar desde otro archivo 
#2.- utilizar listas para almacenar los nombres de las peliculas 

# ===== MENÚ PRINCIPAL =====
def menu_principal():
    """Menú principal del programa"""
    global usuario_activo
    
    while usuario_activo:
        print("\n" + "="*50)
        print("\tMENU DE ADMINISTRACIÓN DE PELICULAS")
        print("="*50)
        print("\t1. Agregar")
        print("\t2. Eliminar")
        print("\t3. Modificar")
        print("\t4. Consultar")
        print("\t5. Buscar")
        print("\t6. Vaciar")
        print("\t7. Salir")
        print("="*50)
        
        opcion = input("\nSeleccione una opción (1-7): ")
        
        if opcion == '1':
            
        elif opcion == '2':
            
        elif opcion == '7':
            print("\nGracias por usar el programa. ¡Hasta pronto!")
            usuario_activo = False
        else:
            print("\nOpción no válida. Por favor, ingrese 1, 2 o 3.")
            input("Presione una tecla para continuar...")