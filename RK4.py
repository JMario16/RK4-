import customtkinter as ctk

#Colores para la interfaz
FONDO = "#0d1b2a"
FRAME_BG = "#1b263b"
TEXTO = "#e0e6ed"
BOTON = "#415a77"
HOVER = "#334b63"
BORDE = "#778da9"
ACCENT = "#a9bcd0"
FUENTE_TITULO = ("Poppins", 22, "bold")
FUENTE_TEXTO =("Times New Roman", 16)
FUENTE_EXPRESION=("STIXGeneral", 16)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana = ctk.CTk()
ventana.title("Método numerico Runge-Kutta")
ventana.geometry("1200x600")
ventana.configure(fg_color="#0d1b2a") 

# Distribución vertical 
ventana.grid_rowconfigure(0, weight=0)  
ventana.grid_rowconfigure(1, weight=0)   
ventana.grid_rowconfigure(2, weight=0) 
ventana.grid_rowconfigure(3, weight=1)

# Columnas
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

#Encabezado
frame_encabezado = ctk.CTkFrame(ventana,fg_color="#1b263b",corner_radius=10, border_width=2, border_color="#e0e1dd")
frame_encabezado.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

titulo = ctk.CTkLabel(frame_encabezado,text="Método numerico Runge-Kutta de cuarto orden",font=FUENTE_TITULO, text_color=TEXTO)
titulo.pack(pady=5)
descripcion1 = ctk.CTkLabel(frame_encabezado,text="El método de Runge-Kutta de cuarto orden es probablemente uno de los procedimientos númericos más populares, así como preciso, usado para obeter soluciones aproximadas para un problema con valores iniciales y' = f(x,y), y(x₀) = y₀.",font=FUENTE_TEXTO,text_color=ACCENT,wraplength=800)
descripcion1.pack(pady=15)

#Datos de la formula
frame_izq = ctk.CTkFrame(ventana,fg_color="#1b263b",corner_radius=10, border_width=2, border_color="#e0e1dd")
frame_izq.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
descripcion2 = ctk.CTkLabel(frame_izq,text="El conjunto de valores usado con más frecuencia para realizar el cálculo es el siguiente: ",font=FUENTE_TEXTO,text_color=ACCENT,wraplength=400,justify="left")
descripcion2.pack(padx=15,pady=10,anchor="w")
formula_k1 = ctk.CTkLabel(frame_izq,text="k₁ = f(xₙ,yₙ)",text_color=ACCENT,font=FUENTE_EXPRESION)
formula_k1.pack(padx=15,pady=2,anchor="w")
formula_k2 = ctk.CTkLabel(frame_izq,text="k₂ = f(xₙ + ½h,yₙ + ½hk₁)",text_color=ACCENT,font=FUENTE_EXPRESION)
formula_k2.pack(padx=15,pady=2,anchor="w")
formula_k3 = ctk.CTkLabel(frame_izq,text="k₃ = f(xₙ + ½h,yₙ + ½hk₂)",text_color=ACCENT,font=FUENTE_EXPRESION)
formula_k3.pack(padx=15,pady=2,anchor="w")
formula_k4 = ctk.CTkLabel(frame_izq,text="k₄ = f(xₙ + h,yₙ + hk₃)",text_color=ACCENT,font=FUENTE_EXPRESION)
formula_k4.pack(padx=15,pady=2,anchor="w")

#Ingresar datos
frame_der = ctk.CTkFrame(ventana,fg_color="#1b263b",corner_radius=10, border_width=2, border_color="#e0e1dd")
frame_der.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")
etiqueta_funcion = ctk.CTkLabel(frame_der,text="Ingrese la función dy/dx : ",text_color=ACCENT,font=FUENTE_TEXTO)
etiqueta_funcion.grid(row=0,column=0,padx=15,pady=15,sticky="w")
etiqueta_xo = ctk.CTkLabel(frame_der,text="Ingrese el valor de x₀:",text_color=ACCENT,font=FUENTE_TEXTO) 
etiqueta_xo.grid(row=1,column=0,pady=5,padx=15,sticky="w")
etiqueta_yo = ctk.CTkLabel(frame_der,text="Ingrese el valor de y(x₀):",text_color=ACCENT,font=FUENTE_TEXTO)
etiqueta_yo.grid(row=2,column=0,padx=15,pady=5,sticky="w")
etiqueta_xf = ctk.CTkLabel(frame_der,text="Ingrese el punto de aproximación (x final):",text_color=ACCENT,font=FUENTE_TEXTO)
etiqueta_xf.grid(row=3,column=0,padx=15,pady=5,sticky="w")
entry_funcion = ctk.CTkEntry(frame_der,font=FUENTE_EXPRESION,width=400)
entry_funcion.grid(row=0,column=1,padx=15,pady=5,sticky="ew")
entry_xo = ctk.CTkEntry(frame_der,font=FUENTE_EXPRESION,width=400)
entry_xo.grid(row=1,column=1,padx=15,pady=5,sticky="ew")
entry_yo = ctk.CTkEntry(frame_der,font=FUENTE_EXPRESION,width=400)
entry_yo.grid(row=2,column=1,padx=15,pady=10,sticky="ew")
entry_xf = ctk.CTkEntry(frame_der,font=FUENTE_EXPRESION,width=400)
entry_xf.grid(row=3,column=1,padx=15,pady=5,sticky="ew")

#Frame botones
frame_botones = ctk.CTkFrame(ventana,fg_color="#1b263b",corner_radius=10,border_width=2, border_color="#e0e1dd")
frame_botones.grid(row=2, column=0, columnspan=2, sticky="nsew",padx=10,pady=10)
boton_calcular = ctk.CTkButton(frame_botones,text="Calcular",text_color=ACCENT,font=FUENTE_EXPRESION,fg_color=BOTON,hover_color=HOVER)
boton_calcular.grid(row=0,column=1,padx=15,pady=5,sticky="ew")
boton_graficar = ctk.CTkButton(frame_botones,text="Graficar",text_color=ACCENT,font=FUENTE_EXPRESION,fg_color=BOTON,hover_color=HOVER)
boton_graficar.grid(row=0,column=2,padx=15,pady=5,sticky="ew")
frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_columnconfigure(1, weight=1)
frame_botones.grid_columnconfigure(2, weight=1)
frame_botones.grid_columnconfigure(3, weight=1)

#Frame para mostrar datos
frame_tabla = ctk.CTkFrame(ventana,fg_color="#1b263b",corner_radius=10, border_width=2, border_color="#e0e1dd")
frame_tabla.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

ventana.mainloop()