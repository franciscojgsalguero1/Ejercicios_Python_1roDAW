#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que imprimeixi les taules de multiplicar del 0 al 9.

Autor: Francisco José Gordo Salguero
Fecha: 29/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 13
Versión: 1.0
"""

def ejercicio13():
    
    for i in range(0, 10):
        for j in range(0, 10):
            print(str(i) + " X " + str(j) + " = " + str(i*j));
        print("");