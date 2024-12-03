import tkinter as tk
from tkinter import ttk

class Materia:
    def __(self):
        self.calificacion1 = 0.0
        self.calificacion2 = 0.0
        self.calificacion3 = 0.0
        self.notaminima = 0.0
        self.nota_necesaria = 0.0
    
    def calcularNotaNecesaria(self, calificacion1, calificacion2, calificacion3, notaminima):
        # Asumiendo que el examen final cuenta como el 40% de la calificación final
        calificacion_actual = (calificacion1 + calificacion2 + calificacion3) / 3
        # Calculamos la nota necesaria en el examen final
        self.nota_necesaria = (notaminima * 2) - calificacion_actual
        if self.nota_necesaria > 10:
            self.nota_necesaria = 10  # Limitar a 10 como máximo
        elif self.nota_necesaria < 0:
            self.nota_necesaria = 0  # No puede ser negativa
        return self.nota_necesaria

def calcularNota():
    calificacion1 = 0.0
    calificacion2 = 0.0
    calificacion3 = 0.0
    notaminima = 0.0
    try:
        calificacion1 = float(input_calificacion1.get())
        etiqueta_error_calificacion1.config(text="")
    except ValueError:
        etiqueta_error_calificacion1.config(text="Introduce un número válido")
    try:
        calificacion2 = float(input_calificacion2.get())
        etiqueta_error_calificacion2.config(text="")
    except ValueError:
        etiqueta_error_calificacion2.config(text="Introduce un número válido")
    try:
        calificacion3 = float(input_calificacion3.get())
        etiqueta_error_calificacion3.config(text="")
    except ValueError:
        etiqueta_error_calificacion3.config(text="Introduce un número válido")
    try:
        notaminima = float(input_notaminima.get())
        etiqueta_error_notaminima.config(text="")
    except ValueError:
        etiqueta_error_notaminima.config(text="Introduce un número válido")
    
    # Calcular la nota necesaria con la clase Materia
    materia = Materia()
    nota_necesaria = materia.calcularNotaNecesaria(calificacion1, calificacion2, calificacion3, notaminima)
    
    etiqueta_nota_necesaria.config(text=f"Nota necesaria en el examen final: {nota_necesaria:.2f}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Nota Necesaria para Aprobar")
ventana.config(width=500, height=350)

# Etiquetas para los campos de entrada
etiqueta_calificacion1 = ttk.Label(text="Calificación 1:")
etiqueta_calificacion1.place(x=10, y=10)
etiqueta_calificacion2 = ttk.Label(text="Calificación 2:")
etiqueta_calificacion2.place(x=10, y=40)
etiqueta_calificacion3 = ttk.Label(text="Calificación 3:")
etiqueta_calificacion3.place(x=10, y=70)
etiqueta_notaminima = ttk.Label(text="Nota mínima para aprobar:")
etiqueta_notaminima.place(x=10, y=100)

# Etiquetas de error
etiqueta_error_calificacion1 = ttk.Label(text="")
etiqueta_error_calificacion1.place(x=300, y=10)
etiqueta_error_calificacion2 = ttk.Label(text="")
etiqueta_error_calificacion2.place(x=300, y=40)
etiqueta_error_calificacion3 = ttk.Label(text="")
etiqueta_error_calificacion3.place(x=300, y=70)
etiqueta_error_notaminima = ttk.Label(text="")
etiqueta_error_notaminima.place(x=300, y=100)

# Campos de entrada
input_calificacion1 = ttk.Entry()
input_calificacion1.place(x=200, y=10, width=80)
input_calificacion2 = ttk.Entry()
input_calificacion2.place(x=200, y=40, width=80)
input_calificacion3 = ttk.Entry()
input_calificacion3.place(x=200, y=70, width=80)
input_notaminima = ttk.Entry()
input_notaminima.place(x=200, y=100, width=80)

# Botón para calcular
boton_calcular = ttk.Button(text="Calcular Nota Necesaria", command=calcularNota)
boton_calcular.place(x=100, y=150)

# Etiqueta para mostrar la nota necesaria
etiqueta_nota_necesaria = ttk.Label(text="Nota necesaria en el examen final:")
etiqueta_nota_necesaria.place(x=10, y=180)

# Ejecutar la ventana
ventana.mainloop()
