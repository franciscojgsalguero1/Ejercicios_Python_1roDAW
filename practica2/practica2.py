# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
Programa que muestra un menú al usuario de programas y pide cual quiere
ejecutar.

Autor: Francisco José Gordo Salguero
Fecha: 26/03/2020
Versión: 1.0
"""

if __name__ == "__main__":
    
    from importaciones import *
    
    def switch_demo(ejercicio):
        if(ejercicio == 0):
            print ("Gracias por utilizar nuestro programa.");
            print ("Adiós.");
        elif(ejercicio == 1):
            ejercicio1();
        elif(ejercicio == 2):
            ejercicio2();
        elif(ejercicio == 3):
            ejercicio3();
        elif(ejercicio == 4):
            ejercicio4();
        elif(ejercicio == 5):
            ejercicio5();
        elif(ejercicio == 6):
            ejercicio6();
        elif(ejercicio == 7):
            ejercicio7();
        elif(ejercicio == 8):
            ejercicio8();
        else:
            print("Se ha equivocado introduciendo los datos");
        
    ejercicio = 1;
    
    while(ejercicio != 0):
        
        for i in range(1, 9):
            print(str(i) + ') Ejercicio ' + str(i) + ".");
        print ("Si Introduce 0 saldrá de la aplicación \n");

        ejercicio = int(input("Elija el ejercicio que desea ejecutar: "));
        switch_demo(ejercicio);
