#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que Escriu un programa que demani dos nombres i escrigui quins nombres 
son parells i quins són senars (=”impares”) des del primer fins al segon.

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 2
Versión: 1.0
"""

def ejercicio2():
    numero1 = int(input("Introduzca un número: "));
    numero2 = -1;
    output = "senar";
    while (numero1>numero2):
        numero2 = int(input("Introduzca un número mayor que " + str(numero1) + 
        ":"))
    for i in range(numero1, numero2+1):
        if (i % 2 == 0):
            output = "parell";
        else:
            output = "senar";
        print("El nombre " + str(i) + " es " + output);