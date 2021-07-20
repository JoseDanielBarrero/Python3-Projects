# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 00:02:29 2021

@author: jdbar
"""

import numpy as np
import tablaTipos as tt

# Metodo que retorna la posicion del tipo ingresado por el usuario

def buscarTipo(tipo):
    tipos = tt.getTipos()
    postipo = [x for x in range(17) if tipos[x]==tipo]
    return postipo

# Metodo que muestra las debilidades de un pokemon

def mostrar_debilidades(tipo1, tipo2, tab):
    tipos = tt.getTipos()
    deb = []
    posTipo1 = buscarTipo(tipo1)
    m1 = tab[:,posTipo1]
    if tipo2 != "":      
        posTipo2 = buscarTipo(tipo2)       
        m2 = tab[:,posTipo2]
        m3 = [m1[i]*m2[i] for i in range(17)]      
        [deb.append(x) for x in range(17) if(m3[x][0] >= 2)]
    else:
        [deb.append(x) for x in range(17) if(m1[x][0] >= 2)]
    
    print("Los tipos eficaces son: ")
    [print(tipos[i]) for i in deb]
    menu_Inicial(tab)
        
def menu_Inicial(tab):
    tipo1 = input('Ingrese el tipo #1 del pokemon: ')
    tipo2 = input('Ingrese el tipo #2 del pokemon(de no tener dejelo vacio): ')
    mostrar_debilidades(tipo1, tipo2, tab)
    
if __name__ == '__main__':
    tab = tt.tabla_de_tipos_3ra()
    menu_Inicial(tab)
    