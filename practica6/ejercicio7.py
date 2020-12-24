#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
7. Escribe un programa que permita crear dos listas de palabras y que, a 
continuación, escriba las siguientes listas (en las que no debe haber 
repeticiones):
• Lista de palabras que aparecen en las dos listas
• Lista de palabras que aparecen en la primera lista, pero no en la segunda
• Lista de palabras que aparecen en la segunda lista, pero no en la primera
• Lista de palabras que aparecen en ambas listas

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 7
Versión: 1.0
"""

def ejercicio7():
    
    palabra = "";
    palabras = [];
    palabras2 = [];
    lista_palabras = [];
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la primera "+
        " lista ( * para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
    
    palabra = "";
    print("");
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la segunda "+
        " lista ( * para salir): ");
        
        if (palabra != "*"):
            palabras2.append(palabra.title());
    
    for i in palabras:
        if (i not in lista_palabras):
            lista_palabras.append(i);
            
    for j in palabras2:
        if (j not in lista_palabras):
            lista_palabras.append(j);
    
    lista_palabras.sort();
    
    print("Lista de palabras que aparecen en las dos listas " + 
        str(lista_palabras));
    
    lista_palabras = [];
    
    for i in palabras:
        if (i not in palabras2 and i not in lista_palabras):
            lista_palabras.append(i);
    
    print("Lista de palabras que aparece en la primera lista pero no en la " +
        "segunda " + str(lista_palabras));
    
    lista_palabras = [];
    
    for i in palabras2:
        if (i not in palabras and i not in lista_palabras):
            lista_palabras.append(i);
    
    print("Lista de palabras que aparece en la segunda lista pero no en la " +
        "primera " + str(lista_palabras));
        
    lista_palabras = [];
    
    for i in palabras:
        if (i in palabras2 and i not in lista_palabras):
            lista_palabras.append(i);
    
    print("Lista de palabras que aparece en las dos listas es " + 
        str(lista_palabras));