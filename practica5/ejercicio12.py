#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Escriu un programa per a jugar a endevinar un nombre (l'usuari pensa un nombre i
el programa l'ha d'endevinar). El programa comença demanant entre què nombres 
està el nombre a endevinar i després intenta endevinar de què nombre es tracta. 
L'usuari va dient si el nombre que ha dit el programa és menor, major o igual al
que s'ha cercat.

Pots perfeccionar el programa fent (ampliació per a qui vagi molt sobrat):
• que al principi el programa s'asseguri de què el valor màxim és superior al 
valor mínim.
• Que el programa detecti “trampes”, per exemple, si quan dius “25” li deim 
”major” i al dir “26”
li deim “menor”, el programa ha de dir que estam fent trampes i ha de deixar de 
jugar amb nosaltres. 

Autor: Francisco José Gordo Salguero
Fecha: 31/03/2020
Curso: 1ro FPS DAW Presencial
Modulo: Programación
Practica 5 Ejercicio 12
Versión: 1.0
"""

def ejercicio12():
    minimo = 0;
    intentos = 0;
    respuesta = "diferente";
    respuesta_anterior = [];
    trampas = False;
    
    minimo = int(input("Introduzca el límite inferior: "));
    maximo = minimo-1;
    
    while(minimo >= maximo):
        maximo = int(input("Introduzca el límite superior: "));
    
    while (not trampas and respuesta != "igual" and respuesta != "Igual" and respuesta != "i"):
        
        if(respuesta == "mayor" or respuesta == "Mayor" or respuesta == "ma"):
            if(maximo-1 == numero_secreto):
                numero_secreto = maximo;
            minimo = numero_secreto;
        elif(respuesta == "menor" or respuesta == "Menor" or respuesta == "me"):
            if (minimo+1 == numero_secreto):
                numero_secreto = minimo;
            maximo = numero_secreto;
        numero_secreto = (maximo+minimo)//2;
        if(len(respuesta_anterior) != 0 and numero_secreto in respuesta_anterior):
            print ("Has hecho trampas");
            trampas = True;
        else:
            respuesta = raw_input("El número es igual, mayor o menor a " + 
            str(numero_secreto) + "? ");
        respuesta_anterior.append(numero_secreto);
        respuesta_anterior = sorted(respuesta_anterior);
        intentos += 1;
    
    if(not trampas):
        print("Gracias por jugar conmigo. He acertado a los " + str(intentos) + 
        " intentos.")
    else:
        print("No quiero seguir jugando contigo.");
        
    
    