#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario tres números y un divisor, e informa cuales de los 
números son pares y cuales impares.

He considerado que realmente pide si los números son divisibles ya que no 
tendría sentido pedir un divisor si solo quisiera que se indicase si son pares.
Diría 4 números en vez de tres y un divisor.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 3 Ejercicio 4
Versión: 1.0
"""

def ejercicio4():
    numeros = [];
    for i in range(0, 3):
        numero = int(input("Introduzca el número, por favor: "));
        numeros.append([numero, ""]);
    divisor = int(input("Introduzca el divisor por favor: "));
    
    for numero in numeros:
        if(divisor == 2):
            if(numero[0]%divisor == 0):
                numero[1] = "par";
                print ("El número " + str(numero[0]) +" es par.");
            else:
                numero[1] = "impar";
                print ("El número " + str(numero[0]) +" es impar.");
        else:
            if(numero[0]%divisor == 0):
                numero[1] = "divisible";
                print ("El número " + str(numero[0]) +" es divisible entre " 
                + str(divisor));
            else:
                numero[1] = "no es divisible";
                print ("El número " + str(numero[0]) +" no es divisible entre " 
                + str(divisor));
    if(divisor%2 == 0):
        print ("El divisor " + str(divisor) +" es par.");
    else:
        print ("El número " + str(divisor) +" es impar.");