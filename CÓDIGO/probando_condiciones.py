#probando condicionales IF, AND, OR, ALL, ELSE y NOT
#objetivo aprender estructuras de decisión en un programa en base a condiciones
#pendiente: elif implentación y uso para aprender a usarlo de mejor manera
estado_lógico= False
edad = int(input('ingresa tu edad:'))

while True:
    id = input("¿Tienes identificación?, 1 = si y 0 = no")
    if id == '1' or id== '0':
        credencial= bool(int(id))
        break
    else :
        print ('ingresa 1 o 0')
    
    
while True:
    permiso = input("¿Tienes permiso de tus padres?, 'si' o 'no':")
    if permiso == 'si' or permiso== 'no':
        permiso_padres= (permiso == 'si')
        break
    else :
        print ('ingresa si o no')
        
        
        
condiciones = [
    edad>=18,
    credencial== True
]



if edad>=18 and credencial==True: #probando la condición if (se ocupa que las dos condiciones se cumplan)
    print ('puede pasar, {condicional: and}')
else:
    print('no pasa')

if edad>=18 or credencial==True: #probando condicional or (solo necesita que se cumpla una condición)
    print ('puede pasar, {condicional: or}') 
else:
    print('no pasa')

if (16<=edad<=17 and permiso_padres==True) or edad>=18:  # se combinan las condicionales and y or para realizar la verificación
    print ('puede pasar, {condicional combinada: AND Y OR}')
else:
    print('no pasa')
    
if all(condiciones) : #probando condicional all (empaqueta mas de 2 condiciones, pueden ser mas de 20, ocupa que se cumplan todas)
    print (f'Puedes pasar tienes {edad}, con cuidado (condicional: all)')
else: 
    print ('No puedes ingresar , eres menor de edad')
    

if not estado_lógico  : #se prueba el operador NOT (invierte el estado lógico de las condiciones)
    print('el valor se lógico se invierte')
else: 
    ('no se invirtio el valor lógico')
