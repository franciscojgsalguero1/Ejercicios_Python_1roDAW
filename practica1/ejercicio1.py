#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide la longitud de un triangulo y su altura y te devuelve la 
longitud del Area.

Autor: Francisco José Gordo Salguero
Fecha: 22/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Lenguaje: Python
Practica 1 Ejercicio 1
Versión: 1.0
"""

def ejercicio1():
    base = float(input("Dígame la medida de la base del triangulo (m): "));
    altura = float(input("Dígame la medida de la altura del triangulo (m): "));
    
    area_triangulo = (base*altura)/2;
    
    print ("El Area del triangulo mide " + str(area_triangulo) + " m2")
