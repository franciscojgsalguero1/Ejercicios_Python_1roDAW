#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida un número que como máximo tenga tres cifras (por ejemplo 
serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número de 
más de tres cifras debe un informar con un mensaje de error como este 
“ ERROR: El número 1005 tiene más de tres cifras”.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 6
Versión: 1.0
"""

def ejercicio6():
    decimales = 0;
    numero = str(input("Introduzca un número de maximo 3 cifras: "));
    
    for cifra in numero:
        for i in range(0, 10):
            if(cifra == str(i)):
                decimales += 1;
    if(decimales > 3):
        print("ERROR: El número " + numero + " tienes más de tres cifras.")