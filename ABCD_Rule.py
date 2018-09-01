#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:04:29 2017

@author: ecarbo
"""
"""
ABCD Rule
[Stolz et al. Eur J Dermatol 1994]

To calculate the ABCD score, the 'Asymmetry, Border, Colors, and Dermoscopic structures' criteria are assessed semiquantitatively.

Each of the criteria is then multiplied by a given weight factor to yield a total dermoscopy score (TDS).

TDS values less than 4.75 indicate a benign melanocytic lesion, values between 4.8 and 5.45 indicate a suspicious lesion, and values of 5.45 or greater are highly suggestive of melanoma.
"""

print ('\n\n')
print ('*' * 10 + ' ABCD Rule - Stolz et al. ' + '*' * 10) 
print ('\n\n')
print ('\t Total Dermoscopy Score (TDS)')
print ('\n\n')
print ('ASIMMETRY')
print ('In 0, 1, or 2 axes; assess not only contour, but also colors and structures')
print ('\n')
print ('BORDER')
print ('Abrupt ending of pigment pattern at the periphery in 0-8 segments')
print ('\n') 
print ('COLOR')
print ('Presence of up to 6 colors (white, red, light brown, dark brown, blue-gray, black)')
print ('\n') 
print ('DERMOSCOPIC STRUCTURES')
print ('Presence of network, structureless or homogeneous areas, branched streaks, dots, and globules')
print ('\n\n\n') 

asim = int(input('Enter value for assimetry 0-2 \n'))
while asim > 2:
    print ('Value entered not valid.')
    asim = int(input('Enter value for assimetry 0-2 \n'))

border = int(input('Enter value for abrupt ending of pigment pattern at borders 0-8 \n'))
while border > 8:
    print ('Value entered not valid.')
    border = int(input('Enter value for abrupt ending of pigment pattern at borders 0-8 \n'))

color = int(input('Enter value for diferent colors 0-6 \n'))
while color > 6:
    print ('Value entered not valid.')
    color = int(input('Enter value for diferent colors 0-6 \n'))
    
dstruc = int(input('Enter value for dermoscopic structures 0-5 \n'))
while dstruc > 5:
    print ('Value entered not valid.')
    dstruc = int(input('Enter value for dermoscopic structures 0-5 \n'))

#Formula for TDS:
#[ (A score x 1.3) + (B score x 0.1) + (C score x 0.5) + (D score x 0.5) ]

tds = asim * 1.3 + border * 0.1 + color * 0.5 + dstruc * 0.5

print ('\n The Total Dermoscopy Score is: ', tds)
print ('\n\n')

if tds < 4.75:
    print ('"Benign melanocytic lesion"')
elif 4.75 < tds < 5.45:
    print ('"Suspicious lesion; close follow-up or excision recommended"')
else:
    print ('''"Lesion highly suggestive of MELANOMA" \n\n\n
    False-positive score (>5.45)            Reed and Spitz nevus
    sometimes observed in:                  Clark nevus with globular pattern
                                            Congenital melanocytic nevus''')

    

