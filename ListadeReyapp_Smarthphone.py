import os
import tkinter as tk
import csv
import pandas as pd

# Función para manejar el evento de ingresar un nuevo paciente
def ingresar_paciente():
    ventana_inicio.pack_forget()  # Ocultar la pantalla inicial
    ventana_datos.pack()  # Mostrar la pantalla de ingreso de datos

def guardar_palabra(palabra):
    archivo_csv = "/storage/emulated/0/Download/palabras_seleccionadas.csv_{}.csv".format(nombre)
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([palabra])

# Función para manejar el evento de guardar los datos del paciente
def guardar_datos(): 
    global nombre
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    puesto = entry_puesto.get()

    guardar_palabra(nombre)
    guardar_palabra(edad)
    guardar_palabra(puesto)   

    ventana_datos.pack_forget()  # Ocultar la pantalla de ingreso de datos

    mostrar_palabras()

# Función para mostrar las palabras y la ronda
def mostrar_palabras():

    global ronda_actual, palabras_elegidas

    # Actualizar el número de ronda
    label_ronda.config(text="Ronda {}".format(ronda_actual))

    # Mostrar las palabras en botones
    ventana_palabras.pack()

    if ronda_actual == 6:
      # Actualizar la lista de palabras elegidas
      palabras_elegidas.append(palabrasB.copy())
      for i, palabra in enumerate(palabrasB):
        botones_palabras[i].config(text=palabra, command=lambda p=palabra: guardar_palabra(p))

    else:
      palabras_elegidas.append(palabrasA.copy())
      # Actualizar los botones de palabras
      for i, palabra in enumerate(palabrasA):
        botones_palabras[i].config(text=palabra, command=lambda p=palabra: guardar_palabra(p))


def reiniciar_colores():
    for boton in botones_palabras:
        boton.config(bg="#F0F0F0")  # Reiniciar al color de fondo predeterminado

# Función para avanzar a la siguiente ronda
def siguiente_ronda():
    global ronda_actual

    reiniciar_colores()

    # Incrementar el número de ronda
    guardar_palabra(ronda_actual)
    ronda_actual += 1

    if ronda_actual > 7:
        # Finalizar el juego después de la ronda 7
        ventana_palabras.pack_forget()
        ventana_final.pack()
    else:
        # Mostrar las palabras y la ronda siguiente
        ventana_palabras.pack_forget()
        mostrar_palabras()

# Listas de palabras
palabrasA = ['TAMBOR', 'CAFE', 'SOMBRERO', 'COLOR', 'CORTINA', 'PARIENTE', 'GRANJERO', 'CASA', 'TIMBRE', 'LUNA', 'NARIZ', 'RIO', 'ESCUELA', 'JARDIN', 'PAVO']

palabrasB = ["ESCRITORIO","MONTANIA","CORDERO","COLADOR","VASO","REVOLVER","PAJARO","TOALLA","LAPIZ","ZAPATO","NUBE","IGLESIA","ESTUFA","BOTE","PEZ"]

# Variables globales
ronda_actual = 1
palabras_elegidas = []

# Crear la ventana principal
ventana = tk.Tk()

# Configurar la ventana
ventana.title("Interfaz gráfica")
ventana.geometry("400x300")

# Crear la pantalla inicial
ventana_inicio = tk.Frame(ventana)

label_inicio = tk.Label(ventana_inicio, text="¡Bienvenido! Ingrese un nuevo paciente")
label_inicio.pack(pady=20)

boton_ingresar = tk.Button(ventana_inicio, text="Ingresar nuevo paciente", command=ingresar_paciente)
boton_ingresar.pack()

# Crear la pantalla de ingreso de datos
ventana_datos = tk.Frame(ventana)

label_nombre = tk.Label(ventana_datos, text="Nombre y Apellido:")
label_nombre.pack()

entry_nombre = tk.Entry(ventana_datos)
entry_nombre.pack()

label_edad = tk.Label(ventana_datos, text="Edad:")
label_edad.pack()

entry_edad = tk.Entry(ventana_datos)
entry_edad.pack()

label_puesto = tk.Label(ventana_datos, text="Puesto:")
label_puesto.pack()

entry_puesto = tk.Entry(ventana_datos)
entry_puesto.pack()

boton_guardar = tk.Button(ventana_datos, text="Guardar", command=guardar_datos)
boton_guardar.pack()

#Crear la pantalla de las palabras

def cambiar_color(event):
    boton = event.widget
    boton.config(bg="pale green")  # Cambiar a un verde más claro

ventana_palabras = tk.Frame(ventana)

label_ronda = tk.Label(ventana_palabras, text="Ronda {}".format(ronda_actual))
label_ronda.pack()

ventana_botones = tk.Frame(ventana_palabras)
ventana_botones.pack()

botones_palabras = []

if ronda_actual == 6:
    for i, palabra in enumerate(palabrasB):
        boton_palabra = tk.Button(ventana_botones, text=palabra, width=12, height=2)
        boton_palabra.bind("<Button-1>", cambiar_color)
        boton_palabra.grid(row=i % 3, column=i // 3, padx=5, pady=5)
        botones_palabras.append(boton_palabra)

else:
    for i, palabra in enumerate(palabrasA):
        boton_palabra = tk.Button(ventana_botones, text=palabra, width=12, height=2)
        boton_palabra.bind("<Button-1>", cambiar_color)
        boton_palabra.grid(row=i % 3, column=i // 3, padx=5, pady=5)
        botones_palabras.append(boton_palabra)

ventana_palabras.pack()

#Crear el botón "Siguiente ronda"
boton_siguiente = tk.Button(ventana_palabras, text="Siguiente ronda", command=siguiente_ronda)
boton_siguiente.pack(pady=10)

#Crear la pantalla final
ventana_final = tk.Frame(ventana)
label_final = tk.Label(ventana_final, text= "Gracias")
label_final.pack(pady=20)


#Mostrar la pantalla inicial al inicio
ventana_inicio.pack()

#Ejecutar el bucle principal de la ventana
ventana.mainloop()