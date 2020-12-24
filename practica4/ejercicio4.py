#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que escriu un programa que demani un nombre i calculi el seu factorial.

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 4
Versión: 1.0
"""

def ejercicio4():
    numero = int(input("Introduzca un número: "));
    factorial = 1;
    for i in range(1, numero+1):
        factorial *= i;
    print(factorial);