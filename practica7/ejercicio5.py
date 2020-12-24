#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
5. Escribe un programa que te pida una frase y una vocal, y pase estos datos 
como parámetro a una función que se encargará de cambiar todas las vocales de la
frase por la vocal seleccionada. 
Devolverá la función la frase modificada, y el programa principal la imprimirá:

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 5
Versión: 1.0
"""

def cambiarPorvocal(frase="", vocal=""):
    
    output = "";
    
    for caracter in frase.strip():
        if (caracter in ["a", "e", "i", "o", "u"]):
            output += vocal;
        else:
            output += caracter;
    
    return output;

def ejercicio5():
    
    frase = raw_input("Introduzca una frase: ");
    vocal = raw_input("Introduzca una vocal: ");
    
    frase = cambiarPorvocal(frase, vocal);
    
    print(frase);