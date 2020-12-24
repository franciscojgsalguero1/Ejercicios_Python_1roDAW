#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide un número y dice si es par o no (si cambias el divisor
te dice si es divisible o no).

Autor: Francisco José Gordo Salguero
Fecha: 22/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 1 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    numero = int(input("Introduzca el número, por favor: "));
    divisor = 2;
    
    if(divisor == 2):
        if(numero%divisor == 0):
            print ("El número " + str(numero) +" es par.");
        else:
            print ("El número " + str(numero) +" es impar.");
    else:
        if(numero%divisor == 0):
            print ("El número " + str(numero) +" es divisible entre " 
            + str(divisor));
        else:
            print ("El número " + str(numero) +" no es divisible entre " 
            + str(divisor));
            
            