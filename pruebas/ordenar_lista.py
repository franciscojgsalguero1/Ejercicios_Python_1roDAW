#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que ordene una lista.

Autor: Francisco José Gordo Salguero
Fecha: 02/04/2020
Versión: 1.0
"""

def lista_ordenada(numeros):
    
    mayor = 0;
    menor = 0;
    igual = 0;
    ordenada = True;
    
    for i in range(0, len(numeros)):
        for j in range(i+1, len(numeros)):
            if(numeros[i] < numeros[j]):
                mayor += 1;
            elif( numeros[i] > numeros[j]):
                menor += 1;
            else:
                igual += 1;
    
    if((mayor != 0 and igual != 0) or (mayor != 0 and menor != 0) or (menor != 0 and igual != 0)):
        ordenada = False;
    
    return ordenada;

def ordenar_creciente(lista):
    import copy
    
    lista_auxiliar = copy.copy(lista);
    lista_ordenada = [];
    menor = lista_auxiliar[0];
    
    for i in range(0, len(lista_auxiliar)):
        for j in range(0, len(lista_auxiliar)):
            if(lista_auxiliar[j] < menor):
                menor = lista_auxiliar[j];
        lista_ordenada.append(menor);
        if (menor in lista_auxiliar):
            lista_auxiliar.remove(menor);
        if(len(lista_auxiliar) != 0):
            menor = lista_auxiliar[0];
    return lista_ordenada;

def ordenar_decreciente(lista):
    import copy
    
    lista_auxiliar = copy.copy(lista);
    lista_ordenada = [];
    mayor = lista_auxiliar[0];
    
    for i in range(0, len(lista_auxiliar)):
        for j in range(0, len(lista_auxiliar)):
            if(lista_auxiliar[j] > mayor):
                mayor = lista_auxiliar[j];
        lista_ordenada.append(mayor);
        if (mayor in lista_auxiliar):
            lista_auxiliar.remove(mayor);
        if(len(lista_auxiliar) != 0):
            mayor = lista_auxiliar[0];
    return lista_ordenada;
    

def ordenar_lista():
    lista = [];
    salir = False;
    
    print("Creemos manualmente una lista.")
    while (not salir):
        numero = raw_input("Introduzca un número (para salir *): ");
        if(numero == "*"):
            salir = True;
        else:
            lista.append(float(numero));
    
    if (lista_ordenada(lista)):
        if(len(lista) == 0):
            print("La lista esta vacía");
        else:
            print("La lista ya esta ordenada");
    else:
        print("Formas de ordenar la lista: ");
        print("1) De forma creciente.");
        print("2) De forma decreciente.");
        opcion = int(input("Como le gustaría ordenar la lista?: "));
        if(opcion == 1):
            lista = ordenar_creciente(lista);
        elif(opcion == 2):
            lista = ordenar_decreciente(lista);
        else:
            print("Error al introducir el valor.")
    return lista;


