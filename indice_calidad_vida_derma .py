# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 09:33:43 2016

Indice de Calidad de Vida Dermatológico/DLQI

@author: ecarbo
"""

print ("\n","*" *20 + " " *5 + "Indice de Calidad de Vida Dermatológico" + " " *5 + "*" *20, "\n", "\n", "\n") 
print (
        """¿Qué efectos ha tenido su problema de 
        PIEL en su vida DURANTE LA ÚLTIMA SEMANA?"""
        )
print ("\n", "\n", "\n")


#Def_Variables

us = "Durante la última semana" 
resp = "(Muchísimo = 3, Mucho = 2, Un poco = 1, Nada = 0):  " 
l_resp = [] # lista con las respuestas del usuario

#Preguntas

print ("SINTOMAS Y PERCEPCIONES" )

print ("\n", "\n", "1. " + us + " ¿ha sentido picazón, dolor o ardor en la piel?") 
l_resp.append (int(input("Respuesta: " + resp)))   
print ("\n", "2. " + us + " ¿se ha sentido avergonzado/a o cohibido/a debido a su piel?")
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "\n", "ACTIVIDADES DE LA VIDA DIARIA")
print ("\n", "\n", "3. " + us + " ¿le ha molestado su condición de la piel para hacer las compras u ocuparse de la casa o el jardín?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "4. " + us + " ¿ha influido su condición de la piel en la elección de la ropa que lleva?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "\n", "OCIO")
print ("\n", "\n", "5. " + us + " ¿ha influido su condición de la piel en alguna actividad social o recreativa?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "6. " + us + " ¿ha tenido dificultad para practicar deportes debido a su condición de la piel?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "\n", "TRABAJO - ESTUDIO")
print ("\n", "\n", "7. " + us + " ¿le ha impedido su condición de la piel trabajar o estudiar?") 
trab_est = (input("Respuesta posible: Si = s o No = n : "))
if trab_est == "n":
    print ("¿cuánta dificultad le ha ocasionado su condición de la piel en el trabajo o en sus estudios?")
    l_resp.append (int(input("Mucho = 2, Un poco = 1, Nada = 0 : ")))
else:
    l_resp.append (3)
print ("\n", "\n", "RELACIONES INTERPERSONALES - SEXUALIDAD")
print ("\n", "\n", "8. " + us + " ¿su condición de la piel le ha ocasionado dificultades con su pareja, amigos o familiares?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "9. " + us + " ¿cuánta dificultad le ha ocasionado su condición de la piel en su vida sexual?") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ("\n", "\n", "TRATAMIENTO")
print ("\n", "\n", "10. " + us + " ¿cuánta dificultad le ha ocasionado su tratamiento  de la piel, ejem. ocupándole tiempo o ensuciando o desordenando su casa??") 
l_resp.append (int(input("Respuesta: " + resp))) 
print ()    

######   DLQI = suma de l_resp

dlqi = 0

for i in l_resp:
    dlqi = dlqi + i

print ("\n", "\n", "*" *20 + " " * 5 + "RESULTADO" +  " " * 5 + "*" *20, "\n", "\n", "\n")
print ("El índice de calidad de vida dermatológico (DLQI) es: ", dlqi, "\n", "\n", "\n")

#### Mensaje que interprteta el indice DLQI

if dlqi < 2:
    print ("La enfermedad de la piel NO TIENE efecto alguno en la calidad de vida del paciente")
elif 1 < dlqi < 6:
    print ("La enfermedad de la piel tiene un efecto LEVE en la calidad de vida del paciente")
elif 5 < dlqi < 11:
    print ("La enfermedad de la piel tiene un efecto MODERADO en la calidad de vida del paciente")
elif 10 < dlqi < 21:
    print ("La enfermedad de la piel tiene un efecto Severo sobre la calidad de vida del paciente")
elif dlqi > 20:
    print ("La enfermedad de la piel tiene un efecto MUY SEVERO sobre la calidad de vida del paciente")

    