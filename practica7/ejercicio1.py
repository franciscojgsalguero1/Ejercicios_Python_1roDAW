#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
1. Escribe un programa que pida un texto por pantalla, este texto lo pase como 
parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y 
luego todo en mayúsculas.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 1
Versión: 1.0
"""

def texto_mayor(palabra = "No hay texto"):
    print(palabra.upper());
    print(palabra.lower());

def ejercicio1():
    
    palabra = raw_input("Introduzca una palabra: ");
    
    texto_mayor(palabra);