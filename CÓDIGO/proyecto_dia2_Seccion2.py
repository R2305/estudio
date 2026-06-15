#calculadora de propinas 

totalCuenta= round(float(input("Total de cuenta:")),2)
porcentajeaplicado=round(float(input('ingrese el porcentaje de la propina sobre la cuenta:')),2)
porcentajePropina= totalCuenta* (porcentajeaplicado/100)
totalPagar= totalCuenta + porcentajePropina


print ('total de la cuentaa:',totalCuenta)
print(f'porcentaje aplicado :{porcentajeaplicado}%')
print('propina a calculada:',round(porcentajePropina,2))
print('total a pagar:',totalPagar)
