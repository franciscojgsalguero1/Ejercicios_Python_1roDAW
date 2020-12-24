#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide una temperatura en grados Celcius y los convierte en
grados Fahrenheit.

Autor: Francisco José Gordo Salguero
Fecha: 22/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 1 Ejercicio 2
Versión: 1.0
"""

def ejercicio2():
    centigrados = float(input("Dígame la temperatura en grados Celsius: "));
    
    fahrenheit = centigrados*(9./5)+32;
    
    print ("Los grados Celsius "+ str(centigrados) + " equivalen a " + 
        str(fahrenheit) + " grados Fahrenheit.")
