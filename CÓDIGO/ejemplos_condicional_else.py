# se generararan varios ejemplos con el condicional else            

#objetivo: escribir un programa en python que permita a un usuario ingresar un nombre y una contraseña
#Puntos principales: debe verificar que name y password sean correctos, ambos inputs tienen que ser correctos, usar and para el programa 


name= str(input("ingrese un nombre de usuario:"))[:5]
password= str(input("ingrese una contraseña:")) [:4]
usuario= 'admin'
contraseña='1234'

#el name y el password en los inputs tienen que ser iguales 
if name == usuario and password == contraseña :
    print('bienvenido al sistema')
elif name != usuario and password ==  contraseña: # estos dos caracateres indican es diferente (!=)
    print ('nombre de usuario erroneo')
elif name == usuario and password != contraseña: #mostrar que la constraseña o el nombre de usuario esta mal, representa un grave problema de seguridad porque con un solo dato que se sepa que este bien o mal existe la posibilidad de que se descubran datos sensibles
    print('contraseña erronea')
else:
    print('ambos datos son erroneos')