# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:05:32 2018

@author: ecarbo

3-Point Checklist in Dermoscopy
These three criteria are (i) asymmetry, (ii) atypical pigment network, and (iii) blue-white structures
(a combination of the earlier categories of blue-whitish veil and regression structures). Moreover, these three 
criteria also had a good interobserver agreement

http://dermoscopy-ids.org/wp-content/uploads/2015/05/3pt.tutorial.pdf

"""
print ("3-Point Checklist in Dermoscopy. By Giuseppe Argenziano\n\n")

# Ingreso de variables

# Asimetria

print ("Asimetria en color y/o arquitectura en 1 o 2 axis")
asi = int(input("Si = 1  No = 0   "))
while asi not in (1,0):
    print ("Valor incorrecto. Intente nuevamente")
    asi = int(input("Si = 1  No = 0   "))

# Red atipica    
    
print ("\nRed atípica: Red pigmentadria con líneas gruesas o de distribución irregular")
red = int(input("Si = 1 No = 0   "))
while red not in (1,0):
    print ("Valor incorrecto. Intente nuevamente")
    red = int(input("Si = 1  No = 0   "))

# Estructuras azul blanquecinas

print ("\nEstructuras azul blanquecino")
ab = int(input("Si = 1 No = 0   "))
while ab not in (1,0):
    print ("Valor incorrecto. Intente nuevamente")
    ab = int(input("Si = 1  No = 0   "))
    
# Resultado
    
p3ck = asi + red + ab
print ("\nEl score de Argenziano es igual a: ", p3ck)
if p3ck > 1:
    print ("Lesión sospechosa de malignidad. Se recomienda extirpar")
elif p3ck <= 1:
    print ("Lesión no sospechosa. Se recomienda seguimiento")
print ("\nSensibilidad para Cáncer de piel /Melanoma y Basocelular/ del 91%.")
print ("Especificidad 71,9%")

