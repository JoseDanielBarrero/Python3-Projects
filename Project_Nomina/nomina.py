# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:05:11 2021

@author: jdbarrero
"""

import numpy as np
import pandas as pd
import os
import time as t
import newDataExcel as excel

## Variable Globales

employees =[]
dataBaseName = 'baseNomina.txt'

class employee:
    def __init__(self,nombre, cedula, telefono, cargo, salario):
        self.name = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.cargo = cargo
        self.salario = salario
        self.overtime = 0
        self.saving = 0
        self.loan = 0
        self.socialSecurity = 0
        
def add_to_txt(newEmpleado):
    file = open(dataBaseName, 'w')
    dato = newEmpleado.name + '\t' + newEmpleado.cedula + '\t' + newEmpleado.telefono + '\t' + newEmpleado.cargo + '\t' + str(newEmpleado.salario) + '\t' + str(newEmpleado.overtime) + '\t' + str(newEmpleado.saving) + '\t' + str(newEmpleado.loan) + '\t' + str(newEmpleado.socialSecurity) + '\n'
    file.write(dato)
    
def new_employee():
    print("Ingrese los datos del empleado")
    nombre = input("Ingrese el nombre del empleado: ")
    cedula = input("Ingrese la cedula del empleado: ")
    telefono = input("Ingrese el telefono del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    salario = input("Ingrese el salario del empleado: $ ")
    nuevoEmpleado = employee(nombre,  cedula, telefono, cargo, salario)
    employees.append(nuevoEmpleado)
    add_to_txt(nuevoEmpleado)
    menu()

def show_all_employees():
    
    for i in employees:
        print('***************************************')
        print("Nombre empleado: ", i.name)
        print("Cedula empleado: ", i.cedula)
        print("Telefono empleado: ", i.telefono)
        print("Cargo empleado: ", i.cargo)
        print("Salario empleado: $", i.salario)
        print("Horas extras del empleado: ", i.overtime)
        print("Ahorros del empleado: ", i.saving)
        print("Prestamos del empleado: ", i.loan)
        print("Seguridad social del empleado: ", i.socialSecurity)
        print("")
        
    print('***************************************')
    print("")
    input("Pulse Enter para volver al menu...")
    menu()
   
def menu():
    print("***** Menu *****")
    print("")
    print("1. Ingresar empleado.")
    print("2. Ver empleados registrados.")
    print("3. Buscar empleado.")
    print("4. Modificar datos de empleado.")
    print("5. Generar desprendible de pago.")
    
    opcion = input("Ingrese la opcion que desea usar: ")
    
    if(opcion == "1"):
        new_employee()
    elif(opcion == "2"):
        show_all_employees()
    else:
        print("")
        print("Ingrese una opcion valida!")
        print("")
        menu()
        
if __name__ == '__main__' :
    print("Bienvenido al programa de nomina creado por: Jose Barrero :3 ")
    print("")
    menu()
    
    # new_employee()
    # print('***************************************')
    # show_all_employees()
