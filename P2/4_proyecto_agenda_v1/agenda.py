def borrarPantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("Presione una tecla para continuar...")

def agregar_contacto(agenda):
    borrarPantalla()
    print("\t\t\t.::: Agregar Contacto :::.")
    print("=" * 60)
    nombre = input("\t\tIngrese el nombre del contacto: ").upper().strip()
    
    if nombre in agenda:
        print("Ya existe")
    else:
        tel=input("Telefono: ").upper().strip()
        email=input("Email: ").upper().strip()
        agenda[nombre] = [tel, email]
        print("=" * 60)
        print("Accion realizada con Exito")
        
def mostrar_contactos(agenda):
    borrarPantalla()
    if not agenda:
        print("=" * 60)
        print(f"\t\tNo hay contactos")
        print("=" * 60)
    else:
        print("\t\t\t.::: Agenda :::.")
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print("=" * 60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15} {tel:<15} {email:<15}")
        print("=" * 60)
        
def buscar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto a buscar: ").upper().strip()
    if buscar in agenda:
        persona = agenda[buscar]
        print("=" * 60)
        print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
        print(f"{buscar:<15} {persona[0]:<15} {persona[1]:<15}")
        print("=" * 60)
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")
        
def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar las caracteristicas")
    buscar = input("Ingrese el nombre de la persona que desea modificar: ").upper().strip()
    
    if buscar in agenda:
        persona = agenda[buscar]
        print(f"Los datos de {buscar} son: ")
        print(f"\n\t\tTelefono: {persona[0]}")
        print(f"Email: {persona[1]}")
        
        dato = input("Ingresa el nombre de la característica que deseas modificar (Telefono/Email): ").u
        pper().strip()
        
        if dato == "TELEFONO":
            nuevo_valor = input("Ingresa el nuevo numero telefonico: ").upper().strip()
            persona[0] = nuevo_valor
            print("La operacion se realizo con exito")
        elif dato == "EMAIL":
            nuevo_valor = input("Ingresa el nuevo email: ").upper().strip()
            persona[1] = nuevo_valor
            print("=" * 60)
            print("La operacion se realizo con exito")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("=" * 60)
        print("\t..:: No esta esa persona en la agenda ::..")
    
def borrar_contacto(agenda):
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto que desea borrar: ").upper().strip()
    if buscar in agenda:
        resp = input(f"Se encontro a {buscar}, deseas eliminarla de la agenda (Si/No)?: ").upper().strip()
        if resp == "SI":
            del agenda[buscar]
        print("=" * 60)
        print("La operacion se realizo con exito")
    else:
        print("=" * 60)
        print("No existe el contacto... Vuelva a intentarlo por favor")