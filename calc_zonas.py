# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:01:07 2017

@author: ecarbo
"""


# funcion para pasi

def calc_zonas(): 
    
    # Definir variables

    score_lesion = "(0 = Sin lesion, 1 = Leve, 2 = Moderada, 3 = Severa, 4 = Muy severa) "
    grado_engros = "(0 = Sin engrosamiento, 1 = Leve 0,25mm, 2 = Moderado 0,50mm, 3 = Severo 1mm, 4 = Muy severo 1,25mm) " 

 
    eritema = int(input("Ingrese valor enrojecimiento: " + score_lesion))
    while eritema > 4:
#        print = ("\nValor ingresado incorrecto, ingrese nuevamente") 
        eritema = int(input("Ingrese valor enrojecimiento: " + score_lesion))
        
    ind_engro = int(input("Ingrese valor engrosamiento: " + grado_engros))    
    while ind_engro > 4:
#        print = ("\nValor ingresado incorrecto, ingrese nuevamente") 
        ind_engro = int(input("Ingrese valor engrosamiento: " + grado_engros))


    escama = int(input("Ingrese valor de la descamación: " + score_lesion))
    while escama > 4:
#        print = ("\nValor ingresado incorrecto, ingrese nuevamente") 
        escama = int(input("Ingrese valor de la descamación: " + score_lesion))
       
    
    xciento_afec = int(input("Ingrese porcentaje afectado (0-100%): " ))
    if xciento_afec == 0:
        xc_afec = 0
    elif 1 <= xciento_afec <10: 
        xc_afec = 1
    elif 10 <= xciento_afec <30:
        xc_afec = 2 
    elif 30 <= xciento_afec <50:
        xc_afec = 3
    elif 50 <= xciento_afec <70:
        xc_afec = 4
    elif 70 <= xciento_afec <90:
        xc_afec = 5
    elif 90 <= xciento_afec <=100:
        xc_afec = 6
   

    print (xc_afec)


# Indica PASI y severidad

    print ((eritema + ind_engro + escama) * xc_afec)


calc_zonas()