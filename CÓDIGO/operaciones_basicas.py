#Crear un programa que verifica si una persona puede conducir 

# La persona debe ser mayor de 18 años y tener una licencia para conducir

edad= int(input('ingrese la edad:'))
licencia= str(input('¿Tiene licencia para conducir?, responda con si o no: '))

if edad>18 and licencia == 'si':
    print ('puede conducir')
else:
    print('no puede conducir')