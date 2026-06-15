#Estas programando un sistema para verificar si una persona puede acceder a un concierto exlucisvo. El sistema revisa las siguientes condiciones:

#Debe tener una entrada válida
#debe ser mayor de edad 
#No debe estar en la lista negra
#El sistema debe imprimir un mensaje específico segun las condiciones:


#Si cumple todas las condiciones , debe imprimir :"Acceso permitido" 
# si tiene entrada vpalidad pero esta en la lista negra , "Acceso denegado, listya negra"
#si no tiene entrada vpalida imrpimri "necesitas una entrada válida "
#Si no cumple con ninguna de las condiciones anteroiores debe imprimir "Acceso denegado Revisa los requisitos"

entrada = True
edad=18
blacklist=True

if entrada and edad>=18 and not blacklist:
    print('disfruta')
elif entrada and blacklist:
    print('Estas vetado')
elif not entrada:
    print('No tienes entrada válida')
else:
    print('Acceso denegado revisa los requisitos')

