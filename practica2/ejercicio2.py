#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide dos n�meros y dice cual es mayor o si son iguales.

Autor: Francisco Jos� Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programaci�n
Practica 2 Ejercicio 2
Versi�n: 1.0
"""

def ejercicio2():
    a = int(input("Introduzca el primer n�mero: "));
    b = int(input("Introduzca el segundo n�mero: "));
    mayor = 0;
    menor = 0;
    output = "mayor"

    if (a > b):
      mayor = a;
      menor = b;
    elif(a == b):
      mayor = menor = a;
      output = "igual";
    else:
      mayor = b;
      menor = a;

    print (str(mayor) + " es "+ output +" que " + str(menor));