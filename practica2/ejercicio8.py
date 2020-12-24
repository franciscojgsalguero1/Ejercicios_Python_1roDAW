#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que pida al usuario tres número que serán el día, mes y año. 
Comprueba que la fecha introducida es válida.
Por ejemplo:
32/01/2017->Fecha incorrecta
29/02/2017->Fecha incorrecta
30/09/2017->Fecha correcta

Autor: Francisco José Gordo Salguero
Fecha: 27/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 2 Ejercicio 8
Versión: 2.0
Hemos añadido la llamada a la función externa de año bisiesto para contemplar
este tipo de años también.
"""

from ano_bisiesto import *;

def ejercicio8():
    
    dia = int(input("Introduzca el día en formato numérico: "));
    mes = int(input("Introduzca el mes en formato numérico: "));
    ano = int(input("Introduzca el año en formato numérico (aaaa): "));
    
    fecha_correcta = True;
    fecha = "correcta";
    
    if(mes > 12 or mes < 1):
        fecha_correcta = False;
    else:
        if(dia > 31 or dia < 1):
            fecha_correcta = False;
        else:
            if(mes == 2):
                if(ano_bisiesto(ano)):
                    if(dia > 29):
                        fecha_correcta = False;
                else:
                    if(dia > 28):
                        fecha_correcta = False;
            elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
                if(dia > 30):
                    fecha_correcta = False;

    if(not fecha_correcta):
        fecha = "in"+fecha;
        
    print(str(dia)+"/"+str(mes)+"/"+str(ano)+"->Fecha " + fecha)
                