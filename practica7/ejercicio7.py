#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
7. Escribe un programa que lea una frase, y la pase como parámetro a un
procedimiento. El procedimiento contará el número de vocales (de cada una) que 
aparecen, y lo imprimirá por pantalla.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 7
Versión: 1.0
"""

def contador_vocales(frase = "", vocales = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]):

    for caracter in vocales:
        for caracter2 in frase:
            if(caracter[0].upper() == caracter2.upper()):
                caracter[1] += 1;
    
    return vocales;
    
    
def ejercicio7():
    
    frase = raw_input("Introduzca una frase: ");
    vocales = contador_vocales(frase);
    
    for vocal in vocales:
        print ("El caracter " + vocal[0] + " aparece " + str(vocal[1]) + " veces.");