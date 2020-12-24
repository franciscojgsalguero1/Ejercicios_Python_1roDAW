#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
4. Escribe un programa que permita crear una lista de palabras y que, a 
continuación, pida una palabra y elimine esa palabra de la lista.

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 4
Versión: 1.0
"""

def ejercicio4():
    
    palabras = [];
    palabra = "";
    palabra_eliminar = "";
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista "+
        "( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
            
    palabra = raw_input("Introduzca la palabra a eliminar: ").title();
    
    if (palabra in palabras):
        while (palabra in palabras):
            palabras.remove(palabra);
    else:
        print("La palabra " + palabra + " no esta dentro de la lista de" + 
            " palabras "+ str(palabras))    
    print(palabras);