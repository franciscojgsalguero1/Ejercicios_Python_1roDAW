#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
3. Escribe un programa que lea una frase, y la pase como parámetro a un 
procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 3
Versión: 1.0
"""

def imprimir_frase(frase=""):
    for caracter in frase:
        print(caracter);

def ejercicio3():
    
    frase = raw_input("Introduzca una frase: ");
    
    imprimir_frase(frase.strip());