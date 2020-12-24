#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario pida al usuarios 5 números y diga cual es el mayor 
y cual el menor.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 3 Ejercicio 1
Versión: 1.0
"""

def ejercicio1():
    numeros = [];
    for i in range(0, 5):
        numeros.append(int(input("Introduce un número: ")));
    mayor = numeros[0];
    
    for i in numeros:
        if(mayor < i):
            mayor = i;
    print("El mayor es: " + str(mayor));
    