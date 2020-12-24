#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que inserte un valor dentro de una lista;.

Autor: Francisco José Gordo Salguero
Fecha: 02/04/2020
Versión: 1.0
"""

def introducir_valor():
    
    lista = [];
    salir = False;
    
    print("Creemos manualmente una lista.")
    while (not salir):
        numero = raw_input("Introduzca un número (para salir *): ");
        if(numero == "*"):
            salir = True;
        else:
            lista.append(float(numero));
    
    salir = False;
    
    while (not salir):
        print(lista);
        valor = raw_input("Que valor desea introducir? (para salir *): ");
        if (valor == "*"):
            salir = True;
        else:
            valor = float(valor);
            indice = int(input("En que posición: "));

            if(indice >= 0 and indice <= len(lista)):
                if(indice == len(lista)):
                    lista.append(valor);
                else:
                    lista.insert(indice, valor);
            else:
                print("Error al introducer la posición donde desea introducir " + 
                    "el dato.");
                print("Vuelva a intentarlo.");
    
    return lista;
        
    