#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
10. Escribe un programa que pida un número y a continuación escriba la lista de 
todos los divisores del número (incluidos el uno y él mismo).

Autor: Francisco José Gordo Salguero
Fecha: 13/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 6 Ejercicio 10
Versión: 1.0
"""

def ejercicio10():
    
    divisores = [];
    numero = 0;
    
    while (numero == 0):
        numero = int(input("Introduzca el número al que hay que dividir: "));
    
    for i in range(1, (numero+1)//2):
        if (numero%i == 0):
            divisores.append(i);
    divisores.append(numero);
    divisores_copia = divisores[:];
    
    for i in divisores_copia:
        divisores.append(-i);
    divisores = sorted(divisores);
    
    print("Los divisores de " + str(numero) + " son \n " + str(divisores));