#Cargar librería para GUI
from tkinter import*

#crear ventana
ventana = Tk()
ventana.title("Calculo semana santa")
ventana.minsize(300,200)

#agregar etiqueta
Label(ventana, text="año a calcular: ").grid(row=0, column=0)

#agregar caja de texto
txtAño= Entry(ventana, width=10)
txtAño.grid(row=0, column=1)
txtFecha= Entry(ventana, width=30)
txtFecha.grid(row=1, column=1)
txtFecha.configure(state=DISABLED)

def obtenerSemanaSanta():    
    #proceso
    año=int(txtAño.get())
    a= año%19
    b= año%4
    c= año%7
    d= (19*a+24)%30
    dias= d+(2*b+4*c+6*d+5)%7

    dia= 15+dias
    mes= "marzo"

    if dia>31:
        mes= "abril"
        dia= dia-31
        
    txtFecha.delete(0, END)
    txtFecha.configure(state=NORMAL)
    txtFecha.insert(0, "Empieza el " + str(dia) + "  de " + mes)

#agregar boton
Button(ventana, text="Calcular", command= obtenerSemanaSanta).grid(row=1,column=0)
