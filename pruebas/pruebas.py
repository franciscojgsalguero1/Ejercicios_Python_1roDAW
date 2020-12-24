#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que muestra un menú al usuario de programas y pide cual quiere
ejecutar.

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Versión: 1.0
"""

if __name__ == "__main__":
    
    from importaciones import *
    
    def switch_demo(ejercicio):
        if(ejercicio == 0):
            print ("Gracias por utilizar nuestro programa.");
            print ("Adiós.");
        elif(ejercicio == 1):
            print(factorial());
        elif(ejercicio == 2):
            print(lista_en_orden());
        elif(ejercicio == 3):
            print(invertir());
        elif(ejercicio == 4):
            print(introducir_valor());
        elif(ejercicio == 5):
            print(ordenar_lista());
        elif(ejercicio == 6):
            cuatro_raya();
        else:
            print("Se ha equivocado introduciendo los datos");
        
    ejercicio = 1;
    
    while(ejercicio != 0):
    #    for i in range(1, 2):
    #        print(str(i) + ') Ejercicio ' + str(i) + ".");
        print("""
1) Calcular factorial.
2) Comprobar si una lista esta en orden creciente, decreciente o desordenada.
3) Invertir una lista.
4) Introducir valor dentro de una lista.
5) Ordenar una lista.
6) Jugar al cuatro en raya.
        """);
        print ("Si Introduce 0 saldrá de la aplicación \n");
        
        ejercicio = int(input("Elija el ejercicio que desea ejecutar: "));
        switch_demo(ejercicio);