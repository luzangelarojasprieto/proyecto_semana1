#Cargar librería para GUI
from tkinter import*

#crear ventana

ventana.title("Calculo semana santa")


#agregar etiqueta


#agregar caja de texto


txtFecha= Entry(ventana, width=30)



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
