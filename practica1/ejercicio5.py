#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide un número y dice si este es primo o no.

Autor: Francisco José Gordo Salguero
Fecha: 22/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 1 Ejercicio 5
Versión: 1.0
"""

def ejercicio5():
    numero = 0;
    divisores = [];
    i = 2;
    output = "";

    while(numero <= 0):
      numero = int(input("Introduzca un número mayor que 0: "));

    divisores.append(1);
    divisores.append(numero);

    while(i <= (int(numero/2)) and not len(divisores) > 2):
      if(numero%i == 0):
        divisores.append(i);
        output = " no";
      else:
        i +=1;

    print("El número " + str(numero) + output + " es primo.");
