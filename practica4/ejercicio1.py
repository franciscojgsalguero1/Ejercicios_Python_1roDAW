#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que  escrigui els següents nombres (la separació entre nombre és per a 
facilitar-te sabre quants de nombres s'ha d'escriure en cada bucle) i en el que 
la funció range que utilitzis tengui un únic argument (per exemple, per a la 
primera llista range(10)).

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 1
Versión: 1.0
"""

def ejercicio1():
    output = "";
    for i in range(10):
        output += str(i+1) + " ";
    output += "\n";
    
    for i in range(10):
        output += str((i+1)*2) + " ";
    output += "\n";
    for i in range(10):
        output += str(((i+1)*2)+18) + " ";
    output += "\n";
    for i in range(6):
        output += str((i*4)+10) + " ";
    output += "\n";
    for i in range(9):
        output += str((-5*i)+40) + " ";
    print(output);