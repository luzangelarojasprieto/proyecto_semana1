print("programa para calcular una deuda")
#obtener datos de entrada 
monto = float(input ("monto a prestar"))
tasa = float(input ("tasa de interés"))
plazo = float(input ("número de cuotas"))
#proceso
tasa =tasa/100
x=(1+tasa)**plazo
cuota = monto * x * tasa /(x - 1)

#mostrar resultados
print("El valor de la cuota es", cuota)
