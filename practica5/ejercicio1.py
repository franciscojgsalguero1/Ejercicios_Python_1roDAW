#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que te demani paraules i les guardi en una llista. Per a 
terminar d'introduir paraules, simplement pitja Enter. El programa termina 
escribint la llista de paraules.

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 1
Versión: 1.0
"""

def ejercicio1():
    salir = False;
    palabras = [];
    palabra = "";
    while(not salir):
        palabra = str(raw_input("Introduce una palabra (para salir introduce *): "));
        if (palabra == "*"):
            salir = True;
        else:
            palabras.append(palabra);
    print(palabras);