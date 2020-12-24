#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que Escriu un programa que demani 2 nombres i escrigui la suma de 
sencers des del primer nombre fins al segon.

Autor: Francisco José Gordo Salguero
Fecha: 28/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 4 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    numero1 = int(input("Escriba un número: "));
    numero2 = -1;
    suma = 0;
    ouput = "";
    
    while(numero1 > numero2):
        numero2 = int(input("Escriba un número mayor que "+ str(numero1) + ":"));
    for numero in range(numero1, numero2+1):
        suma += numero;
    output = "La suma de "+ str(numero1) + " hasta " + str(numero2) + " es: " + str(suma) + "\n";
    for numero in range(numero1, numero2+1):
        output += str(numero);
        if(numero != numero2):
            output += " + ";
    output += " = " + str(suma);
    
    print (output);