#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que te demani nombres cada vegada més grans i els guardi 
en una llista. Per a terminar d'escriure els nombres, escriu un nombre que no 
sigui major a l'anterior. El programa termina escribint la llista de nombres. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    numeros = [];
    numero = 0;
    
    while ( len(numeros) == 0 or numero >= numeros[len(numeros)-1]):
        numero = int(input("Introduce un número: "));
        if(len(numeros) == 0 or numero > numeros[len(numeros)-1]):
            numeros.append(numero);
        
    print(numeros);