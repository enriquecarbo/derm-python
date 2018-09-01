# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:04:17 2016

Score de Pasi: Indice de afectación y severidad en Psoriasis

@author: ecarbo
"""

#!/usr/bin/env python3

print ()
print ("*" *20 + " " *5 + "Calculadora de PASI" + " " *5 + "*" *20) 
print () 
print ()


# Definir variables

score_lesion = "(0 = Sin lesion, 1 = Leve, 2 = Moderada, 3 = Severa, 4 = Muy severa) "
grado_engros = "(0 = Sin engrosamiento, 1 = Leve 0,25mm, 2 = Moderado 0,50mm, 3 = Severo 1mm, 4 = Muy severo 1,25mm) " 

eritema = int(input("Ingrese valor enrojecimiento: " + score_lesion))      
ind_engro = int(input("Ingrese valor engrosamiento: " + grado_engros))
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
else:
     xc_afec = 6

print (xc_afec)
# Iterar variables por localización
    


# Indicar PASI y severidad
PASI_CyC = (eritema + ind_engro + escama) * xc_afec * 0.1
print (PASI_CyC)
print ("El score de PASI de Cabeza y Cuello es: " + str(PASI_CyC))