# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:35:10 2018

Calculadora para dosis acumulada de Isotretinoina.
Dermatología

@author: ecarbo
"""

import tkinter as tk 

# Funciones

def calculo():
    calculo = int(entr_dosis.get()) * int(entr_dias.get()) / int(entr_peso.get())
    return var.set(calculo)

# Ventana
ventana = tk.Tk() 
ventana.title("Dosis acumulada Isotretinoina")
ventana.geometry("400x250")
var = tk.StringVar()

# Peso: Etiqueta y entrada

lblpeso = tk.Label(ventana, text="Peso (Kg): ") 
lblpeso.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=tk.X)
entr_peso = tk.Entry(ventana)
entr_peso.pack(padx=2, pady=2, ipadx=2, ipady=2)

# Dosis: Etiqueta y entrada
lbldosis = tk.Label(ventana, text="Dosis isotretinoina (mg): ")
lbldosis.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=tk.X)
entr_dosis = tk.Entry(ventana)
entr_dosis.pack(padx=2, pady=2, ipadx=2, ipady=2)

# Dias de tratamiento: Etiqueta y entrada

lbldias = tk.Label(ventana, text="Tiempo de tratamiento (días): ")
lbldias.pack(padx=2, pady=2, ipadx=2, ipady=2, fill=tk.X)
entr_dias = tk.Entry(ventana)
entr_dias.pack(padx=20, pady=2, ipadx=2, ipady=2)

# Boton calculo DA 

btn_calc = tk.Button(ventana, text="Calcular", bg="slate gray", fg="white", command=calculo)
btn_calc.pack(side=tk.TOP)

# Resultado

res = tk.Label(ventana, textvariable=var, padx=2, pady=2)
res.pack()

ventana.mainloop()