#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
8. Escribe un programa que pida una frase, y pase la frase como parámetro a una 
función que debe  eliminar los espacios en blanco compactar la frase. 
El programa principal imprimirá por pantalla el resultado final.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 8
Versión: 1.0
"""

def sin_espacios(frase=""):
    
    frase = frase.strip().replace(" ", "");
    
    return frase;

def ejercicio8():
    
    frase = raw_input("Introduzca una frase: ");
    
    print(sin_espacios(frase));