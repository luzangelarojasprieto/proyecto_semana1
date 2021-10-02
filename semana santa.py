print("programa para obtener la fecha de inicio de la semana santa")

#obtener datos de entrada
año = int(input("año a calcular"))

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

print("la semana santa inicia el",dia, "de", mes) 
