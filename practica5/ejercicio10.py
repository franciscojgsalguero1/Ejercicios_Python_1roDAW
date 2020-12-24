#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que et demani els noms i notes d'alumnes. Si escrius una nota
fora de l'interval de 0 a 10, el programa entendrà que no vols introduir més 
notes d'aquest alumne. Si no escrius el nom, el programa entendrà que no vols 
introduir més alumnes. Nota: La llista en la que es guarden els noms i notes és 
[ [nom1, nota1, nota2, etc], [nom2, nota1, nota2, etc], 
[nom3,nota1, nota2, etc], etc].

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 10
Versión: 1.0
"""

def ejercicio10():
    
    alumnos = [];
    notas = [];
    nota = 0;
    alumno = "";
    output = "";
    
    while(alumno != "*"):
        alumno = raw_input("Introduza un nombre de alumno: ");
        if(alumno != "*" and alumno != "" and alumno != " "):
            notas.append(alumno);
            nota = 0;
            while(nota >= 0 and nota <= 10):
                nota = float(input("Introduzca una nota: "));
                if(nota >= 0 and nota <= 10):
                    notas.append(nota);
            alumnos.append(notas);
            notas = [];
        else:
            if(alumno == "*"):
                print(alumnos);
            else:
                print("Ha introducido más el nombre del alumno");
                
    print("Las notas de los alumnos son: ");
    for alumno in alumnos:
        for notas in alumno:
            if(notas == alumno[0]):
                output += str(notas) + ": ";
            elif (notas == alumno[len(alumno)-1]):
                output += str(notas);
            else:
                output += str(notas) + " - ";
            if (len(alumno) == 1):
                output += "NP";
        print(output);
        output = "";
            
            