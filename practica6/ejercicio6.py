#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
6. Escribe un programa que permita crear una lista de palabras y que, a 
continuación, cree una segunda lista igual a la primera, pero al revés (no se 
trata de escribir la lista al revés, sino de crear una lista distinta).

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 6
Versión: 1.0
"""

def ejercicio6():
    
    palabra = "";
    palabras = [];
    palabras_copia = [];
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista "+
        "( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
    
    for i in range(0, len(palabras)):
        palabras_copia.append(palabras[len(palabras)-1-i]);
    
    print(palabras);
    print(palabras_copia);
    