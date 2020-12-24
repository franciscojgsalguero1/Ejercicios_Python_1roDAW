#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
5. Escribe un programa que permita crear dos listas de palabras y que, a 
continuación, elimine de la primera lista los nombres de la segunda lista.

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    
    palabras = [];
    palabra = "";
    palabras_eliminar = [];
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista "+
        "( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
            
    palabra = "";
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista "+
        " para eliminar (* para salir): ");
        
        if (palabra != "*"):
            palabras_eliminar.append(palabra.title());
            
    print("La lista a eliminar es " + str(palabras));
    
    for i in palabras_eliminar:
        while (i in palabras):
            palabras.remove(i);
    
    print("La lista de palabras a eliminar es " + str(palabras_eliminar));
    print("La lista resultante es " + str(palabras));