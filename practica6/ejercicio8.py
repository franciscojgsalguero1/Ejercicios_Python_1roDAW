#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
8. Escribe un programa que permita crear una lista de palabras y que, a 
continuación, ordene la lista por orden alfabético.

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 8
Versión: 1.0
"""

def ejercicio8():
    
    palabra = "";
    palabras = [];
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista " +
        "(* para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
    
    palabras = sorted(palabras);
    
    print("La lista de palabras ordenadas por orden alfabético " + str(palabras));