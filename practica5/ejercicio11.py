#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa per a jugar a endivinar un nombre (l'ordinador “pensa” el 
nombre i l'usuari l'ha d'endevinar). El programa comença demanant entre què 
nombres està el nombre a endevinar, s'”inventa” un nombre a l'atzar i després 
l'usuari va probant valors i el programa va decidint si són massa grans o 
petits. 
Pista:
import random
import time
random.seed(time.time())
minim = int(raw_input("Vamor minim: "))
maxim = int(raw_input("Vamor maxim: "))
secret = random.randint(minim, maxim)

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 11
Versión: 1.0
"""

def ejercicio11():
    
    import random;
    import time;
    random.seed(time.time());
    minimo = int(raw_input("Valor mínimo: "));
    maximo = int(raw_input("Valor máximo: "));
    numero_secreto = random.randint(minimo, maximo);
    respuesta = numero_secreto-1;
    intentos = 0;
    
    while(respuesta != numero_secreto):
        respuesta = int(input("Escribe un número: "));
        if(respuesta > numero_secreto):
            print("Demasiado grande. Vuelve a intentarlo.");
        elif (respuesta < numero_secreto):
            print("Demasiado pequeño. Vuelve a intentarlo.")
        intentos += 1;
    
    print("Correcto. Lo has intentado " + str(intentos) + " veces.")