import csv
import datetime
# se estara haciendo una libreria para Validador expresiones regulares
import re
# Sistema Operativo libreria
import os
# Se importa las clases de clasePIA
from clasepia import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter

def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.TELEFONO==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

Contactos = []
with open('contacto_mobil.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            NickN=str(row[0])
            Name=str(row[1])
            Email=str(row[2])
            Cell=int(row[3])
            FechNac= datetime.date(*(int(s) for s in row[4].split('-')))
            Gasto= row[5]
            Contactos.append(Contacto(NickN,Name,Email,Cell,FechNac,Gasto))
        line_count += 1
    print(f'Processed {line_count} lines.')

CuantosElementosHay()

# Se agregan objetos a la lista.
Contactos.append(Contacto("malexheart","MELANY VILLAFAÑA BENAVIDES","melany26vb@hotmail.com",811210-8101,datetime.date(year=2002,month=3,day=26),5000))
Contactos.append(Contacto("yogi28","YAHIR HERNANDEZ GARCIA","yahirhrzQhotmail.com",818345-9824,datetime.date(year=2001,month=1,day=7),7000))
CuantosElementosHay()

#se estara haciendo un menu para darle opciones al usuario 

LimpiarPantalla = lambda: os.system('cls')
LimpiarPantalla()

def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Seleccionaste la Opcion Agregar Contacto")
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(f"Telefono: {Contactos[indice_obtenido].TELEFONO}")
                    print(f"Nombre: {Contactos[indice_obtenido].NOMBRE}")
                    print(f"Correo: {Contactos[indice_obtenido].CORREO}")

            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Ordenamiento.
                Contactos.sort(key=attrgetter('TELEFONO'),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(f"Nickname: {contacto.NICKNAME}")
                    print(f"Nombre: {contacto.NOMBRE}")
                    print(f"Email: {contacto.CORREO}")
                    print(f"Telefono: {contacto.TELEFONO}")
                    print(f"Fecha de Nacimiento: {contacto.FECHANACIMIENTO}")
                    print(f"Gastos: {contacto.GASTO}")
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()
