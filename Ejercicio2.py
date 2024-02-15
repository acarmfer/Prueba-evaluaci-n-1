capital_inicial = 1000
años = int(input("Ingrese el número de años: "))

while True:
    tasa_interes = float(input("Ingrese la tasa de interés anual (entre 1% y 10%): "))
    if 1 <= tasa_interes <= 10:
        break
    print("La tasa de interés debe estar entre 1% y 10%.")

tasa_interes_decimal = tasa_interes / 100
capital_final = capital_inicial * (1 + tasa_interes_decimal) ** años
print("El capital final es:", capital_final)