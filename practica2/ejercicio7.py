#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario el precio de un producto y el nombre del producto 
y muestre el mensaje con el precio del IVA (21%). 
Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 
euros en total”.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 7
Versión: 1.0
"""

def ejercicio7():
    nombre_producto = raw_input("Introduzca el nombre del producto: ");
    
    precio_producto = float(input("Introduzca el precio del producto: "));
    IVA = 0.21;
    
    print ("Tu " + nombre_producto + " vale " + str(precio_producto) + " euros "+
        "y con el " + str(IVA*100) + "% de IVA se queda en " + 
        str(precio_producto*(1+IVA)) + " euros en total.");