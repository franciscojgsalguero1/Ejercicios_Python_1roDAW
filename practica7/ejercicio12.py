#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
12. Escribir un programa que lea una frase, y pase ésta como parámetro a una 
función que debe contar el número de palabras que contiene. Debe imprimir el 
programa principal el resultado. Asumir que cada palabra está separada por un 
sólo blanco:
1. Asumir que cada palabra está separada por un sólo blanco.
2. No se sabe cómo están separadas las palabras. Pueden estar separadas por más 
de un blanco o por signos de puntuación.


Autor: Francisco José Gordo Salguero
Fecha: 14/04/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 7 Ejercicio 12
Versión: 1.0
"""

def contar_Palabras(frase="", formato=1):
    
    numero_palabras = 0;
    frase = frase.strip();
    if(formato == 1):
        
        caracter_anterior = "";
        numero_palabras += 1;
        
        for caracter in frase:
            if (caracter == " " and caracter_anterior != " "):
                numero_palabras += 1;
                caracter_anterior = caracter;
            else:
                
                caracter_anterior = caracter;
                
    elif(formato == 2):
        
        tupla = ("!","·", ".","$","%","/","(",")","=","?","¿","¡","!",",");
        
        caracter_anterior = "";
        numero_palabras += 1;
        
        for caracter in frase:
            if ((caracter == " " or caracter in tupla) and caracter_anterior != " "):
                if (caracter == " " and caracter_anterior in tupla):
                    caracter_anterior = caracter;
                else:
                    numero_palabras += 1;
                caracter_anterior = caracter;
            else:
                caracter_anterior = caracter;
        
        if(frase[len(frase)-1] in tupla):
            numero_palabras -= 1;
            
    else:
        print("Error al introducir el formato.");
    
    return numero_palabras;

def ejercicio12():
    
    frase = raw_input("Introduzca una frase: ");
    
    print(contar_Palabras(frase, 2));