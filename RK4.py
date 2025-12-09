import customtkinter as ctk
from sympy import symbols, sympify, lambdify, sin, cos, exp, log, sqrt
import math

ctk.set_appearance_mode("dark")

# - - - PALETA COLORES Y FUENTE - - -

Fuente=("Leelawadee UI", 14)
FuenteTitulo=("Leelawadee UI", 22, "bold")
FuenteBoton=("Leelawadee UI", 14, "bold")

Blanco="#F0F0F0"
Azul="#121729"
AzulClaro="#1B2347"
AzulFuerte="#151B36"

# - - - VENTANA PRINCIPAL - - -

ventana=ctk.CTk()
ventana.title("RK4")
ventana.geometry("1100x650")
ventana.config(bg=Azul)

#--filas--
ventana.grid_rowconfigure(0, weight=0)
ventana.grid_rowconfigure(1, weight=0)
ventana.grid_rowconfigure(2, weight=0)
ventana.grid_rowconfigure(3, weight=1)

#--columnas--
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# - - - VARIABLES - - -

edo=ctk.StringVar()
edo.set("f(x, y)")
xPvi=ctk.DoubleVar()
yPvi=ctk.DoubleVar()
xFinal=ctk.DoubleVar()

# - - - FUNCIONES - - -

# - - - COMPONENTES - - -

#--frame titulo--
frame_encabezado=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_encabezado.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(20, 10), padx=20)

#--titulo--
titulo=ctk.CTkLabel(frame_encabezado, text="Método numerico Runge-Kutta de cuarto orden", font=FuenteTitulo, text_color=Blanco)
titulo.pack(pady=10)
descripcion1=ctk.CTkLabel(frame_encabezado, text="El método de Runge-Kutta de cuarto orden es probablemente uno de los procedimientos númericos más populares, así como preciso, usado para obeter soluciones aproximadas para un problema con valores iniciales y' = f(x, y), y(x₀) = y₀.", font=Fuente, text_color=Blanco, wraplength=800)
descripcion1.pack(pady=(0, 10))

#--informacion--
frame_izq=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_izq.grid(row=1, column=0, pady=10, padx=(20, 10), sticky="nsew")
descripcion2=ctk.CTkLabel(frame_izq, text="El conjunto de valores usado con más frecuencia para realizar el cálculo es el siguiente: ", font=Fuente, text_color=Blanco, wraplength=300, justify="left")
descripcion2.pack(pady=(5, 2), padx=15, anchor="w")

formula_k1=ctk.CTkLabel(frame_izq,text="k₁ = f(xₙ, yₙ)", text_color=Blanco, font=Fuente)
formula_k1.pack(pady=2, padx=15, anchor="w")
formula_k2=ctk.CTkLabel(frame_izq,text="k₂ = f(xₙ + ½h, yₙ + ½hk₁)", text_color=Blanco, font=Fuente)
formula_k2.pack(pady=2, padx=15, anchor="w")
formula_k3=ctk.CTkLabel(frame_izq, text="k₃ = f(xₙ + ½h, yₙ + ½hk₂)", text_color=Blanco, font=Fuente)
formula_k3.pack(pady=2, padx=15, anchor="w")
formula_k4=ctk.CTkLabel(frame_izq,text="k₄ = f(xₙ + h, yₙ + hk₃)", text_color=Blanco, font=Fuente)
formula_k4.pack(pady=(2, 5), padx=15, anchor="w")

#--ingresar datos--
frame_der=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_der.grid(row=1, column=1, pady=10, padx=(10, 20), sticky="nsew")

etiqueta_funcion=ctk.CTkLabel(frame_der, text="Ingrese la función dy/dx:", text_color=Blanco, font=Fuente)
etiqueta_funcion.grid(row=0, column=0, pady=5,padx=15,sticky="w")
etiqueta_xo=ctk.CTkLabel(frame_der, text="Ingrese el valor de x₀:", text_color=Blanco, font=Fuente) 
etiqueta_xo.grid(row=1, column=0, pady=5, padx=15, sticky="w")
etiqueta_yo=ctk.CTkLabel(frame_der, text="Ingrese el valor de y(x₀):", text_color=Blanco, font=Fuente)
etiqueta_yo.grid(row=2, column=0, pady=5, padx=15, sticky="w")
etiqueta_xf=ctk.CTkLabel(frame_der,text="Ingrese el punto de aproximación (x final):", text_color=Blanco, font=Fuente)
etiqueta_xf.grid(row=3, column=0, pady=5, padx=15, sticky="w")

entry_funcion=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0, textvariable=edo)
entry_funcion.grid(row=0, column=1, padx=15, pady=(15, 5), sticky="ew")
entry_xo=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0, textvariable=xPvi)
entry_xo.grid(row=1, column=1, padx=15, pady=5, sticky="ew")
entry_yo=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0, textvariable=yPvi)
entry_yo.grid(row=2, column=1, padx=15, pady=5, sticky="ew")
entry_xf=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0, textvariable=xFinal)
entry_xf.grid(row=3, column=1, padx=15, pady=(5, 15), sticky="ew")

#--botones--
frame_botones=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_botones.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

boton_calcular=ctk.CTkButton(frame_botones, width=50, text="Calcular", text_color=Blanco, font=FuenteBoton, fg_color=Azul, hover_color=AzulClaro)
boton_calcular.grid(row=0, column=1, padx=15, pady=10, ipady=2, sticky="ew")
boton_graficar=ctk.CTkButton(frame_botones, width=50, text="Graficar", text_color=Blanco, font=FuenteBoton, fg_color=Azul, hover_color=AzulClaro)
boton_graficar.grid(row=0, column=2, padx=15, pady=10, ipady=2, sticky="ew")

frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_columnconfigure(1, weight=1)
frame_botones.grid_columnconfigure(2, weight=1)
frame_botones.grid_columnconfigure(3, weight=1)

#--frame datos--
frame_tabla=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_tabla.grid(row=3, column=0, columnspan=2, pady=(10, 20), padx=20, sticky="nsew")

#--datos--

ventana.mainloop()