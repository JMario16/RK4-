import customtkinter as ctk
from tkinter import ttk,messagebox
from sympy import symbols, sympify, lambdify, sin, cos, exp, log, sqrt
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)
import math

ctk.set_appearance_mode("dark")

# - - - VARIABLES GLOBALES
valores_x = []
valores_y = []
y_solucion = []
error = []

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

# - - - FUNCIONES - - -

x,y = symbols("x y")

def convertir_funcion(texto):
    transform = standard_transformations + (implicit_multiplication_application,)
    expr = parse_expr(texto, transformations=transform)
    f = lambdify((x, y), expr, "numpy")
    return f

def on_click_calcular():
    try:
        funcion = entry_funcion.get()
        aux = entry_PVI.get()
        x0_aux, y0_aux = aux.split(",")
        x0 = float(x0_aux)
        y0 = float(y0_aux)
        h = float(entry_h.get())
        xf = float(entry_xf.get())
        calcular(x0, y0, xf, h, funcion)
    except ValueError:
        messagebox.showerror("Error", "Ingrese los campos")
    except SyntaxError:
        messagebox.showerror("Error", "Ingrese una función válida.")
    except TypeError:
        messagebox.showerror("Error", "Ingrese una función valida")
    
    
def calcular(x0, y0, xf, h, fun):
    #Limpiar frame
    for widget in frame_tabla.winfo_children():
        widget.destroy()
    
    #Limpiar arreglo de valores
    valores_x.clear()
    valores_y.clear()
    
    #funcion = sympify(fun)
    f = convertir_funcion(fun)
    
    n = int((xf - x0) / h)
    
    valores_x.append(x0)
    valores_y.append(y0)
    
    for i in range(n):
        x_actual = x0 + h*(i+1)
        valores_x.append(x_actual)
        k1, k2, k3, k4 = 0, 0, 0, 0
        k1 = f(valores_x[i],valores_y[i])
        k2 = f(valores_x[i]+0.5*h, valores_y[i]+0.5*h*k1)
        k3 = f(valores_x[i]+0.5*h, valores_y[i]+0.5*h*k2)
        k4 = f(valores_x[i]+h, valores_y[i]+h*k3)
        y_actual = valores_y[i] + ((1/6)*h)*(k1 + 2*k2 + 2*k3 + k4)
        valores_y.append(y_actual)
        
    #Mostrar la tabla con valores
    columnas = ("Iteracion","x", "y", "valor_real", "error_absoluto","error_relativo")
    
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
    # Encabezados
    tabla.heading("Iteracion", text="n")
    tabla.heading("x", text="xₙ")
    tabla.heading("y", text="yₙ")
    tabla.heading("valor_real", text="Valor real")
    tabla.heading("error_absoluto", text="Error absoluto")
    tabla.heading("error_relativo", text="% de error relativo")

    # Ancho de columnas
    tabla.column("Iteracion", width=80, anchor="center")
    tabla.column("x", width=80, anchor="center")
    tabla.column("y", width=80, anchor="center")
    tabla.column("valor_real", width=100, anchor="center")
    tabla.column("error_absoluto", width=100, anchor="center")
    tabla.column("error_relativo", width=100, anchor="center")
    
    for i in range(n+1):
        tabla.insert("", "end", values=(i,round(valores_x[i],4),round(valores_y[i],4),0,0,0))
    
    tabla.pack(fill="both", expand=True)

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
etiqueta_PVI=ctk.CTkLabel(frame_der, text="Ingrese el PVI:", text_color=Blanco, font=Fuente) 
etiqueta_PVI.grid(row=1, column=0, pady=5, padx=15, sticky="w")
etiqueta_h=ctk.CTkLabel(frame_der, text="Ingrese el tamaño de paso:", text_color=Blanco, font=Fuente)
etiqueta_h.grid(row=2, column=0, pady=5, padx=15, sticky="w")
etiqueta_xf=ctk.CTkLabel(frame_der,text="Ingrese el punto de aproximación (x final):", text_color=Blanco, font=Fuente)
etiqueta_xf.grid(row=3, column=0, pady=5, padx=15, sticky="w")

entry_funcion=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0)
entry_funcion.grid(row=0, column=1, padx=15, pady=(15, 5), sticky="ew")
entry_PVI=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0)
entry_PVI.grid(row=1, column=1, padx=15, pady=5, sticky="ew")
entry_h=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0)
entry_h.grid(row=2, column=1, padx=15, pady=5, sticky="ew")
entry_xf=ctk.CTkEntry(frame_der, fg_color=Azul, font=Fuente, width=400, border_width=0)
entry_xf.grid(row=3, column=1, padx=15, pady=(5, 15), sticky="ew")

#--botones--
frame_botones=ctk.CTkFrame(ventana, fg_color=AzulFuerte, bg_color=Azul, corner_radius=10, border_width=2, border_color=AzulFuerte)
frame_botones.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

boton_calcular=ctk.CTkButton(frame_botones, width=50, text="Calcular", text_color=Blanco, font=FuenteBoton, fg_color=Azul, hover_color=AzulClaro, command=on_click_calcular)
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