#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario el espacio recorrido por un coche y el tiempo que 
ha tardado en horas y que calcule a que velocidad media había realizado el 
recorrido.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    distancia = float(input("Que distancia ha recorrido el coche (km): "));
    tiempo = float(input("Cuanto tiempo ha tardado el coche en recorrer esa distancia? (horas): "));
    
    velocidad = distancia/tiempo;
    
    print ("El coche tenía una velocidad media de: " + str(velocidad));