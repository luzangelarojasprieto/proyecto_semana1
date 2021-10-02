#cargar la librería para GUI
#interfaz fráfica para el usuario
from tkinter import *

#crear la ventana
ventana = Tk()
ventana.title("calcuo semana santa")
ventana.minisize(300,200)

#agregar etiqueta
label(ventana,text="Año a calcular").grid(row=0, column =0)

#agregar caja de texto
txtAño=Entry(ventana, width=10)
txtAño.grid(row=0, column =1)

txtFecha =Entry(ventana, width=30)
txtFecha.grid(row=1, column =1)
txtFecha.configure(state=DISABLED)

def obtenerSemanaSanta():
    #obtener datos de entrada
    año = int(txtAño.get())

    #proceso
    a= año %19
    b= año %4
    c= año %7
    d= (19 * a + 24)% 30
    dias= d + (2*b + 4*c +6*d +5)%7

    dia = 15+ dias
    mes = "marzo"
    if dia > 31:
        mes =("abril")
        dia=dia-31
#mostrar datos de salida
#print("la semana santa inicia", dias, "despues del 15 de marzo")
    txtFecha.insert(0, str(dia) + "de" + mes)

#el algoritmo se pone antes del boton, porque el botron es el que lo va a llamar.
#agregar boton
Button(ventana, text="calcular",command =obtenerSemanaSanta). grid(row=1, column=0)
