#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que demani un nombre i retorni els seus divisors.

Autor: Francisco José Gordo Salguero
Fecha: 29/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 11
Versión: 1.0
"""

def ejercicio11():
    numero = int(input("Introduzca un número: "));
    divisores = [];
    output = "";
    
    for divisor in range(1, (numero+1)/2):
        if(numero%divisor == 0):
            divisores.append(divisor);
    divisores.append(numero);
    
    output += "Los divisores de " + str(numero) + " son: ";
    for divisor in divisores:
        output += str(divisor) + " ";
    print(output);