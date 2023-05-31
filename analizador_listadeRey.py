import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def buscar_archivo():
    nombre = entry_nombre.get()
    archivo_csv = r"C:\Users\bruno\palabras_seleccionadas.csv_{}.csv".format(nombre)

    try:
        df = pd.read_csv(archivo_csv, header=None, names=["nombre"])  # Leer el archivo con una sola columna

        # Cantidad total de palabras mayúsculas
        palabras_mayusculas = df['nombre'].loc[df['nombre'].str.isupper()]
        total_palabras_mayusculas = len(palabras_mayusculas)
        label_total.config(text="Total de palabras mayúsculas: {}".format(total_palabras_mayusculas))

        # Cantidad de palabras mayúsculas en cada rango
        cantidades_rango = []
        rango_actual = []
        for palabra in df['nombre']:
            if palabra.isupper():
                rango_actual.append(palabra)
            elif rango_actual:
                cantidades_rango.append(len(rango_actual))
                rango_actual = []

        if rango_actual:
            cantidades_rango.append(len(rango_actual))

        label_rangos.config(text="Cantidad de palabras mayúsculas en cada rango: {}".format(cantidades_rango))

        # Crear gráfico de línea
        x = list(range(1, len(cantidades_rango) + 1))
        y = cantidades_rango

        # Crear figura y gráfico de línea
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('Rango')
        ax.set_ylabel('Cantidad')
        ax.set_title('Gráfico de Línea')

        # Crear lienzo de figura en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except FileNotFoundError:
        label_total.config(text="Archivo no encontrado")
        label_rangos.config(text="")

# Crear la ventana principal
ventana = tk.Tk()

# Configurar la ventana
ventana.title("Buscar Archivo")
ventana.geometry("400x400")

# Crear el campo de entrada
label_nombre = tk.Label(ventana, text="Ingrese el nombre:")
label_nombre.pack()

entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Crear el botón de búsqueda
boton_buscar = tk.Button(ventana, text="Buscar archivo", command=buscar_archivo)
boton_buscar.pack()

# Crear etiquetas para los resultados
label_total = tk.Label(ventana)
label_total.pack()

label_rangos = tk.Label(ventana)
label_rangos.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()