#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide dos números y dice cual es mayor o si son iguales.

Autor: Francisco José Gordo Salguero
Fecha: 22/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 1 Ejercicio 4
Versión: 1.0
"""

def ejercicio4():
    a = int(input("Introduzca el primer número: "));
    b = int(input("Introduzca el segundo número: "));
    mayor = 0;
    menor = 0;
    output = "mayor"

    if (a > b):
      mayor = a;
      menor = b;
    elif(a == b):
      mayor = menor = a;
      output = "igual";
    else:
      mayor = b;
      menor = a;

    print (str(mayor) + " es "+ output +" que " + str(menor));