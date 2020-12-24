#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que demani un nombre (límit) i després et demani nombres fins
a què la suma dels nombres introduits superi un nombre inicial. El programa 
termina escribint la llista de nombres. 


Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 7
Versión: 1.0
"""

def ejercicio7():
    limite = 0;
    numero = 0;
    numeros = [];
    output = "un";
    
    limite = int(input("Introduce el límite: "));
    
    while(sum(numeros) < limite):
        numero = int(input("Introduce "+ output +" número: "));
        if(sum(numeros) < limite):
            output = "otro";
            numeros.append(numero);
    print(numeros);