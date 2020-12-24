#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
4. Escribe un programa que pida una frase, y le pase como parámetro a una 
función dicha frase.
La función debe sustituir todos los espacios en blanco de una frase por un 
asterisco, y devolver el resultado para que el programa principal la imprima por
pantalla.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 4
Versión: 1.0
"""

def transformar_espacios(frase=""):
    
    frase = frase.strip();
    output = "";
    
    for caracter in frase:
        if (caracter == " "):
            output += "*";
        else:
            output += caracter;
    return output;
    
def ejercicio4():
    
    frase = raw_input("Introduzca una frase: ");
    
    frase = transformar_espacios(frase);
    
    print(frase);