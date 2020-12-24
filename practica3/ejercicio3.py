#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pide al usuario si quiere calcular el área de un triángulo o un 
cuadrado, y pida los datos según que caso y muestre el resultado.

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 3 Ejercicio 3
Versión: 1.0
"""

def ejercicio3():
    print(
    """
    1) Calcular Area Triángulo.
    2) Calcular Area Cuadrado.
    """
    );
    
    respuesta = int(input("Introduzca la opción: "));
    
    if(respuesta == 1):
        triangulo();
    elif(respuesta == 2):
        cuadrado();
    else:
        print("Se ha equivocado al introducir la opción.")

def triangulo():
    base = float(input("Dígame la medida de la base del triangulo (m): "));
    altura = float(input("Dígame la medida de la altura del triangulo (m): "));
    
    area_triangulo = (base*altura)/2;
    
    print ("El Area del triangulo mide " + str(area_triangulo) + " m2");
    
def cuadrado():
    lado1 = float(input("Introduzca la longitud del cuadrado (m): "));
    lado2 = float(input("Introduzca la longitud del cuadrado (m): "));
    
    area_cuadrado = (lado1*lado2);
    
    print("El Área del cuadrado mide " + str(area_cuadrado) + " m2");