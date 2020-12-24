#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
2. Escribe un programa que lea el nombre y los dos apellidos de una persona (en 
tres cadenas de caracteres diferentes), los pase como parámetros a una función, 
y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el
programa por pantalla.

Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 2
Versión: 1.0
"""

def union_nombres(nombre="", apellido1="", apellido2=""):
    nombre_completo = nombre.strip().title()+ " " + apellido1.strip().title() + " " + apellido2.strip().title();
    return nombre_completo.strip();

def ejercicio2():
    nombre = raw_input("Introduzca su nombre: ");
    apellido1 = raw_input("Introduzca su primer apellido: ");
    apellido2 = raw_input("Introduzca su segundo apellido: ");
    
    print("Su nombre completo es: " + 
        union_nombres(nombre, apellido1, apellido2));
    
    