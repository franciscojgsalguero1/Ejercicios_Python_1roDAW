#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que demani primer dos nombres (màxim i mínim) i que després 
te demani 2 nombres situats entre ells. Per a terminar d'escriure nombres, 
escriu un nombre que no sigui comprès entre els dos valors inicials. El programa
termina escribint la llista de nombres. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 6
Versión: 1.0
"""

def ejercicio6():
    
    numero_minimo = int(input("Introduzca el valor mínimo: "))
    numero_maximo = numero_minimo-1;
    numero = numero_minimo+1;
    numeros = [];
    
    while (numero_maximo <= numero_minimo):
        numero_maximo = int(input("Introduzca el valor máximo (mayor que " + str(numero_minimo)+ "): "));
    
    while(numero >= numero_minimo and numero <= numero_maximo):
        numero = int(input("Introduzca un número entre " + str(numero_minimo) 
            + " y " + str(numero_maximo) + ": "));
        if(numero >= numero_minimo and numero <= numero_maximo):
            numeros.append(numero);
    print(numeros);