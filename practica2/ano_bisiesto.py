#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que verifica si un año es bisiesto o no.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 8.2
Versión: 1.0
"""

def ano_bisiesto(ano):
    divisor4, divisor100, divisor400  = 4, 100, 400;
    ano_bisiesto = True;
    
    if(ano%divisor4 == 0):
        if(ano%divisor100 == 0) and (ano%divisor400 != 0):
            ano_bisiesto = False;
    else:
        ano_bisiesto = False;
    return ano_bisiesto;

"""
if(ano_bisiesto(1920)):
    print("El año es bisiesto.");
else:
    print("El año no es bisiesto.");
"""
