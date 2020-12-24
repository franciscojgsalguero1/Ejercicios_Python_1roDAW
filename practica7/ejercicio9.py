#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
9. Escribe un programa que pida dos palabras las pase como parámetro a un 
procedimiento y diga si riman o no. Si coinciden las tres últimas letras tiene 
que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman
un poco y si no, que no riman.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 9
Versión: 1.0
"""

def comprobar_rima(palabra1="", palabra2=""):
    
    output = "La palabra " + palabra1 + " y la palabra " + palabra2;
    if (palabra1[-3:].upper() == palabra2[-3:].upper()):
        print(output + " riman.");
    elif (palabra1[-2:].upper() == palabra2[-2:].upper()):
        print(output + " riman un poco.");
    else:
        print(output + " no riman.");

def ejercicio9():
    
    palabra1 = raw_input("Introduzca la primera palabra: ");
    palabra2 = raw_input("Introduzca la segunda palabra: ");
    
    comprobar_rima(palabra1, palabra2);