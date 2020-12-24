#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
3. Escribe un programa que permita crear una lista de palabras y que, a 
continuación, pida dos palabras y sustituya la primera por la segunda en la 
lista.

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    
    palabras = [];
    palabra = "";
    palabra_intercambiar = "";
    numero_palabras = 0;
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista "+
        "( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
            
    palabra = raw_input("Introduzca la palabra a intercambiar: ").title();
    
    palabras.sort();
    
    palabra_intercambiar = raw_input("Introduzca la palabra por la que quieres"+
    " intercambiar: ").title();
    
    if (palabra not in palabras):
        print("La palabra " + palabra_intercambiar + " no se encuentra en la"+
            " lista de palabras");
    else:
        for i in range(0, len(palabras)):
            if (palabras[i] == palabra):
                palabras[i] = palabra_intercambiar;
    print("La lista de palabras actual es \n " + str(palabras));