#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
2. Escribe un programa que permita crear una lista de palabras y que, 
    a continuación, pida una palabra y diga cuántas veces aparece esa 
    palabra en la lista

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 2
Versión: 1.0
"""

def ejercicio2():
    
    palabras = [];
    palabra = "";
    numero_palabras = 0;
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista ( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
            
    palabra = raw_input("Introduzca la palabra a buscar: ").title();
    
    palabras.sort();
    
    for i in palabras:
        if (i == palabra):
            numero_palabras += 1;
            
    print("En la lista de palabras \n " + str(palabras) + "\n hay " + 
        str(numero_palabras) + " veces la palabra " + palabra);