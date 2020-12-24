#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que calcula el factorial.

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Versión: 1.0
"""

def factorial():
    
    factorial = 1;
    numero = -1;
    
    while(numero < 0):
        numero = int(input("Introduzca un número positivo: "));
    
    if(numero == 0 or numero == 1):
        factorial = 1;
    else:
        for i in range(1, numero+1):
            factorial = factorial*i;
    
    return factorial;