#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
10. Escribe un programa que te pida una palabra o número, pase por parámetro 
estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. 
El programa principal imprimirá el resultado de la función:

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 10
Versión: 1.0
"""

def capicua(palabra=""):
    
    output = "";
    
    for caracter in range(0, len(palabra)):
        output += palabra[len(palabra)-1-caracter];
    
    return output;

def ejercicio10():
    
    output = "";
    palabra = raw_input("Introduzca una palabra o números: ");
    
    if(palabra != capicua(palabra)):
        output = " no";
        
    print("La palabra " + palabra + output + " es capicua.");