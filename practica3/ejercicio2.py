#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario 5 números y diga si estos estaban en orden 
decreciente, creciente o desordenados.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 3 Ejercicio 2
Versión: 1.0
"""

def ejercicio2():
    
    numeros = [];
    ordenador = True;
    
    mayor = 0;
    menor = 0;
    igual = 0;
    
    for i in range(0, 5):
        numeros.append(float(input("Introduce un número: ")));
    
    for i in range(0, len(numeros)):
        for j in range(i+1, len(numeros)):
            if(numeros[i] < numeros[j]):
                mayor += 1;
            elif( numeros[i] > numeros[j]):
                menor += 1;
            else:
                igual += 1;
    
    if(mayor == 0 and igual == 0):
        print("Los números estan en orden decreciente.");
    elif (menor == 0 and igual == 0):
        print("Los números estan en orden creciente.");
    elif (mayor == 0 and menor == 0):
        print("Los números son todos iguales así que estan ordenados de forma"
            + " tanto creciente como decreciente.");
    elif (mayor == 0 and menor == 0 and igual == 0):
        print("La lista esta vacía.");
    else:
        print("Los números estan desordenados.");