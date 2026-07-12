'''
La acamdeia requiere mantener orden en sus grimorios

'''
#Hechizos(nombre-escuela-poder-rareza-prohibido-creador)
hechizos = {
'H001': ['Llamarada Solar', 'elemental', 5, 'C', False, 'Ignus el Ardiente'],
'H002': ['Escudo de Escarcha', 'elemental', 3, 'C', False, 'Dama Fenwick'],
'H003': ['Rayo Astral', 'arcana', 7, 'R', False, 'Magíster Orin'],
'H004': ['Cadena de Almas', 'oscura', 9, 'L', True, 'El Innombrable'],
'H005': ['Portal Menor', 'arcana', 4, 'R', False, 'Selene Valdour'],
'H006': ['Toque Vampírico', 'oscura', 6, 'R', True, 'Mordath']
}
# print(hechizos["H003"][0])
#Reservas (precio(cristales)-stock(paginas))
reservas = {
'H001': [120, 8],
'H002': [90, 0],
'H003': [340, 3],
'H004': [999, 2],
'H005': [210, 5],
'H006': [450, 4],
}

def leer_opcion():
    print('''========= GRIMORIO ASTRALIS =========
1. Pergaminos por escuela de magia
2. Búsqueda de hechizos por rango de precio
3. Actualizar precio de hechizo
4. Agregar hechizo
5. Eliminar hechizo
6. Salir
====================================''')
    try:
        validacion=int(input("Ingrese una opcion: "))
        if validacion==0:
            return validacion
        elif validacion<1 or validacion>6:
            print("Debe seleccionar una opcion valida")
            return 0
        return validacion
    except ValueError:
        print("Debe seleccionar una opcion valida")
        return 0
def pergaminos_escuela(escuela,hechizos,reservas):   
    print(f"Pergaminos disponibles para la escuela de magia {escuela}: ")
    cant_pregaminos_escuela=0
    for codigo,datos in hechizos.items():
        if datos[1].lower() == escuela.lower():
            cant_pregaminos_escuela+=reservas[codigo][1]
    print(f"Total de pergaminos de {escuela} son: {cant_pregaminos_escuela}")
def busqueda_precio(p_min, p_max,hechizos,reservas):
    contador=1
    cantidad_de_hechizos_mostrados=0
    for codigo,datos in reservas.items():
        if p_min<datos[0]<p_max and datos[1]>0:
            print(f"{contador}. {hechizos[codigo][0]} | Precio: {datos[0]} | Stock: {datos[1]}")
            contador+=1
            cantidad_de_hechizos_mostrados+=1
    if cantidad_de_hechizos_mostrados==0:
        print(f"No hay hechizos disponibles en el rango de precios de {p_min} - {p_max} cristales")
def main():
    while True:
        op_menu=leer_opcion()
        if op_menu==0:
            print("Debe seleccionar una opcion valida")
        elif op_menu==1:
            escuela=input("Ingrese el nombre de la escuela de magia que desee revisar: ")
            pergaminos_escuela(escuela,hechizos,reservas)
        elif op_menu==2:
            while True:
                try:
                    p_min=int(input("Ingrese su monto minimo a pagar: "))
                    if p_min>0:
                        p_max=int(input("Ingrese su monto maximo a pagar:"))
                        if p_max>0 and p_max>p_min:
                            busqueda_precio(p_min,p_max,hechizos,reservas)
                            break
                        print("Debe ingresar valores enteros y su monto maximo tiene que ser un valor ams grande que su monto minimo")
                    print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif op_menu==3:
            print()
        elif op_menu==4:
            print()
        elif op_menu==5:
            print()
        else:
            print("Saliendo del sistema")
            break
main()



