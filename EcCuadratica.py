#Cargar la libreria para GUI
from tkinter import*
from tkinter import messagebox

v = Tk()
Label(v, text="Coeficiente A:").grid(row=0,column=0)
Label(v, text="Coeficiente B:").grid(row=1,column=0)
Label(v, text="Coeficiente C:").grid(row=2,column=0)

txtA=Entry(v,width=10)
txtA.grid(row=0,column=1)
txtB=Entry(v,width=10)
txtB.grid(row=1,column=1)
txtC=Entry(v,width=10)
txtC.grid(row=2,column=1)

Label(v, text="raiz x1:").grid(row=4,column=0)
Label(v, text="raiz x2:").grid(row=5,column=0)

txtx1=Entry(v,width=30)
txtx1.grid(row=4,column=1)
txtx1.configure(state=DISABLED)
txtx2=Entry(v,width=30)
txtx2.grid(row=5,column=1)
txtx2.configure(state=DISABLED)

def calcularRaices():
    #Obtener Datos de entrada
    a=float(txtA.get())
    b=float(txtB.get())
    c=float(txtC.get())

    #proceso
    if a !=0:
        r=b**2-4*a*c
    else:
        messagebox.showerror("Error al calcular","La Ecuación no es cuadratica")

Button(v,text="Calcular", command=calcularRaices).grid(row=3, column=0, columnspan=2)
