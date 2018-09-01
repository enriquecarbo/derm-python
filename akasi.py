# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:19:42 2018

@author: ecarbo

A proposed scoring system for assessing the severity of actinic keratosis on the head: actinic keratosis 
area and severity index.
T. Dirschka et. al.
JEADV 2017, 31, 1295–1302 

Actinic keratosis area and severity index (AKASI)

Total score range from 0 to 18


"""

print ("\nScore de Severidad en Queratosis Actínica")

# Funcion que obtiene un subtotal del akasi por zona evaluada

def akasisubtotal(): 

#Porcentaje de extensión de la patología.

    print ("\n\nEvaluación de la extensión del daño solar.")
    area_score = 0
    area = int(input("Que porcentaje del area esta afectada? 0-100 "))
    while area > 100:
        print ("Valor incorrecto. Ingrese nuevamente")
        area = int(input("Que porcentaje del area esta afectada? 0-100 "))

# Score del 0 al 6 de acuerdo a la superficie afectada
    
    if area == 0:
        area_score = 0
    elif 0 < area < 10:
        area_score = 1
    elif 9 < area < 30:
        area_score = 2
    elif 29 < area < 50:
        area_score = 3
    elif 49 < area < 70:
        area_score = 4
    elif 69 < area < 90:
        area_score = 5
    elif 89 < area < 101:
        area_score = 6

    print ("El porcentaje de superficie afectada es: ", area)
    print ("El score del area afectada es: ", area_score)

# Aspecto de las queratosis actínicas

    print ("\n\nAspecto de las queratosis actinicas")

# Distribucion "D"

    print ("\nDistribución")
    print ("0. Sin lesiones clinicas.")
    print ("1. Aisladas. Rodeadas de piel sana.")
    print ("2. Varias lesiones aisladas confinadas a grupos (hasta 25cm2)")
    print ("3. Lesiones coalescentes (hasta 25 cm2)")
    print ("4. Todo confluyente. Lesiones que coalescen no distinguible del area fotodañada.")
    d = int(input("Opcion 0-4:   "))
    while d not in (0,1,2,3,4):
        print ("Error!! Ingrese nuevamente")
        d = int(input("Opcion 0-4:   "))

# Eritema "E"

    print ("\nEritema")
    print ("0 = Sin eritema; 1 = Leve; 2 = Moderada; 3 = Intenso; 4 = Muy intenso")
    e = int(input("Opcion 0-4:   "))
    while e not in (0,1,2,3,4):
        print ("Error!! Ingrese nuevamente")
        e = int(input("Opcion 0-4:   "))
    
# Espesor "T" Thickness

    print ("\nEspesor")
    print ("0 = No palpable; 1 = Palpable; 2 = Facilmente palpable; 3 = Grueso e hiperqueratosico; 4 = Muy grueso")
    t = int(input("Opcion 0-4:   "))
    while t not in (0,1,2,3,4):
        print ("Error!! Ingrese nuevamente")
        t = int(input("Opcion 0-4:   "))
    

# Subtotal 

    subtotal = area_score + d + e + t 
    print ("\n\nEl subtotal del area es: ", subtotal)
    return subtotal
    
    
    
#1 AKASI subtotal del Cuero Cabelludo - Scalp
print ("\nCuero cabelludo o Scalp")    
subtot_cc = akasisubtotal()
scoretotal_cc = subtot_cc * 0.4
print ("El AKASI de cuero cabelludo es: ", scoretotal_cc)

#2 AKASI subtotal para la frente o Forehead
print ("\nFrente")
subtot_f = akasisubtotal()
scoretotal_f = subtot_f * 0.2
print ("El AKASI de la frente es: ", scoretotal_f)

#3 AKASI subtotal para la mejilla derecha 
print ("\nMejilla, pabellon, nariz y menton lado Derecho")
subtot_r = akasisubtotal()
scoretotal_r = subtot_r * 0.2
print ("El AKASI del lado derecho de la cara es: ", scoretotal_r)

#4 AKASI subtotal para la mejilla izquierda
print ("\nMejilla, pabellon, nariz y menton lado Izquierdo")
subtot_l = akasisubtotal()
scoretotal_l = subtot_l * 0.2
print ("El AKASI del lado izquierdo de la cara es: ", scoretotal_l)

# Impresion de los resultados

print ("\n\nEl AKASI de cuero cabelludo es: ", scoretotal_cc)
print ("El AKASI de la frente es: ", scoretotal_f)
print ("El AKASI del lado derecho de la cara es: ", scoretotal_r)
print ("El AKASI del lado izquierdo de la cara es: ", scoretotal_l)

akasi = scoretotal_cc + scoretotal_f + scoretotal_r + scoretotal_l
print ("\n\nEl AKASI total es: ", akasi)
