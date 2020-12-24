#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que Escriu un programa que demani l'amplada i alçada d'un rectangle i 
ho dibuixi de la següent manera:
Amplada del rectangle: 5
Alçada del rectangle: 3
*****
*****
*****

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    base = int(input("Introduce longitud del lado del rectangulo: "));
    altura = int(input("Introduce longitud del otro lado del rectangulo: "));
    
    for i in range(0, altura):
        print("*" * base);