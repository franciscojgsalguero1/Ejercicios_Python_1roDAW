#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa que et demani noms de persones i els seus números de telèfon.
Per a terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani
el nom. El programa termina escribint noms i números de telèfon. Nota: La llista
en la que es guarden els noms i números de telèfon és [ [nom1, telef1], 
[nom2, telef2], [nom3, telef3], etc].

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 9
Versión: 1.0
"""

def telefonos_iguales(telefono_principal, telefonos):
    igual = False;
    posicion = 0;
    
    while(posicion < len(telefonos) and not igual):
        if(telefono_principal == telefonos[posicion][1]):
            igual = True;
        posicion += 1;
    return not igual;
        
def ejercicio9():
    nombre = "";
    telefono = "";
    agenda = [];
    
    while (nombre != "*"):
        nombre = raw_input("Introduzca un nombre (para salir *): ");
        
        if (nombre != "*"):
            telefono = raw_input("Introduzca un número de teléfono: ");
            if(telefonos_iguales(telefono, agenda) and len(telefono) == 9):
                agenda.append([nombre, telefono]);
            else:
                if(len(telefono) != 9):
                    print("El número de teléfono no tiene la longitud correcta.");
                else:
                    print("El número introducido ya esta registrado. \n Así que "+
                    "no se registrará este ni el nombre introducido.");
    print("Los nombres y los teléfonos son: ");
    for contacto in agenda:
        print(str(contacto[0]) + ": " + str(contacto[1]));
        