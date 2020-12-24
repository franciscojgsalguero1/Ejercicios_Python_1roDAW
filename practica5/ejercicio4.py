#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que te demani dos nombres, de manera que el segon sigui major
que el primer. El programa termina escrivint els dos nombre tal i com es demana. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 4
Versión: 1.0
"""

def ejercicio4():
    numero_menor = int(input("Introduzca un número: "));
    numero_mayor = numero_menor-1;
    
    while (numero_mayor <= numero_menor):
        numero_mayor = int(input("Introduzca un número mayor que "+ 
        str(numero_menor) +" : "));
        if(numero_mayor <= numero_menor):
            print("El número " + str(numero_mayor) + " no es mayor que " 
                + str(numero_menor));
    print("Los números introducidos son: " + str(numero_menor) + " y " 
        + str(numero_mayor));