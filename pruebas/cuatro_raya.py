#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa para jugar al 4 en raya.

Autor: Francisco José Gordo Salguero
Fecha inicio: 02/04/2020
Fecha fin : 13/04/2020
Versión: 1.0
"""

def crear_jugadores():
    
    jugadores = [];
    
    for i in range(0, 2):
        nombre = raw_input("Introduzca su nombre: ");
        if(i == 0):
            ficha = "O";
        else:
            ficha = "X";
        jugadores.append([nombre.title(), ficha]);
        
    return jugadores;

def funcion_crear_columnas (columnas):
    
    columna = [];
    
    if (columnas != 0):
        for crear_columnas1 in range(0, columnas):
            columna.append(" ");
            
    return columna;

def crear_tablero (filas, columnas):
    
    tablero_creado = [];
    
    if (filas != 0 and columnas != 0):
        
        for crear_filas in range(0, filas):
            
                tablero_creado.append(funcion_crear_columnas(columnas));
                
    else:
        
        print("No se puede crear tablero.");
        
    return tablero_creado;
    
def mostrar_tablero(tablero):
    
    output = "";
    
    for filas in range(0, len(tablero[0])):
        for columnas in range(0, len(tablero)):
            
            if(columnas == 0 and filas == 0):
                
                for numeros in range(1, len(tablero)+1):
                    if (numeros == 1):
                        output = "| ";
                    output += str(numeros) + " | ";
                output += "\n";
            
            if(columnas == 0):
                
                output += "| ";
            
            output += tablero[columnas][filas] + " | ";
        output += "\n";
        
    print(output)

def poner_ficha(tablero, jugador):
    
    puesta = True;
    nombre = jugador[0];
    ficha = jugador[1];
    posiciony = 0;
    victoriax = 0;
    victoriay = 0;
    
    mostrar_tablero(tablero)
    
    print("Turno jugador: " + str(nombre))
    posicion = int(input("Donde quiere introducir la ficha?: "));
    
    if(posicion > 0 and posicion <= len(tablero)):
        if(tablero[posicion-1][len(tablero[posiciony])-1] == " "):
            tablero[posicion-1][len(tablero[posiciony])-1] = ficha;
            victoriax = posicion-1;
            victoriay = len(tablero[posiciony])-1;
        elif (tablero[posicion-1][0] == " "):
            while(tablero[posicion-1][posiciony] == " "):
                posiciony += 1;
            posiciony -= 1;
            tablero[posicion-1][posiciony] = ficha;
            victoriax = posicion-1;
            victoriay = posiciony;
        else:
            puesta = False;
    else:
        puesta = False;
        
    return [puesta, victoriax, victoriay];

def comprobar_victoria(posicion, posiciony, tablero):
    
    victoria = False;
    ficha = tablero[posicion][posiciony];
    ficha_encontrada = False;
    fichas = 0;
    
    for posicionx in range(0, len(tablero)):
        if(tablero[posicionx][posiciony] == ficha):
            ficha_encontrada = True;
        else:
            ficha_encontrada = False;
            fichas = 0;
        if(ficha_encontrada):
            fichas +=1;
            if(fichas == 4):
                victoria = True;
        else:
            fichas = 0;
            
    fichas = 0;
            
    if (not victoria):
        for posiciony2 in range(0, len(tablero[0])):
            if(tablero[posicion][posiciony2] == ficha):
                ficha_encontrada = True;
            else:
                ficha_encontrada = False;
                fichas = 0;
            if(ficha_encontrada):
                fichas +=1;
                if(fichas == 4):
                    victoria = True;
            else:
                fichas = 0;
    
    fichas = 0;
    
    if (not victoria):
        posicioninicio = [];
        posicioninicio = posicion_inicio(posicion, posiciony, tablero);
        posicionx3, posiciony3 = posicioninicio[0], posicioninicio[1];
        posicionx4 = posicioninicio[2];    
        posiciony4 = posicioninicio[3];
        
        while( posicionx3 >= 0 and posicionx3 < len(tablero) and posiciony3 >= 0
            and posiciony3 < len(tablero[0]) and not victoria):
                
                if(tablero[posicionx3][posiciony3] == ficha):
                    ficha_encontrada = True;
                else:
                    ficha_encontrada = False;
                    fichas = 0;

                if(ficha_encontrada):
                    fichas +=1;
                    if(fichas == 4):
                        victoria = True;
                else:
                    fichas = 0;

                posicionx3 += 1;
                posiciony3 -= 1;
                
        while( posicionx4 >= 0 and posicionx4 < len(tablero) and posiciony4 >= 0
            and posiciony4 < len(tablero[0]) and not victoria):
                
                if(tablero[posicionx4][posiciony4] == ficha):
                    ficha_encontrada = True;
                else:
                    ficha_encontrada = False;
                    fichas = 0;

                if(ficha_encontrada):
                    fichas +=1;
                    if(fichas == 4):
                        victoria = True;
                else:
                    fichas = 0;

                posicionx4 += 1;
                posiciony4 += 1;
                
    return victoria;

def posicion_inicio(posicionx, posiciony, tablero):
    
    px1 = posicionx;
    py1 = posiciony;
    px2 = posicionx;
    py2 = posiciony;
        
    while(px1 > 0 and py1 < len(tablero[0])):
        px1 -= 1;
        py1 += 1;
        
    while(px2 > 0 and py2 < len(tablero[0])):
        px2 -= 1;
        py2 -= 1;
    
    return [px1, py1, px2, py2]

def comprovar_empate(tablero):
    empate = True;
    for i in tablero:
        for j in i:
            if (j == " "):
                empate = False;
    return empate;

def cuatro_raya():
    
    victoria = False;
    empate = False;
    turnos = 0;
    filas_tablero = 7;
    columnas_tablero = 6;
    
    jugadores = crear_jugadores();
    tablero = crear_tablero(filas_tablero, columnas_tablero);
    
    while(not victoria and not empate):
        
        jugador = turnos%2;
        jugada = poner_ficha(tablero, jugadores[jugador]);
        
        if(jugada[0]):
            
            victoria = comprobar_victoria(jugada[1], jugada[2], tablero);
            
            if (not victoria):
                empate = comprovar_empate(tablero);
                if (not empate):
                    turnos +=1;
    
    mostrar_tablero(tablero);
    
    if (victoria):
        print("Ha ganado el jugador " + jugadores[jugador][0]);
    elif (empate):
        print("Los jugadores han empatado");
    else:
        print("Los jugadores han empatado2");