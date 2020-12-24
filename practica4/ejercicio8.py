#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que Escriu un programa que demani l'amplada d'un triangle i ho dibuixi 
de la següent manera:
Alçada del triangle: 4
*
**
***
****
***
**
*

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 8
Versión: 1.0
"""

def ejercicio8():
    altura = int(input("Introduce la altura del triangulo: "));
    
    for i in range(1, (altura+1)):
        print("*" * (i));
        
    for i in range(2, (altura+1)):
        print("*" * ((altura+1)-i));