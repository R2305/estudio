#autoincremento de una variable 
for z in range (2):
    print (f"el valor de z es: {z}")
    print ("es el autoincremento:",z)



print("dame dos numeros:")
numero1 = int(input()) 
numero2 = int(input())

#suma de dos números
suma = numero1 + numero2
print (suma)
#resta de dos números
resta = numero1 - numero2   
print (resta)

#multiplicación de dos números
multiplicacion = numero1 * numero2
print (multiplicacion)

#ingresa variables para división, módulo 
print("ingresa dos números para división y módulo:")
a = float(input())
b = float(input())

division = a / b
print ("es la division:",division)

modulo = a % b
print ("es el modulo:",modulo)

# ingresa variables para potencia, x = base y = exponente
print("ingresa la base y el exponente:")
x= float(input())
y= float(input())
potencia = x ** y   
print ("es el número elevado:",potencia)  

#operaciones combinadas suma, resta, multiplicación y división
operacion_combinada = (numero1 + numero2) * ((numero1 - numero2)+1) / numero1
print ("es la operacion combinada:",operacion_combinada)

#division redondeada a 2 decimales
dividendo =1 
divisor = 3
division_2_decimales = round(dividendo / divisor, 2) #round sirve para redondear un número a una cantidad con decimales exactos
print ("es la division redondeada a 2 decimales:",division_2_decimales)