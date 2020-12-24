#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que demani notes i les guardi en una llista. Per a terminar 
d'introduir notes, escriu una nota que no estigui entre 0 i 10. El programa 
termina escrivint la llista de notes. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    nota = 0;
    notas = [];
    
    while (nota >= 0 and nota < 11):
        nota = int(input("Introduzca una nota entre 0 y 10: "));
        
        if (nota >=0 and nota < 11):
            notas.append(nota);
            
    print(notas);
        

    