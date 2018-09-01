# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 10:06:34 2016

Indice de Severidad del Acné Inversa (AISI)

Este índice mide 5 variables distribuidas en 17 regiones anatómicas
Las variables son comedones; nodulos inflamatorios o abscesos; tractos fibrosos/fìstulas; 
queloides/adherencias fibrosas, placas inflamatorias fibroescleróticas; y la valoración
de una escala visual analógica de dolor, discapacidad, disconfort.

@author: ecarbo

http://www.woundsresearch.com/article/aisi-new-disease-severity-assessment-tool-hidradenitis-suppurativa
"""

print ("\n", "\n", " "*10, "*"*10, "Cálculo del Indice de Severidad del Acné Inversa", "*"*10, "\n", "\n")



print ("""" Las regiones anatómicas a evaluar son las siguientes:
Cara, Cuero Cabelludo, Axila derecha, Axila izquierda, Submamario derecha, Submamario izquierda,
Brazo derecho, Brazo izquierdo, Tronco, Ingle derecha, Ingle izquierda, Gluteo derecho, Gluteo 
izquierdo, Genital, Perianal, Pierna derecha, Pierna Izquierda (Total = 17 zonas).""")

## Ingreso de datos

print ("\n\n¿En cuantas regiones anatómicas se observan comedones?")
comedones = int(input("Respuesta (0-17): "))
print ("\n", "¿En cuantas regiones anatómicas se observan nódulos inflamatorios o abscesos?")
nodulos = int(input("Respuesta (0-17): "))
print ("\n", "¿En cuantas regiones anatómicas se observan tractos fibrosos/fístulas?")
fis = int(input("Respuesta (0-17): "))
print ("\n", "¿En cuantas regiones anatómicas se observan queloides/adherencias fibrosas?")
quelo = int(input("Respuesta (0-17): "))
print ("\n", "¿En cuantas regiones anatómicas se observan placas inflamadas fibroescleróticas?")
plac = int(input("Respuesta (0-17): "))

print ("\n", "En una escala del 0 al 10 ¿como se ha sentido a partir de su enfermedad?")
print ("¿Cuanto dolor, disconfort o discapacidad?")
vas = int(input("Respuesta 0=Nada 10=Máximo: "))


#Hurley 

if nodulos > 0 and fis == 0 and quelo == 0 and plac == 0:
    print ("\nHurley I")
elif nodulos > 0 and (fis > 0 or quelo > 0) and plac == 0:
    print ("\nHurley II")
elif plac > 0:
    print ("\nHurley III")

#AISI

aisi = comedones + (nodulos *2) + (fis *3) + (quelo *4) + (plac *5) + vas

# the authors may design a new disease severity staging classification according to AISI values: 
# mild HS if the AISI score is less than 10; moderate HS if AISI score is between 10 and 18; 
#severe HS if AISI score is higher than 18

print ("\n\nEl Indice de Severidad en Acné Inversa (AISI) es: ", aisi)  
print ("\n")

if aisi < 10:
    print ("Forma Leve de HS")
elif 9 < aisi < 19:
    print ("Forma Moderada de HS")
else:
    print ("Forma Severa de HS")


#Bibliografia
print ("""\n\n  + Bibliografía +
----------------
            
Andrea Chiricozzi, MD; Sara Faleri, MD; Chiara Franceschini, MD; 
Raffaele Dante Caposiena Caro, MD; Sergio Chimenti, MD; and Luca Bianchi, MD
\nAISI: A New Disease Severity Assessment Tool for Hidradenitis Suppurativa
Wounds 2015;27(10):258-264""")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            