#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario un importe en euros y diga si el cajero automático 
le puede dar dicho importe utilizando el mismo billete y el más grande (recuerda
que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 €).
Por ejemplo: 25 euros → “el cajero te devuelve 5 billetes de 5 euros”
20 euros → “el cajero de devuelve 1 billete de 20 euros”
130 euros → “el cajero te devuelve 13 billetes de 10 euros”.

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 3 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    cajero = [500, 200, 100, 50, 20, 10, 5];
    expedir = False;
    billete = 0;
    dinero = int(input("Indique cuanto dinero quiere extraer: "));
    
    while(not expedir and billete <= len(cajero)-1):
        if(dinero%cajero[billete]==0):
            print(str(dinero) + " euros -> el cajero expedirá " + 
            str(dinero/cajero[billete]) + " billetes de " + str(cajero[billete])
            + " euros.");
            expedir = True;
        else:
            billete += 1;
    
    if(not expedir):
        print("No se puede expedir la cantidad solicitada.")