#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que et demani primer un nombre i després et demani nombres 
fins a què la suma dels nombres introduïts coincideixi amb el nombre inicial. 
El programa termina escribint la llista de nombres.

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 8
Versión: 1.0
"""

def ejercicio8():
    limite = 0;
    numeros = [];
    numero = 0;
    output = "un";
    
    limite = int(input("Introduce el número límite: "));
    
    while (sum(numeros) < limite):
        numero = int(input("Introduce "+output+" número: "));
        output = "un";
        if(sum(numeros)+numero > limite):
            output = "otro";
            print(str(numero) + " es demasiado grande.");
        else:
            numeros.append(numero);
    print(numeros);