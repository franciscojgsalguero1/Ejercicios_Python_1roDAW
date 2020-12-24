#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que te demani nombres i els guardi en una llista. Per a 
terminar d'introduir nombres, simplement pitja Enter. El programa termina 
escrivint la llista de nombres. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 2
Versión: 1.0
"""

def ejercicio2():
    salir = False;
    numeros = [];
    numero = "";
    while(not salir):
        numero = raw_input("Introduce una palabra (para salir introduce *): ");
        if (numero == "*"):
            salir = True;
        else:
            numero = int(numero);
            numeros.append(numero);
    print(numeros);
