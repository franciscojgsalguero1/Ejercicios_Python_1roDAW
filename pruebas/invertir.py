#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que ordene en orden inverso una lista.

Autor: Francisco José Gordo Salguero
Fecha: 02/04/2020
Versión: 1.0
"""

def invertir():
    lista_original = [];
    lista_revertida = [];
    salir = False;
    
    while (not salir):
        numero = raw_input("Introduzca un número (para salir *): ");
        if(numero == "*"):
            salir = True;
        else:
            lista_original.append(numero);
    
    for i in range(0, len(lista_original)):
        lista_revertida.append(lista_original[len(lista_original)-i-1]);
    
    return lista_revertida;
    