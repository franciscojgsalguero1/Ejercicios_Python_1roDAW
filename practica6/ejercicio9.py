#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
9. Escribe un programa que permita crear una lista de palabras y que, a 
continuación, cree una segunda lista con las palabras de la primera, pero sin 
palabras repetidas (el orden de las palabras en la segunda lista no es 
importante).

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 9
Versión: 1.0
"""

def ejercicio9():
    
    palabra = "";
    palabras = [];
    lista_palabras_sin_repetir = [];
    
    while (palabra != "*"):
        palabra = raw_input("Introduzca palabras para introducir en la lista " +
        "(* para salir): ");
        
        if (palabra != "*"):
            palabras.append(palabra.title());
    
    for i in palabras:
        if (i not in lista_palabras_sin_repetir):
            lista_palabras_sin_repetir.append(i);
    
    print("La lista sin las palabras repetidas es " + 
        str(lista_palabras_sin_repetir));