#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario que introduzca 3 calificaciones, y calcule 
la media de estas.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    calificaciones = [];
    media = 0;
    limite = 3;
    
    for i in range(0, limite):
        calificaciones.append(int(input("Introduzca una nota: ")));
    for i in calificaciones:
        media += i;
    print("La media es: " + str(media/len(calificaciones)));