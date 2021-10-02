#CARGAR LA LIBRERIA PARA INTERFAZ GRÁFICA
from tkinter import *

v= Tk ()
v.title ("ecuacuon cuadratica")
Label(v,text="coeficiente A:".grid (row=0, column=0)
Label(v,text="coeficiente B:".grid (row=1, column=0)
Label(v,text="coeficiente C:".grid (row=2, column=0)

txtA =Entry(v, width = 10)
txtA.grid (row=0, column=1)

txtB =Entry(v, width = 10)
txtB.grid (row=1, column=1)

txtC =Entry(v, width = 10)
txtC.grid (row=2, column=1)

Label (v,text="raiz X1".grid (row=4, column=0)
Label (v,text="raiz X2".grid (row=4, column=0)

txt1 =Entry(v, width = 30)
txt1.grid (row=4, column=1)
